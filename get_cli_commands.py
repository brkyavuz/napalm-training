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
# commands to run on device
commands = ["show interface status", "show version"]

# load driver
device = driver(**conn_details)

try:
    device.open()
except Exception as err:
    print(f"Connection failed to {conn_details['hostname']}.\n{err}")
else:
    print(f"Connected to {conn_details['hostname']}")
    print(f"Running commands...\n")
    result = device.cli(commands)
    padding = "*"*20
    for command,output in result.items():
        print(f"{padding} {command} {padding}")
        for line in output.split("\n"):
            print(line)

finally:
    device.close()