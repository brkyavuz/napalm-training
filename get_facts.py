import napalm


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
    print(f"Getting facts...\n")
    facts = device.get_facts()
    padding = "*"*20
    print(f"{padding} {conn_details['hostname']}-Facts {padding}")
    for fact_key,fact_value in facts.items():
        print(f"{fact_key}: {fact_value}")
finally:
    device.close()