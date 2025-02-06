"""
Part 1 Task C Objective 2
"""
import yaml
from netmiko import ConnectHandler


def read_yaml(file):
    """Function to read YAML file"""
    with open(file) as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            raise e


if __name__ == '__main__':

    config = read_yaml('ansible_inventory.yaml')

    vlan_id = 10
    for ip, data in config.get('switches', {}).get('hosts', {}).items():
        if ip == '10.10.1.24':
            # No need to create any vlans on "local" switch
            continue
        user = config.get('switches', {}).get('vars', {}).get('ansible_user', '')
        with ConnectHandler(device_type='extreme_exos', host=ip, username=user, password='') as ssh:
            print(ssh.send_command(f'create vlan {vlan_id} description {data.get("General settings", "").get("name", "")}'))
            print(ssh.send_command(f'configure vlan {vlan_id} name {data.get("General settings", "").get("name", "")}'))
        print(f'\n{"="*10}\n')
        vlan_id += 1