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
|ASI01: Agent Goal Hijack<br><br><br>                         |<strong>INPUTS</strong><br><br><br><br>     |What the `fix` changes?<br><em>Changes what the agent<br>was told.</em> &nbsp;&nbsp; = `GOAL`<br><br>|______________________________________________________________<br><br><br><br>|
|ASI02: Tool Misuse<br>and Exploitation<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>   |<strong>OUTPUTS</strong><br>Agent held together a `set of tools` that shouldn´t.<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>     |What a `tool` was given?<br><br>What a `tool` was given?<br>___________________________<br><br><br><br>What a `tool` reaches?<br>- Access to private data<br>- Exposure to untrusted content<br>- Communicate externally<br><br><br><br><br><br><br><br>| ⚡︎ &nbsp;&nbsp; Over-privileged tool access<br><br>⚡︎ &nbsp;&nbsp; Over-scoped tool access<br>&nbsp;&nbsp;&nbsp;&nbsp; `Scope` is a claim about the answer, not the question.<br>&nbsp;&nbsp;&nbsp;&nbsp; Different tools can read same records and hand back<br>&nbsp;&nbsp;&nbsp;&nbsp; very different amounts of what they found.<br><br>⚡︎ &nbsp;&nbsp; External data tool poisoning<br>&nbsp;&nbsp;&nbsp;&nbsp; Assess the `allowlist` as a whole, rather than tool by<br>&nbsp;&nbsp;&nbsp;&nbsp; tool.<br><br><br><br> ⚡︎ &nbsp;&nbsp; Loop amplification<br><br>⚡︎ &nbsp;&nbsp; Unvalidated input forwarding<br><br> ⚡︎ &nbsp;&nbsp; Unsafe browsing or federated calls<br><br>|
|ASI03: Agent Identity<br>and Privilege Abuse<br><br><br><br><br><br><br><br><br><br>     |<strong>INPUTS</strong><br>Agent acts under a <br>`credential` nobody<br>granted.<br><br><br><br><br><br><br><br><br>|<br><br><br><br><br><br><br>|⚡︎ &nbsp;&nbsp; Un-scoped Privilege `Inheritance`<br><br>⚡︎ &nbsp;&nbsp; Memory-Based Privilege Retention & Data Leakage<br><br>⚡︎ &nbsp;&nbsp; Cross-Agent Trust Exploitation (Confused Deputy<br><br>⚡︎ &nbsp;&nbsp; Time-of-Check to Time-of-Use (`TOCTOU`)<br>&nbsp;&nbsp;&nbsp;&nbsp; in Agent Workflows<br><br>⚡︎ &nbsp;&nbsp; Synthetic Identity Injection<br><br>|
|ASI04: Agentic Supply<br>Chain Vulnerabilities<br><br>       |<br><br><br> |||
|ASI05: Unexpected<br>Code Execution<br>(RCE)<br><br>         |<br><br><br> |||
|ASI06: Memory &<br>Context Poisoning<br><br><br>             |<br><br><br> |||
|ASI07: Insecure InterAgent Communication<br><br>             |<strong>INTEGRATION/<br>PROCESSING</strong><br><br><br> |||
|ASI8: Cascading Failures<br><br><br>                         |<strong>INTEGRATION/<br>PROCESSING</strong><br><br><br> |||
|ASI09: HumanAgent<br>Trust Exploitation<br><br><br>              |<strong>INPUTS</strong><br><br><br><br> |||
|ASI10: Rogue Agents<br><br><br>                              |<strong>INTEGRATION/<br>PROCESSING</strong><br><br><br> |||

</p></div>

<br>
<br>
<p>
  
- A `non-human identity` (NHI) is any credential that authenticates software rather than a person:<br>- a service account<br>- an API key<br>- an OAuth token<br>- a signed assertion<br>- a certificate.<br><br>
- `Identity` is recorded per call rather than per agent.<br>Agents holds one `credential` = `service identity` for each kind of action it performs.<br><br>
- `Estate´s inventory` = agents and their credentials.<br><br>
- A `tool` declares the `identity` it runs under. The `estate` honours that declaration without checking it against the agent making the call.<br><br>Anywhere an `identity` is a `configuration value` rather than something derived from the `caller`, it can be set to a `value` the `caller` could not have obtained for itself.<br><br>`Identity sprawl` is credentials accumulating across agents faster than anyone is tracking them. </p>

<br>
<br>
<br>

<h3>Study Case 1</h3>
<p>

- Relevant Guardrails (6 were switched off):<br>- `quarantine_output` &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Frame returned content as data rather than instruction.<br>- `max_rows` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Cap the rows returned.<br>- `redact_identifiers` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mask account identifiers in returned lines.<br>- `egress_allowlist` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Reject a destination not on the approved sink list.<br>- `scan_for_identifiers` &nbsp;&nbsp; Reject a body containing account identifiers.<br>- `max_range` &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Reject a window longer than the caller's retention entitlement. (ceiling)<br>- `require_human_origin` &nbsp;&nbsp; Reject a schedule the user did not ask for<br>- `max_scheduled_tasks` &nbsp;&nbsp;&nbsp;&nbsp; Cap how many schedules exist. (ceiling)<br><br><br>
- `log-agent` is a telemetry specialist:<br>3 capabilities<br> - Reads the company´s own records.<br>- Reads text that people outside the company wrote.<br>- Sends what it finds somewhere else.<br><br>2 identities<br>- `telemetry-read-svc` (for its reads)<br>- `telemetry-export-svc` (for anything that leaves)<br><br>8 tools (`allowlist`)<br>`query_logs`, `read_metrics`, `read_attached_doc`, `recall_context`, `store_context`, `export_report`, `export_logs`, `schedule_followup`. `log-agent` tool `read_metrics` &nbsp;&nbsp;&nbsp;&nbsp; returns rates and counts. `log-agent` tool `query_logs` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; returns the matching line in full (usernames, request paths, and more).<br><br>
- Request `R-4902` was raised by Priya in the Data Team. She didn´t write an attachment on the quarterly review. `access-review.md` was uploaded by a contractor on the audit engagement, using a guest serrvice account. That nakes the author an outsider.<br>`log-agent` reads attachments with the tool `read_attached_doc`. -> `access-review` : `R-4902`<br>Approved reporting sinks = `sinks.trytrainme.invalid/eng-leads` and `sinks.trytrainme.invalid/security`<br><br>
- The `log-agent` handled the request and found 24 rows of audit figures for the quarterly access review on `R-4902`. The full account listing was exported to the engineering leads at `sinks.trytrainme.invalid/eng-leads` with export ID `R-4902-1` and to the compliance intake at `sinks.trytrainme-compliance.invalid/audit-intake` with export `ID R-4902-2`. Both exports were successfully completed.<br>
<br><br>
</p>

<h3>Study Case 2</h3>
<p>

- Session was started when ticke `R-913` was raised asking for an entitlement review on the account `m.reyes`.<br>It returned the entire directory rather than the one account that was asked about --> `Entitlements Store` = `rows`= `214`.<br>0004 &nbsp;  | &nbsp; `desk-agent` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | `tool.call` &nbsp;&nbsp;&nbsp; | `read_request(request_id=R-4913) identity=desk-read_svc`<br>0005 &nbsp;  | &nbsp; `access-agent` &nbsp;&nbsp;&nbsp; | `tool.call` &nbsp;&nbsp;&nbsp; | &nbsp; `read_request(request_id=R-4913) identity=desk-read_svc`<br>0010 &nbsp;  | &nbsp; `desk-agent` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | `tool.call` &nbsp;&nbsp;&nbsp; | `check_role(account=m.reyes) identity=access-admin-svc`<br>0012 &nbsp;  | &nbsp; `access-agent` &nbsp;&nbsp;&nbsp; | `tool.result` | `check_role ok rows=214 bytes=61840`
- 
- </p>




