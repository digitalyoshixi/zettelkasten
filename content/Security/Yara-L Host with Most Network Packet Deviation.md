---
tags:
  - security
---

```json
//calculate the total bytes exchanged per day by source and target
stage A {
  $source = principal.hostname
  $target = target.ip
  $total_bytes = cast.as_int(network.sent_bytes + network.received_bytes)
  $date = timestamp.get_date(metadata.event_timestamp.seconds)
  match:
    $source, $target, $date
  outcome:
    $exchanged_bytes = sum($total_bytes)
}
//calculate the average over the time window and compare the bytes exchanged today
$source = $A.source
$target = $A.target
$Adate = $A.date
$xchd_bytes = $A.exchanged_bytes
match:
  $source, $target
outcome:
  $today_bytes = sum(if($Adate = timestamp.get_date(timestamp.current_seconds()), $xchd_bytes, 0))
  $average_bytes = window.avg($xchd_bytes)
  //$sdev = window.stddev($A.exchanged_bytes)
  $zscore = ($today_bytes - $average_bytes) / window.stddev($xchd_bytes)
order: $zscore desc
```
![[Yara-L Host with Most Network Packet Deviation-20261110013907267.webp]]