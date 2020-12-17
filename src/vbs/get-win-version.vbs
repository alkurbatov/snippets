Function GetOsVersion()
        Dim strComputer : strComputer = "."
        Dim objOs
        Dim objWmiService : Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\"& strComputer & "\root\cimv2")
        Dim strOsQuery : strOsQuery = "Select * from Win32_OperatingSystem"
        Dim colOperatingSystems : Set colOperatingSystems = objWMIService.ExecQuery(strOsQuery)

        For Each objOs in colOperatingSystems
                GetOsVersion = objOs.Version
        Next

End Function

Wscript.Echo GetOsVersion

