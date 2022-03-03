import napalm


driver = napalm.get_network_driver("nxos_ssh")

conn_details = {
    "hostname": "sandbox-nxos-1.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
    "optional_args": {
        "port": 22
    }
}

device = driver(**conn_details)

device.open()

print(f"Connected to {conn_details['hostname']}")

device.close()