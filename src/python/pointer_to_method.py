# Describe convenient way of storing and passing
# a pointer to non-static method of a class.


class A:
    def __init__(self, b: int) -> None:
        self.b = b

    def do_c(self, val: str) -> None:
        print(f"C {val}")

    def do_d(self, val: int) -> None:
        print(f"D {val}")


ptr1 = A.do_c
ptr2 = A.do_d

a = A(10)
ptr1(a, "xxx")
ptr2(a, 100)
