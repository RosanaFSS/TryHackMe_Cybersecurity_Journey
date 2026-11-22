<h1 align="left">Supervising AI-Assisted Investigations</h1>

<p align="left">
  <img src="https://img.shields.io/static/v1?label=Category&message=SOC&color=24292e&style=flat-square&v=1" /> &nbsp;
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Level-Easy-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Completed-2026, Nov 22%20-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white"  alt="LinkedIn"/></a> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white" height="30" alt="GitHub"/></a> &nbsp;
</p> 

<h3>Incident Scenario</h3>
<h4>Northbridge Finance Group: Security Operations, 02:17</h4>

<p>The night analyst reviewed a service-account logon alert and left <code>NFG-CASE-2047</code> open. An assistive workflow wrote the note in it, saying no persistence occurred on <code>NFG-FS-01</code> in the 28 July 2026 window.<br><br>

The note is well formed and its references resolve. Nobody has checked whether its searches were wide enough to support a claim about the rest of the host.<br><br>

Don't repeat the triage. Work out how that conclusion was produced and test it against the evidence</p><br>

<p><em>Answer the questions below</em></p>

<p>Which Case tag shows that the generated note is still waiting for analyst review?<br>
<code>awaiting-analyst-verification</code></p>

<p>In the recorded run, which <code>model.operation</code> value identifies the step that produced the generated conclusion?<br>
<code>model_synthesis</code></p>

<p>In the recorded run, which <code>lookup.id</code> value identifies the registry-based persistence search?<br>
<code>registry_persistence</code></p>

<p>What value do the two persistence lookups hold in <code>lookup.coverage_status</code>?<br>
<code>partial</code></p>

<p>What <code>validation.result</code> value was recorded before the generated note was written to the Case?<br>
<code>schema_and_citation_passed</code></p>

<p>How many events does the channel count return for Microsoft-Windows-Sysmon/Operational?<br>
<code>29</code></p>

<p>Which source family holds 123 records in the manifest but was not included in the cited persistence searches? Enter the name as the manifest writes it.<br>
<code>Microsoft-Windows-PowerShell/Operational</code></p>

<p>Which claim status label should be recorded for the generated persistence claim?<br>
<code>Unsupported</code></p>

<p>Which activity status did we record for persistence beyond the scope of the cited searches?<br>
<code>Unresolved</code></p>

<p>Which value does the supervision receipt print once the Tier 2 handover check passes?<br>
<code>NFG-HANDOVER------------------</code></p>


<br>
<br>

<img width="1898" height="616" alt="image" src="https://github.com/user-attachments/assets/a1a3d9da-ca57-4a5e-b9f9-cae68c504cc3" />

<br>
<br>

<img width="1886" height="819" alt="image" src="https://github.com/user-attachments/assets/2e93a407-487b-45ee-8de2-5054ccec89b7" />

<br>
<br>

<img width="1897" height="456" alt="image" src="https://github.com/user-attachments/assets/a74db329-20a8-4cad-a2b2-b431087e680d" />

<br>
<br>
<p>Control Searches</p>

```elastic
FROM northbridge-events
| WHERE host.name == "NFG-FS-01"
  AND @timestamp >= TO_DATETIME("2026-07-28T14:18:20Z")
  AND @timestamp <= TO_DATETIME("2026-07-28T16:15:00Z")
| KEEP @timestamp, host.name, event.code, event.provider, winlog.channel, winlog.record_id, casework.evidence_id
| SORT @timestamp ASC
```

<img width="1881" height="341" alt="image" src="https://github.com/user-attachments/assets/9fe6e654-3f89-4f4e-b095-f15751977cb4" />

<br>
<br>

```elastic
FROM northbridge-events
| WHERE host.name == "NFG-FS-01"
  AND @timestamp >= TO_DATETIME("2026-07-28T14:18:20Z")
  AND @timestamp <= TO_DATETIME("2026-07-28T16:15:00Z")
| STATS events = COUNT(*) BY winlog.channel
| SORT events DESC
```

<img width="1890" height="600" alt="image" src="https://github.com/user-attachments/assets/332cd5c9-6e90-4041-8eef-b5bad4337627" />

<br>
<br>

```elastic
FROM northbridge-events
| WHERE host.name == "NFG-FS-01"
  AND @timestamp >= TO_DATETIME("2026-07-28T14:18:20Z")
  AND @timestamp <= TO_DATETIME("2026-07-28T16:15:00Z")
  AND (
    (
      winlog.channel == "Microsoft-Windows-Sysmon/Operational"
      AND event.code IN ("12", "13")
      AND (
        winlog.event_data.TargetObject LIKE "*CurrentVersion*Run*"
        OR winlog.event_data.TargetObject LIKE "*Schedule*TaskCache*Tree*"
      )
    )
    OR (winlog.channel == "Microsoft-Windows-TaskScheduler/Operational" AND event.code IN ("106", "140", "141"))
    OR (winlog.channel == "Security" AND event.code == "4698")
  )
| KEEP @timestamp, host.name, event.code, event.provider, winlog.channel, winlog.event_data.TargetObject, winlog.record_id, casework.evidence_id
| SORT @timestamp ASC
```

<br>
<br>

```elastic
FROM northbridge-evidence-manifest
| WHERE release.id == "NFG-SUPERVISION-ELASTIC-20260828"
| KEEP release.id, evidence.record_count, evidence.hosts, evidence.transform_version
| LIMIT 10
```

<img width="1901" height="476" alt="image" src="https://github.com/user-attachments/assets/5919ed64-4bd9-4c88-9bc5-af7c5edf3d50" />


<br>
<br>

<img width="1864" height="493" alt="image" src="https://github.com/user-attachments/assets/5c150eba-5886-415c-b035-646e8a4f570e" />

<br>
<br>

<img width="783" height="848" alt="image" src="https://github.com/user-attachments/assets/10f49dcb-ba15-45b8-ae1b-6c54160bed43" />

<br>
<br>
<br>

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/2a43d23c-bdcd-42ef-8633-f24bcb061d1b"><br>
                  <img width="300px" src="https://github.com/user-attachments/assets/ea14feca-5731-4416-ba15-351ea00f91e3"></p>
