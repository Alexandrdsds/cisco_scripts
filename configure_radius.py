from netmiko import ConnectHandler
from pprint import pprint
import re
import netmiko
def configure_radius(switches,aaa_commands,radius_commands,aaa_authentications):
    
        for switch in switches:
            try:
                cisco_router = {
                    'device_type': 'cisco_ios',
                    'host': switch,
                    'username': 'nadubov',
                    'password': 'Wanga15',
                    'secret': 'Qq123456',
                    'port': 22,
                    "session_log": "netmiko_session.log"
                    }
                
                ssh = ConnectHandler(**cisco_router)
                ssh.enable()
                ssh.config_mode()
                for command in aaa_commands:
                    aaa_result = ssh.send_command(command,expect_string=r'#')
                    print(aaa_result)
                for r_command in radius_commands:
                    ssh.send_command(r_command, expect_string=r"#")
                ssh.exit_config_mode()
                print(f'RADIUS server configured successfully for {switch}.')
                for aaa_authentication in aaa_authentications:
                    ssh.send_config_set(aaa_authentication,exit_config_mode=False)
                ssh.exit_config_mode()
                print(f'authentication configured successfully for {switch}.')
                        
            except:
                print(f"Unable to connect to the Device {switch}")
        
switches = [#'10.51.130.1',
            #'10.51.130.10',
            '10.51.130.2',
            '10.51.130.3',
            # '10.51.130.5',
            # '10.51.130.6',
            # '10.51.130.7',
            # '10.51.130.9',
            #'10.51.130.12',
            '10.51.130.13'#???????????????,
            '10.51.130.14',
            '10.51.130.17',
            '10.51.130.18',
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
aaa_commands = ['aaa new-model','aaa group server radius IAS']
radius_commands = ['server name NPS','deadtime 1']
aaa_authentications = ['aaa authentication login default local',
                       'aaa authentication login userAuthentication local group IAS',
                       'aaa authorization exec userAuthorization local group IAS if-authenticated',
                       'aaa authorization network userAuthorization local group IAS',
                       'aaa accounting exec default start-stop group IAS',
                       'aaa accounting system default start-stop group IAS',
                       'radius server NPS',
                       'address ipv4 10.201.62.38 auth-port 1812 acct-port 1813',
                       'key secret','line vty 0 4','authorization exec userAuthorization',
                       'login authentication userAuthentication','end']

configure_radius(switches,aaa_commands,radius_commands,aaa_authentications)
