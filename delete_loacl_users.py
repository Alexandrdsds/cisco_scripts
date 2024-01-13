from netmiko import ConnectHandler
from pprint import pprint
import re
import netmiko
import json
import os
import subprocess
def configure_radius(switches,privileges):

    for switch in switches:
        try:
            cisco_router = {
                'device_type': 'cisco_ios',
                'host': switch,
                'username': 'nadubov',
                'password': 'Wanga15',
                'secret': 'Qq123456',
                'port': 22,
                "session_log": f"netmiko_session_{switch}.log"
                }
            print(f"---------------Connect to {switch}------------------------------------")
            ssh = ConnectHandler(**cisco_router)
            ssh.enable()
            ssh.send_config_set(privileges,exit_config_mode=False)
            ssh.send_config_set("username hdcrp privilege 5",exit_config_mode=False)
            print("Privilege level for hdcrp has been changed successfully")
            ssh.send_config_set("username administrator privilege 15 secret *r_xAV*5Ln8uh^57CT6*",exit_config_mode=True)
            print("Password for administrator has been changed successfully")
            output = ssh.send_command("show run | sec username",expect_string=r'#')
            pattern = r'username\s+(\S+)'
            matches = re.finditer(pattern,output)
            for match in matches:
                username = match.group(1)
                if username != "hdcrp" and username != "administrator" and username != 'nadubov':
                    print(f"delete {username}")
                    ssh.config_mode()
                    ssh.send_command(f"no username {username}",expect_string=r"confirm")
                    ssh.send_command("y",r'#')
            ssh.exit_config_mode()
            ssh.send_command('wr')
            ssh.disconnect()
        except:
            print(f"Device {switch} is unavailable")
        
switches = [
            '10.51.130.1',
            '10.51.130.10',
            '10.51.130.2',
            '10.51.130.3',
            '10.51.130.5',
            '10.51.130.6',
            '10.51.130.7',
            '10.51.130.9',
            '10.51.130.12',
            '10.51.130.13',
            '10.51.130.14',
            '10.51.130.17',
            '10.51.130.18',
            '10.51.130.19',
            '10.51.130.23',
            '10.51.130.24',
            '10.51.130.25',
            '10.51.130.26',
            '10.51.130.27',
            '10.51.130.29',
            '10.51.130.31',
            '10.51.130.33',
            ]

privileges = ["privilege interface level 5 switchport access vlan",
"privilege interface level 5 switchport access",
"privilege interface level 5 switchport",
"privilege configure level 5 interface",
"privilege exec level 5 configure terminal",
"privilege exec level 5 configure",
"privilege exec level 5 show",
"privilege exec level 5 clear port-security all",
"privilege exec level 5 clear port-security",
"privilege exec level 5 clear",
"privilege interface level 5 switchport voice vlan",
"privilege interface level 5 switchport voice",
"privilege exec level 5 show ip interface brief",
"privilege exec level 5 show ip interface",
"privilege exec level 5 show ip",
"privilege exec level 5 show arp",
]
configure_radius(switches,privileges)
