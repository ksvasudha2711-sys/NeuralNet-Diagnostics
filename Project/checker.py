#!/usr/bin/env python3
"""NetSage AI deterministic rule-based network checker.

This is an educational validator, not an AI model and not a full Cisco parser.
It inspects a small set of explicit sample facts/text and reports PASS/FAIL/
WARNING/INFO. It never changes network configuration.
"""
import ipaddress, re


def result(status, message):
    return f"[{status}] {message}"


def check_duplicate_ips(ips):
    seen = set(); duplicates = set()
    for ip in ips:
        if ip in seen: duplicates.add(ip)
        seen.add(ip)
    return result("FAIL", f"Duplicate IP(s) detected: {', '.join(sorted(duplicates))}") if duplicates else result("PASS", "No duplicate IP detected")


def check_subnet_mask(host_ip, mask, network):
    try:
        iface = ipaddress.ip_interface(f"{host_ip}/{mask}")
        expected = ipaddress.ip_network(network, strict=False)
        if iface.network == expected:
            return result("PASS", f"Subnet mask {mask} matches network {network}")
        return result("FAIL", f"Mask/network mismatch: {host_ip}/{mask} belongs to {iface.network}, not {expected}")
    except ValueError as exc:
        return result("FAIL", f"Invalid IP/mask/network data: {exc}")


def check_gateway(host_ip, mask, gateway):
    try:
        net = ipaddress.ip_interface(f"{host_ip}/{mask}").network
        gw = ipaddress.ip_address(gateway)
        if gw in net:
            return result("PASS", f"Gateway {gateway} is in host subnet {net}")
        return result("FAIL", f"Gateway mismatch: {gateway} is outside host subnet {net}")
    except ValueError as exc:
        return result("FAIL", f"Invalid gateway data: {exc}")


def check_interface_status(status):
    s = status.lower()
    if "administratively down" in s or "down down" in s:
        return result("FAIL", "Interface is administratively down/down")
    if "down" in s:
        return result("WARNING", "Interface contains a down state; inspect the physical/link condition")
    if "up up" in s:
        return result("PASS", "Interface is up/up")
    return result("INFO", "Interface state could not be classified")


def check_vlan(vlan_id, vlan_output):
    pattern = rf"^\s*{re.escape(str(vlan_id))}\s+\S+\s+active"
    if re.search(pattern, vlan_output, re.MULTILINE | re.IGNORECASE):
        return result("PASS", f"VLAN {vlan_id} exists and is active")
    return result("FAIL", f"VLAN {vlan_id} is missing or not active")


def check_routes(destination, route_output):
    if destination in route_output:
        return result("PASS", f"Route entry for {destination} is present")
    return result("WARNING", f"Route for {destination} may be missing")


def run_demo():
    print("NetSage AI — Deterministic Rule Checker (demo)\n")
    print("CASE: NS-DEMO")
    print(check_duplicate_ips(["192.168.10.10", "192.168.10.11", "192.168.10.10"]))
    print(check_subnet_mask("192.168.20.10", "255.255.255.0", "192.168.30.0/24"))
    print(check_gateway("192.168.20.10", "255.255.255.0", "192.168.30.1"))
    print(check_interface_status("GigabitEthernet0/0 192.168.20.1 administratively down down"))
    print(check_vlan(20, "10 SALES active Fa0/1\n20 STAFF active Fa0/2"))
    print(check_routes("192.168.40.0/24", "C 192.168.20.0/24 is directly connected"))
    print("\nINFO: This checker covers common patterns only; it cannot prove that a network is fully correct.")


if __name__ == "__main__":
    run_demo()
