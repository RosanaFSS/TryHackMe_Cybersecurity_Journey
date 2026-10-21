<h1 align="center">Windows Event ID<br>Related to Groups</h1>
<p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20OCT%2021-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p
<br>
<p align="center">Ref: <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor">Microsoft</a></p><br><br>

<p>The table lists the event ID related to <code>Groups</code> as it's implemented in versions of Windows and Windows Server.<br>

The `Potential Criticality` column identifies whether the event should be considered of `Low`, `Medium`, or `High` criticality in detecting attacks.<br>
- A potential criticality of `High` means that one occurrence of the event should be investigated.<br>
- Potential criticality of `Medium` or `Low` means that these events should only be investigated if they occur unexpectedly or in numbers that significantly exceed the expected baseline in a measured period of time.<br>

The "Event Summary" column provides a brief description of the event.</p><br>

<div align="center"><p>

|Event ID|Potential Criticality|Event Summary                       |
|:-------------|:-------|:------------------------------------------------------------|
|4964          |High    |<strong>Special &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; groups</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; have been assigned to a new logon |
|              |        ||
|4727          |Medium  |<strong>Security-enabled &nbsp;&nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4730          |Low     |<strong>Security-enabled &nbsp;&nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|4737          |Medium  |<strong>Security-enabled &nbsp;&nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4731          |Low     |<strong>Security-enabled &nbsp;&nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4732          |Low     |<strong>Security-enabled &nbsp;&nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4733          |Low     |<strong>Security-enabled &nbsp;&nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|4734          |Low     |<strong>Security-enabled &nbsp;&nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|4735          |Medium  |<strong>Security-enabled &nbsp;&nbsp; <code>local</code>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4754          |Medium  |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4755          |Medium  |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4757          |Low     |<strong>Security-enabled &nbsp;&nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|4758          |Low|<strong>Security-enabled &nbsp;&nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|              |        ||
|4764          |Medium  |<strong>Type of &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; changed|
|              |        ||
|4764          |Medium  |<strong>Security-disabled &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|4728          |Low     |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|4729          |Low     |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|4744          |Low     |<strong>Security-disabled &nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4745          |Low     |<strong>Security-disabled &nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4746          |Low     |<strong>Security-disabled &nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4747          |Low     |<strong>Security-disabled &nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|4748          |Low     |<strong>Security-disabled &nbsp; <code>local</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|4749          |Low     |<strong>Security-disabled &nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4750          |Low     |<strong>Security-disabled &nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4751          |Low     |<strong>Security-disabled &nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4752          |Low     |<strong>Security-disabled &nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4753          |Low     |<strong>Security-disabled &nbsp; <code>global</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|4756          |Low     |<strong>Security-enabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4759          |Low     |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4760          |Low     |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4761          |Low     |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4762          |Low     |<strong>Security-disabled &nbsp; <code>universal</code> &nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|              |        ||
|4780          |Medium  |The ACL was set on accounts which are members of administrators groups|
|              |        ||
|4908          |Medium  |Special Groups Logon table modified|
|4783          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|
|4784          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group changed|
|4785          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member added|
|4786          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; member removed|
|4787          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nonmember added|
|4788          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nonmember removed|
|4789          |Low     |<strong>Basic application &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group deleted|
|              |        ||
|4790          |Low     |<strong>LDAP query &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group</strong>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group created|

</p></div>
