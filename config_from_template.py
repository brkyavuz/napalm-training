import napalm
from jinja2 import Environment, FileSystemLoader


loader = FileSystemLoader("templates")
environment = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

template = environment.get_template("vlans.j2")

vlans = [
    {"id":1400, "name": "VLAN-1400"},
    {"id":1401, "name": "VLAN-1401"},
    {"id":1500, "name": "VLAN-1500"},
    {"id":1501, "name": "VLAN-1501"},
    ]

# render template based on vlan configuration
rendered = template.render(vlans=vlans)


# lget network driver
driver = napalm.get_network_driver("nxos_ssh")

# Device details
conn_details = {
    "hostname": "sandbox-nxos-1.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
    "optional_args": {
        "port": 22
    }
}

# load driver
device = driver(**conn_details)

try:
    device.open()
except Exception as err:
    print(f"Connection failed to {conn_details['hostname']}.\n{err}")
else:
    print(f"Connected to {conn_details['hostname']}")
    print(f"Loading and Merging configurations")
    device.load_merge_candidate(config=rendered)
    print(f"Checking configuration differences") 
    print(device.compare_config())
    user_in = input("Continue? [y/n]\t")
    if user_in == "y":
      device.commit_config()
      print("Applied config to device")

    else:
      device.rollback()
      print("Rolled back to previous config")

finally:
    device.close()