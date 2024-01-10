from netmiko import ConnectHandler
from pprint import pprint
import re
import netmiko
def configure_radius(switches):
    
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
                
                ssh = ConnectHandler(**cisco_router)
                ssh.enable()
                output = ssh.send_command("sh run | include access-list")
                if "standard Monitor" in output:
                    print(f"standard Monitor on {switch}")
                    ssh.send_config_set(["ip access-list standard Monitor","remark access for VM scripts", "permit 10.241.2.148"])
                    ssh.send_command('wr')
                    print(f"Configure successfully for {switch}")
                elif "standard Dostup" in output:
                    print(f"standard Dostup on {switch}")
                    ssh.send_config_set(["ip access-list standard Dostup","remark access for VM scripts", "permit 10.241.2.148"])
                    ssh.send_command('wr')
                    print(f"Configure successfully for {switch}")
                else:
                    print("access-list doesn't exists")
                        
            except:
                print(f"Unable to connect to the Device {switch}")
        
switches = ['10.51.130.1',
            # '10.51.130.10',
            # '10.51.130.2',
            # '10.51.130.3',
            # '10.51.130.5',
            # '10.51.130.6',
            # '10.51.130.7',
            # '10.51.130.9',
            # '10.51.130.12',
            # '10.51.130.13',
            # '10.51.130.14',
            # '10.51.130.17',
            # '10.51.130.18',
            # '10.51.130.19',
            # '10.51.130.23',
            # '10.51.130.24',
            # '10.51.130.25',
            # '10.51.130.26',
            # '10.51.130.27',
            # '10.51.130.29',
            # '10.51.130.31',
            # '10.51.130.33',
            ]


configure_radius(switches)
