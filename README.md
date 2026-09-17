# Nmap XML Asset Inventory

Parses a **saved XML file from an authorized scan** and produces a compact JSON inventory of live assets and open services. It performs no scanning itself.

```bash
python main.py sample_scan.xml
python -m unittest -v
```

Demonstrates XML parsing, asset inventory, service enumeration, defensive documentation, and unit tests. Use Nmap only on systems you own or have explicit permission to test.
