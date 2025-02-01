"""
Part 1 Task C Objective 1
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

    for ip, data in config.get('switches', {}).items():
        print(f'=== {ip} | {data.get("General settings", "").get("name", "")} ===')
        with ConnectHandler(device_type='extreme_exos', host=ip, username=data.get('vars', {}).get('ansible_user', {}), password='') as ssh:
            print(ssh.send_command(f'create vlan 10 description {data.get("General settings", "").get("name", "")}'))
            print(ssh.send_command(f'configure vlan 10 name {data.get("General settings", "").get("name", "")}'))
        print(f'\n{"="*10}\n')