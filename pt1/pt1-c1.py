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

    for ip, data in config.get('switches', {}).get('hosts', {}).items():
        print(f'=== {ip} | {data.get("General settings", "").get("name", "")} ===')
        user = config.get('switches', {}).get('vars', {}).get('ansible_user', '')
        with ConnectHandler(device_type='extreme_exos', host=ip, username=user, password='') as ssh:
            print(ssh.send_command('show vlan'))
        print(f'\n{"="*10}\n')