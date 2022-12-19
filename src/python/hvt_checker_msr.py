import os
import sys


class MSR:
    """
    Represents Model-Specific Registers (MSR), provide an ability
    to read data by specific register from MSR file.
    """

    def __init__(self):
        self.msr_location = "/dev/cpu/0/msr"

        if os.access(self.msr_location, os.R_OK) is False:
            self.msr_location = "/dev/msr0"

    def read(self, index):
        """
        Read a 'index' register from MSR.
        Return tuple of two integer numbers: first represents 31:0 bits,
        second represents 63:32 bits.
        """

        import struct

        try:
            with open(self.msr_location, "r", 0) as src:
                src.seek(index)

                val = struct.unpack("Q", src.read(8))[0]  # type: ignore
                return (val & 0xFFFFFFFF, val >> 32)

        except Exception as err:
            print(f"Failed to read MSR: {repr(err)}", file=sys.stderr)
            return 0, 0


class CPU:
    """
    Represents generic CPU, provide useful contants and access to MSR.
    """

    def __init__(self):
        self.msr = MSR()

        self.MSR_EFER = 0xC0000080
        self.MSR_IA32_FEATURE_CONTROL = 0x3A
        self.MSR_IA32_VMX_PROCBASED_CTLS2 = 0x48B

    @staticmethod
    def get():
        """
        Return object representing current CPU. The object's type is
        determined by vendor information extracted from /proc/cpuinfo.
        """

        with open("/proc/cpuinfo") as src:
            for line in src.readlines():
                if line.startswith("vendor_id") is False:
                    continue

                if "GenuineIntel" in line:
                    return Intel()

                if "AuthenticAMD" in line:
                    return AMD()

                # Unsupported vendor
                return None


class Intel(CPU):
    """
    Represents Intel processors. Allow to check support of hardware
    virtualization (VT-x) and required CPU features using
    Model-Specific Registers (MSR) as a data source.
    For additional details please refer to 'Intel Software Developer's Manual
    Volume 3B: System Programming Guide, Part 2'.
    """

    def vt_enabled(self):
        """
        Check support of basic virtualization technology (VT-x) by checking
        VMX feature (2nd bit in MSR_IA32_FEATURE_CONTROL control).
        """

        val = self.msr.read(self.MSR_IA32_FEATURE_CONTROL)[0]
        return bool(val & (1 << 2))

    def full_featured(self):
        """
        Check support of 'Extended Page Tables (EPT)' and 'Unrestricted guest'
        features (32+1 and 32+7 bits in MSR_IA32_VMX_PROCBASED_CTLS2
        control respectively) enabled.
        """

        val = self.msr.read(self.MSR_IA32_VMX_PROCBASED_CTLS2)[1]
        return all(val & (1 << i) for i in [1, 7])

    def __str__(self):
        return os.linesep.join(
            [
                "Intel processor:",
                "\tVMX: %s" % self.vt_enabled(),
                "\tEPT and Unrestricted guest: %s" % self.full_featured(),
            ]
        )


class AMD(CPU):
    """
    Represents AMD processors. Allow to check support of hardware
    virtualization (SVM) and required CPU features using
    Model-Specific Registers (MSR) as a data source.
    For additional details please refer to
    'AMD64 Architecture Programmer's Manual'.
    """

    def vt_enabled(self):
        """
        Check support of basic virtualization technology (SVM) by checking
        SVME feature (12th bit in MSR_EFER control) enabled.
        """

        val = self.msr.read(self.MSR_EFER)[0]
        return bool(val & (1 << 12))

    def full_featured(self):
        """
        Check support of 'Rapid Virtualization Indexing (RVI)' feature
        (32+1 bit in control) enabled.
        """

        pass

    def __str__(self):
        return os.linesep.join(
            [
                "AMD processor:",
                "\tSVM: %s" % self.vt_enabled(),
                "\tRVI: %s" % self.full_featured(),
            ]
        )


def main():
    """
    Show general information about virtualization support
    of the CPU in Linux system.
    """

    print(CPU.get(), file=sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
