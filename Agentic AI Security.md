<h1 align="left">Agentic AI Security</h1>
<p align="left">
  <img src="https://img.shields.io/badge/Category-Agentic%20AI%20Security-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Completed-2026, Nov 4%20-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white"  alt="LinkedIn"/></a> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white" height="30" alt="GitHub"/></a> &nbsp;
</p> 


<br>
<p>OWASP Top 10 for Agentic Applications</p>

<div align="center"><p>
  
|ID<br><br>    |Where<br><br>   |L<br><br>   |Common Vulnerabilities<br><br>|
|:-----------------------|:--------------------------------|:--------------------------------|:--------------------------------|
|ASI01: Agent Goal Hijack<br><br><br>                         |Inputs<br><br><br><br>     |What the `fix` changes?<br><em>Changes what the agent<br>was told.</em> &nbsp;&nbsp; = `GOAL`<br><br>|______________________________________________________________<br><br><br><br>|
|ASI02: Tool Misuse<br>and Exploitation<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>   |Outputs<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>     |What a `tool` was given?<br><br>What a `tool` was given?<br>_____________________________<br><br><br><br>What a `tool` reaches?<br>- Access to private data<br>- Exposure to untrusted content<br>- Communicate externally<br><br><br><br><br><br><br><br>| ⚡︎ &nbsp;&nbsp; Over-privileged tool access<br><br>⚡︎ &nbsp;&nbsp; Over-scoped tool access<br>&nbsp;&nbsp;&nbsp;&nbsp; `Scope` is a claim about the answer, not the question.<br>&nbsp;&nbsp;&nbsp;&nbsp; Different tools can read same records and hand back<br>&nbsp;&nbsp;&nbsp;&nbsp; very different amounts of what they found.<br><br>⚡︎ &nbsp;&nbsp; External data tool poisoning<br>&nbsp;&nbsp;&nbsp;&nbsp; Assess the `allowlist` as a whole, rather than tool by<br>&nbsp;&nbsp;&nbsp;&nbsp; tool.<br><br><br><br> ⚡︎ &nbsp;&nbsp; Loop amplification<br><br>⚡︎ &nbsp;&nbsp; Unvalidated input forwarding<br><br> ⚡︎ &nbsp;&nbsp; Unsafe browsing or federated calls<br><br>|
|ASI03: Agent Identity<br>and Privilege Abuse<br><br>         |Inputs<br><br><br><br><br>|Agent acts under<br>`permissions`nobody<br>granted.<br><br><br>||
|ASI04: Agentic Supply<br>Chain Vulnerabilities<br><br>       |<br><br><br> |||
|ASI05: Unexpected Code<br>Execution (RCE)<br><br>            |<br><br><br> |||
|ASI07: Insecure InterAgent Communication<br><br>             |Integration/<br>Processing<br><br><br> |||
|ASI09: HumanAgent<br>Trust Exploitation<br><br>              |Inputs<br><br><br><br><br> |||
|ASI10: Rogue Agents<br><br><br>                              |Integration/<br>Processing<br><br><br> |||

</p></div>

<br>

<h3>Study Case</h3>
<p>

- Relevant Guardrails (6 are switched off):<br>- `quarantine_output` &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Frame returned content as data rather than instruction.<br>- `max_rows` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Cap the rows returned.<br>- `redact_identifiers` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mask account identifiers in returned lines.<br>- `egress_allowlist` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Reject a destination not on the approved sink list.<br>- `scan_for_identifiers` &nbsp;&nbsp; Reject a body containing account identifiers.<br>- `max_range` &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Reject a window longer than the caller's retention entitlement. (ceiling)<br>- `require_human_origin` &nbsp;&nbsp; Reject a schedule the user did not ask for<br>- `max_scheduled_tasks` &nbsp;&nbsp;&nbsp;&nbsp; Cap how many schedules exist. (ceiling)<br><br><br>
- `log-agent` is a telemetry specialist:<br>3 capabilities<br> - Reads the company´s own records.<br>- Reads text that people outside the company wrote.<br>- Sends what it finds somewhere else.<br><br>2 identities<br>- `telemetry-read-svc` (for its reads)<br>- `telemetry-export-svc` (for anything that leaves)<br><br>8 tools (`allowlist`)<br>`query_logs`, `read_metrics`, `read_attached_doc`, `recall_context`, `store_context`, `export_report`, `export_logs`, `schedule_followup`. `log-agent` tool `read_metrics` &nbsp;&nbsp;&nbsp;&nbsp; returns rates and counts. `log-agent` tool `query_logs` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; returns the matching line in full (usernames, request paths, and more).<br><br>
- Request `R-4902` was raised by Priya in the Data Team. She didn´t write an attachment on the quarterly review. `access-review.md` was uploaded by a contractor on the audit engagement, using a guest serrvice account. That nakes the author an outsider.<br>`log-agent` reads attachments with the tool `read_attached_doc`. -> `access-review` : `R-4902`<br>Approved reporting sinks = `sinks.trytrainme.invalid/eng-leads` and `sinks.trytrainme.invalid/security`<br><br>
- The `log-agent` handled the request and found 24 rows of audit figures for the quarterly access review on `R-4902`. The full account listing was exported to the engineering leads at `sinks.trytrainme.invalid/eng-leads` with export ID `R-4902-1` and to the compliance intake at `sinks.trytrainme-compliance.invalid/audit-intake` with export `ID R-4902-2`. Both exports were successfully completed.<br>
<br><br>
</p>


