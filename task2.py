# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import json
import netifaces  # pylint: disable=c-extension-no-member  # ✅ Disable C-extension warning
from netaddr import IPAddress

def get_ip_addresses():
    """
    Get a dictionary mapping network interface names to a list of their IPv4 addresses.
    """
    interface_to_ip = {}
    interface_list = netifaces.interfaces()  # pylint: disable=c-extension-no-member

    # Break long line for pylint compliance (C0301)
    address_entries = [
    netifaces.ifaddresses(iface) for iface in interface_list  # pylint: disable=line-too-long
]


    # map the interface name to IP address
    for key, value in zip(interface_list, address_entries):
        interface_to_ip[key] = value

    # ipv4 address types
    ipv4_address_entries = {}
    for interface, address in interface_to_ip.items():
        # extract the interface_to_ip
        if netifaces.AF_INET in address:  # pylint: disable=c-extension-no-member
            ipv4_address_entries[interface] = interface_to_ip[interface][netifaces.AF_INET]
    return ipv4_address_entries

def get_netmask_readable(ip_info):
    """
    Convert the netmask to integer format.
    """
    netmask = ip_info['netmask']
    ip_info['netmask'] = IPAddress(netmask).netmask_bits()  # ✅ Removed eval()
    return ip_info

def check_localhost(ip_info):
    """
    Check if the IP address is localhost (127.0.0.1).
    """
    ip_addr = ip_info['addr']
    if ip_addr == "127.0.0.1":  # ✅ Replaced 'is' with '=='
        return True
    return False

if __name__ == "__main__":
    ip_addresses = get_ip_addresses()
    for intf, ip in ip_addresses.items():
        ip_addresses[intf] = get_netmask_readable(ip[0])
        ip_addresses[intf]['is_localhost'] = check_localhost(ip[0])

    # Print the result as JSON
    print(json.dumps(ip_addresses, indent=4))
