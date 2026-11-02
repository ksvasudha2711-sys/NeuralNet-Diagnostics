# NetSage AI — Responsible AI / Human Review Log

> **Scope:** Project/test dataset results only. These entries are simulated review records created to demonstrate the human-oversight workflow. They are not measurements of real-world AI performance. No live AI model or Packet Tracer execution is claimed here.

## Why human review is required

Network configuration changes can cause outages or weaken security. NetSage AI therefore produces recommendations rather than executing fixes. A reviewer checks the supplied evidence, topology intent, security policy, and reversibility before choosing **ACCEPT**, **EDIT**, or **REJECT**.

## Review summary

| Metric | Count |
|---|---:|
| Total cases reviewed | 32 |
| Accepted diagnoses | 28 |
| Edited diagnoses | 3 |
| Rejected diagnoses | 1 |
| AI-human agreement rate | 87.5% |

**Agreement calculation:** accepted diagnoses / total reviewed = 28 / 32 × 100 = **87.5%**. “Edited” and “Rejected” are counted as not fully accepted as initially proposed.

### Dashboard-ready issue summary

| Issue Type | Number of Cases |
|---|---:|
| VLAN access-port assignment | 1 |
| 802.1Q trunk allowed VLANs | 1 |
| Access VLAN configuration | 1 |
| VLAN segmentation | 1 |
| Default gateway mismatch | 1 |
| Gateway addressing | 1 |
| Inter-VLAN gateway configuration | 1 |
| Server default gateway | 1 |
| DHCP pool/network mismatch | 1 |
| DHCP and interface state | 1 |
| DHCP default-router option | 1 |
| DHCP address exhaustion | 1 |
| DNS resolver configuration | 1 |
| DNS server address | 1 |
| DNS traffic filtering | 1 |
| Static name resolution | 1 |
| Static/dynamic routing | 1 |
| Missing route | 1 |
| Return path routing | 1 |
| OSPF network advertisement | 1 |
| Extended ACL | 1 |
| SSH ACL filtering | 1 |
| ACL order and guest isolation | 1 |
| ACL protocol/port filtering | 1 |
| PAT/NAT configuration | 1 |
| NAT ACL scope | 1 |
| NAT inside/outside interface roles | 1 |
| Static PAT | 1 |
| Wireless VLAN trunking | 1 |
| Wireless guest NAT | 1 |
| Guest Wi-Fi isolation | 1 |
| Wireless authentication | 1 |

| Severity (source case) | Number of Cases |
|---|---:|
| Medium | 10 |
| High | 20 |
| Critical | 2 |

### ASCII dashboard

```text
AI decision status
Accepted ████████████████████████████ 28
Edited    ███ 3
Rejected  █ 1

Agreement: 87.5% (28/32)
```

## Detailed review cases

### 1. NS001 — Accepted
**AI initial prediction:** PC access port may be in the wrong VLAN.

**Human finding:** No correction; reviewer confirmed Fa0/4 is in VLAN 1 while it should be VLAN 20.

**Evidence:** show interfaces Fa0/4 switchport: Access Mode VLAN 1; show vlan brief: VLAN 20 exists.

**Final diagnosis:** Fa0/4 is assigned to VLAN 1 instead of VLAN 20.

**Review rationale:** Accepted because the supplied switchport evidence directly supports the diagnosis.

### 2. NS002 — Accepted
**AI initial prediction:** VLAN 30 is not allowed on the SW1-SW2 trunk.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** SW2#show interfaces trunk; Port Fa0/1 Status trunking; Port Fa0/1 Vlans allowed on trunk 10,20; SW2#show vlan brief; 30 SERVERS active

**Final diagnosis:** VLAN 30 is not allowed on the SW1-SW2 trunk.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 3. NS003 — Accepted
**AI initial prediction:** Fa0/8 is still assigned to VLAN 1 rather than VLAN 40.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** SW1#show vlan brief; 40 VOICE active Fa0/9; SW1#show interfaces Fa0/8 switchport; Access Mode VLAN: 1 (default)

**Final diagnosis:** Fa0/8 is still assigned to VLAN 1 rather than VLAN 40.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 4. NS004 — Accepted
**AI initial prediction:** The two switch ports are in different VLANs (50 and 60).

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** SW1#show vlan brief; 50 ENGINEERING active Fa0/5; 60 TEST active Fa0/6; PC-A 192.168.50.10/24; PC-B 192.168.50.11/24

**Final diagnosis:** The two switch ports are in different VLANs (50 and 60).

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 5. NS005 — Accepted
**AI initial prediction:** PC-A uses gateway 192.168.10.254, but the router interface is 192.168.10.1.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** PC-A: IP 192.168.10.25 Mask 255.255.255.0 Gateway 192.168.10.254; R1#show ip interface brief; GigabitEthernet0/0 192.168.10.1 up up

**Final diagnosis:** PC-A uses gateway 192.168.10.254, but the router interface is 192.168.10.1.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 6. NS006 — Accepted
**AI initial prediction:** Host default gateway is on a different subnet (192.168.30.1).

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** PC-A: IP 192.168.20.15 Mask 255.255.255.0 Gateway 192.168.30.1; R1#show ip interface brief; G0/0 192.168.20.1 up up

**Final diagnosis:** Host default gateway is on a different subnet (192.168.30.1).

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 7. NS007 — Accepted
**AI initial prediction:** The client gateway does not match the active R1 interface for VLAN 70.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** PC-A: IP 10.70.0.20 Mask 255.255.255.0 Gateway 10.70.0.254; R1#show ip interface brief; G0/1 10.70.0.1 up up

**Final diagnosis:** The client gateway does not match the active R1 interface for VLAN 70.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 8. NS008 — Accepted
**AI initial prediction:** Server default gateway is outside its local subnet.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** Server: IP 172.16.5.50 Mask 255.255.255.0 Gateway 172.16.6.1; R2#show ip interface brief; G0/0 172.16.5.1 up up

**Final diagnosis:** Server default gateway is outside its local subnet.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 9. NS009 — Accepted
**AI initial prediction:** DHCP pool serves 192.168.10.0/24 but R1 has no interface in that subnet; clients on G0/0 are on 192.168.20.0/24.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip dhcp pool; Pool LAN10; Network 192.168.10.0 /24; Default router 192.168.10.1; R1#show ip interface brief; G0/0 192.168.20.1 up up

**Final diagnosis:** DHCP pool serves 192.168.10.0/24 but R1 has no interface in that subnet; clients on G0/0 are on 192.168.20.0/24.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 10. NS010 — Accepted
**AI initial prediction:** The router LAN interface is shutdown, so DHCP requests cannot reach the service.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip dhcp pool; Pool VLAN20; Network 192.168.20.0 /24; Default router 192.168.20.1; R1#show ip dhcp binding; Bindings: none; R1#show ip interface brief; G0/0 192.168.20.1 administratively down down

**Final diagnosis:** The router LAN interface is shutdown, so DHCP requests cannot reach the service.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 11. NS011 — Accepted
**AI initial prediction:** DHCP advertises gateway 192.168.30.254 while R1 interface is 192.168.30.1.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip dhcp pool; Pool VLAN30; Network 192.168.30.0 /24; Default router 192.168.30.254; R1#show ip interface brief; G0/1 192.168.30.1 up up

**Final diagnosis:** DHCP advertises gateway 192.168.30.254 while R1 interface is 192.168.30.1.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 12. NS012 — Accepted
**AI initial prediction:** The DHCP pool has no free leases.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip dhcp pool; Pool LAB; Network 10.0.0.0 /29; Total addresses 6; Leased addresses 6; R1#show ip dhcp binding; 10.0.0.1  ...; 10.0.0.2  ...; 10.0.0.3  ...; 10.0.0.4  ...; 10.0.0.5  ...; 10.0.0.6  ...

**Final diagnosis:** The DHCP pool has no free leases.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 13. NS013 — Accepted
**AI initial prediction:** No DNS server is configured on R1 even though clients are pointed to it.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** PC-A: IP 192.168.40.10 Mask 255.255.255.0 Gateway 192.168.40.1 DNS 192.168.40.1; R1#show running-config | include ip name-server; (no output)

**Final diagnosis:** No DNS server is configured on R1 even though clients are pointed to it.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 14. NS014 — Accepted
**AI initial prediction:** Client DNS points to 192.168.60.53, while the reachable DNS server is 192.168.50.53.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** PC-A: IP 192.168.50.10 Gateway 192.168.50.1 DNS 192.168.60.53; Server: DNS 192.168.50.53 up; R1#show ip route 192.168.50.0; C 192.168.50.0/24 is directly connected

**Final diagnosis:** Client DNS points to 192.168.60.53, while the reachable DNS server is 192.168.50.53.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 15. NS015 — Accepted
**AI initial prediction:** ACL explicitly denies DNS traffic from the client subnet to the DNS server.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show access-lists; Extended IP access list CLIENT-FILTER; 10 deny udp 192.168.60.0 0.0.0.255 host 192.168.60.53 eq domain; 20 permit ip any any; R1#show ip interface g0/0; Internet address is 192.168.60.1/24

**Final diagnosis:** ACL explicitly denies DNS traffic from the client subnet to the DNS server.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 16. NS016 — Accepted
**AI initial prediction:** The static DNS/host entry maps app.lab.local to the wrong address.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** PC-A> nslookup app.lab.local; Name: app.lab.local; Address: 10.10.10.99; DNS#show running-config | include app.lab.local; ip host app.lab.local 10.10.10.99

**Final diagnosis:** The static DNS/host entry maps app.lab.local to the wrong address.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 17. NS017 — Edited
**AI initial prediction:** A routing issue is likely because 192.168.20.0/24 is not in R1's route table.

**Human finding:** Human reviewer checked the topology and noted R2's connected LAN is 192.168.20.0/24; the missing R1 route is the specific fault, not a generic routing failure.

**Evidence:** R1 show ip route lacks 192.168.20.0/24; R2 shows it as directly connected.

**Final diagnosis:** R1 needs the intended route to R2's 192.168.20.0/24 LAN.

**Review rationale:** The AI wording was too broad; human review made the diagnosis topology-specific.

### 18. NS018 — Accepted
**AI initial prediction:** HQ R1 lacks a route to the branch network 172.16.30.0/24.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip route 172.16.30.0; % Network not in table; R2#show ip route; C 172.16.30.0/24 is directly connected, G0/0

**Final diagnosis:** HQ R1 lacks a route to the branch network 172.16.30.0/24.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 19. NS019 — Accepted
**AI initial prediction:** R2 lacks the return route to R1 LAN 192.168.1.0/24.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip route 192.168.2.0; S 192.168.2.0/24 [1/0] via 10.1.1.2; R2#show ip route 192.168.1.0; % Network not in table

**Final diagnosis:** R2 lacks the return route to R1 LAN 192.168.1.0/24.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 20. NS020 — Accepted
**AI initial prediction:** The new LAN is connected but not included in OSPF network statements, so neighbors do not learn it.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip protocols; Routing Protocol is "ospf 1"; Networks: 10.0.0.0/30; R1#show ip route 192.168.50.0; C 192.168.50.0/24 is directly connected

**Final diagnosis:** The new LAN is connected but not included in OSPF network statements, so neighbors do not learn it.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 21. NS021 — Accepted
**AI initial prediction:** ACL explicitly denies HTTPS from the user subnet to the internal web server.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show access-lists; Extended IP access list WEB-FILTER; 10 deny tcp 10.20.10.0 0.0.0.255 host 10.20.20.10 eq 443; 20 permit ip any any

**Final diagnosis:** ACL explicitly denies HTTPS from the user subnet to the internal web server.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 22. NS022 — Accepted
**AI initial prediction:** ACL denies TCP port 22 from the management subnet.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show access-lists MGMT; 10 permit icmp 192.168.99.0 0.0.0.255 any; 20 deny tcp 192.168.99.0 0.0.0.255 any eq 22; 30 permit ip any any

**Final diagnosis:** ACL denies TCP port 22 from the management subnet.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 23. NS023 — Edited
**AI initial prediction:** Guest traffic is allowed by an ACL and may be able to reach internal resources.

**Human finding:** Human reviewer confirmed the target is specifically the database/internal subnet and required security-policy review before changing the ACL.

**Evidence:** GUEST ACL rule 10 permits guest 192.168.80.0/24 to internal 10.0.50.0/24 before the broader deny.

**Final diagnosis:** Guest-to-internal access is explicitly permitted; human security approval is required before reordering/removing the permit.

**Review rationale:** ACL changes are security-sensitive; the reviewer added the policy constraint and refused an automatic fix.

### 24. NS024 — Accepted
**AI initial prediction:** ACL denies outbound HTTP (TCP/80) for the client subnet.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show access-lists OUTBOUND; 10 permit udp 192.168.60.0 0.0.0.255 any eq domain; 20 deny tcp 192.168.60.0 0.0.0.255 any eq www; 30 permit tcp 192.168.60.0 0.0.0.255 any eq 443

**Final diagnosis:** ACL denies outbound HTTP (TCP/80) for the client subnet.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 25. NS025 — Rejected
**AI initial prediction:** NAT is not translating inside hosts because no translations are present.

**Human finding:** Human reviewer rejected the conclusion that NAT configuration alone is proven faulty and requested verification of traffic generation, inside/outside roles, and the NAT ACL.

**Evidence:** show ip nat translations has no entries; statistics show Hits 0 and Misses 42.

**Final diagnosis:** NAT translation is not occurring; the exact cause requires checking the NAT rule/ACL and generating test traffic.

**Review rationale:** Empty translations show a symptom, but do not by themselves prove which NAT prerequisite is missing.

### 26. NS026 — Accepted
**AI initial prediction:** NAT ACL covers only 192.168.20.0/25, leaving the upper half of the /24 untranslated.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show running-config | include ip nat inside source; ip nat inside source list 10 interface GigabitEthernet0/1 overload; R1#show access-lists 10; 10 permit 192.168.20.0 0.0.0.127

**Final diagnosis:** NAT ACL covers only 192.168.20.0/25, leaving the upper half of the /24 untranslated.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 27. NS027 — Accepted
**AI initial prediction:** NAT outside is assigned to the wrong/down interface; the actual WAN is G0/1.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip nat statistics; Inside interfaces: GigabitEthernet0/0; Outside interfaces: GigabitEthernet0/2; R1#show ip interface brief; G0/1 203.0.113.2 up up; G0/2 unassigned administratively down down

**Final diagnosis:** NAT outside is assigned to the wrong/down interface; the actual WAN is G0/1.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 28. NS028 — Accepted
**AI initial prediction:** Port forwarding is configured on external port 8080, while the requirement is public TCP/80.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** R1#show ip nat translations; Pro Inside global 203.0.113.10:8080 Inside local 192.168.30.10:80; R1#show running-config | include ip nat inside source static; ip nat inside source static tcp 192.168.30.10 80 203.0.113.10 8080

**Final diagnosis:** Port forwarding is configured on external port 8080, while the requirement is public TCP/80.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 29. NS029 — Edited
**AI initial prediction:** DHCP service may be unavailable to wireless clients.

**Human finding:** Reviewer identified the stronger evidence: VLAN 80 is absent from the AP uplink trunk even though the guest VLAN and DHCP pool exist.

**Evidence:** AP uses VLAN 80; SW1 trunk allows only VLANs 10,20,30; R1 has a GUEST DHCP pool for 192.168.80.0/24.

**Final diagnosis:** VLAN 80 is missing from the AP uplink trunk, preventing guest DHCP traffic from reaching R1.

**Review rationale:** The AI was too general; trunk evidence provides a more specific Layer 2 cause.

### 30. NS030 — Accepted
**AI initial prediction:** Guest subnet 192.168.90.0/24 is not included in the NAT ACL, so guest traffic is not translated.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** AP#show wireless vlan; SSID Guest VLAN 90; R1#show ip interface brief; G0/2 192.168.90.1 up up; R1#show ip nat statistics; Inside interfaces: GigabitEthernet0/1; Outside interfaces: GigabitEthernet0/2; NAT ACL 15; R1#show access-lists 15; 10 permit 192.168.10.0 0.0.0.255

**Final diagnosis:** Guest subnet 192.168.90.0/24 is not included in the NAT ACL, so guest traffic is not translated.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 31. NS031 — Accepted
**AI initial prediction:** Guest ACL explicitly permits access to the internal server subnet.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** AP#show wireless vlan; SSID Guest VLAN 100; R1#show access-lists GUEST-IN; 10 permit ip 192.168.100.0 0.0.0.255 10.100.10.0 0.0.0.255; 20 permit ip 192.168.100.0 0.0.0.255 any

**Final diagnosis:** Guest ACL explicitly permits access to the internal server subnet.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

### 32. NS032 — Accepted
**AI initial prediction:** Client PSK does not match the AP PSK.

**Human finding:** No correction; reviewer confirmed the expected fault from the supplied case evidence.

**Evidence:** AP#show running-config | include ssid|wpa|passphrase; ssid LabWiFi;  authentication open;  wpa-psk ascii 0 LabNet2026; Client profile: SSID LabWiFi, WPA2-PSK, key LabNet2025

**Final diagnosis:** Client PSK does not match the AP PSK.

**Review rationale:** Accepted because the supplied case evidence supports the diagnosis.

## Responsible-AI lessons learned

1. **Traceability beats plausibility:** every diagnosis should point to concrete command output.
2. **Uncertainty should be visible:** low/medium confidence is preferable to fabricated certainty.
3. **Human control is mandatory:** recommendations are reviewed before any configuration change.
4. **Security needs a gate:** ACL, NAT, guest-isolation, and authentication changes require explicit human approval.
5. **Diagnosis is not execution:** NetSage AI does not claim that a fix was applied unless an operator actually performs and verifies it.
6. **Next-command recommendations reduce guessing:** when evidence is insufficient, collect more evidence rather than inventing it.