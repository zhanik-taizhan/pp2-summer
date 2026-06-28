# Parse JSON file and print interface information

import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<55} {'Description':<15} {'Speed':<8} {'MTU'}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    print(
        f"{attributes['dn']:<55} "
        f"{attributes['descr']:<15} "
        f"{attributes['speed']:<8} "
        f"{attributes['mtu']}"
    )