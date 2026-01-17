# import json

# # Load Wireshark JSON export
# with open("capture.json", "r") as f:
#     packets = json.load(f)

# print("=== Ethernet Packet Summary ===\n")

# for i, pkt in enumerate(packets, start=1):

#     layers = pkt.get("_source", {}).get("layers", {})
#     eth = layers.get("eth", {})

#     # Basic Ethernet fields
#     dst = eth.get("eth.dst", "N/A")
#     src = eth.get("eth.src", "N/A")
#     eth_type = eth.get("eth.type", "N/A")
#     stream = eth.get("eth.stream", "N/A")

#     # Resolved names (from *_tree)
#     dst_resolved = eth.get("eth.dst_tree", {}).get("eth.dst_resolved", "N/A")
#     src_resolved = eth.get("eth.src_tree", {}).get("eth.src_resolved", "N/A")

#     # OUI vendor lookups
#     src_vendor = eth.get("eth.src_tree", {}).get("eth.src.oui_resolved", "N/A")
#     dst_vendor = eth.get("eth.dst_tree", {}).get("eth.dst.oui_resolved", "N/A")

#     print(f"Packet #{i}")
#     print(f"  Source MAC:        {src}")
#     print(f"    Vendor:          {src_vendor}")
#     print(f"    Resolved Name:   {src_resolved}")

#     print(f"  Destination MAC:   {dst}")
#     print(f"    Vendor:          {dst_vendor}")
#     print(f"    Resolved Name:   {dst_resolved}")

#     print(f"  EtherType:         {eth_type}")
#     print(f"  Stream ID:         {stream}")
#     print("-" * 60)


import json

with open("wireshark.json", "r") as f:
    packets = json.load(f)

for pkt in packets:
    eth = pkt["_source"]["layers"]["eth"]

    src = eth.get("eth.src")
    dst = eth.get("eth.dst")
    etype = eth.get("eth.type")

    print(src, " → ", dst, " | EtherType:", etype)
