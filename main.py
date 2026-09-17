"""Convert a saved Nmap XML report into a defensive asset inventory."""
from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def inventory(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    assets = []
    for host in root.findall("host"):
        status = host.find("status")
        if status is not None and status.get("state") != "up":
            continue
        addresses = {node.get("addrtype", "unknown"): node.get("addr") for node in host.findall("address")}
        ports = []
        for port in host.findall("./ports/port"):
            state = port.find("state")
            service = port.find("service")
            if state is not None and state.get("state") == "open":
                ports.append({"port": int(port.get("portid", "0")), "protocol": port.get("protocol"), "service": service.get("name") if service is not None else "unknown"})
        assets.append({"addresses": addresses, "open_ports": ports})
    return assets


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml", type=Path, help="Saved XML produced by an authorized Nmap scan")
    args = parser.parse_args()
    print(json.dumps(inventory(args.xml.read_text(encoding="utf-8")), indent=2))


if __name__ == "__main__":
    main()
