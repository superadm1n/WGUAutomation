
from netmiko import ConnectHandler


def read_yaml(file):
    """Function to read YAML file"""
    with open(file) as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            raise e


if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('username')

    args = parser.parse_args()

    with ConnectHandler(device_type='extreme_exos', host=args.ip, username=args.username, password='') as ssh:
        print(ssh.send_command('create account admin Local-Admin WGU123'))
