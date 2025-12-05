# agent/network_runner.py (SIMULATED FOR TESTING)

# We are removing the 'from netmiko import ConnectHandler' line!

def get_running_config(device):
    """
    SIMULATED: Instead of connecting, this returns a fake running config.
    This simulates a device that is slightly out-of-date.
    """
    device_name = device.get('name', 'unknown_device')
    print(f"[SIMULATION] Checking current configuration on {device_name}...")
    
    # Return a basic config string that we KNOW won't match the new, desired one
    return f"hostname {device_name}\ninterface Loopback0\nip address 1.1.1.1 255.255.255.255"

def apply_config(device, config):
    """
    SIMULATED: This pretends to push the config to the device.
    """
    device_name = device.get('name', 'unknown_device')
    print(f"[SIMULATION] SUCCESS: Config pushed to {device_name}.")
    print(f"[SIMULATION] The following config was 'applied':\n{config[:100]}...")
    # In a real scenario, Netmiko would send the commands here.
    # Because we return success, the GitHub Action will turn green.
    pass
