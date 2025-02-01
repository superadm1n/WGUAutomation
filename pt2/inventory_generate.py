import yaml


def read_yaml(file):
    """Function to read YAML file"""
    with open(file) as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            raise e


def write_yaml(file, data):
    """Function to write YAML file"""
    with open(file, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

# Read in the base YAML file
gns_data = read_yaml('gns_data.yaml')

# add ansible information for each linux host
for ip, data in gns_data.get('linux', {}).items():
    data['vars'] = {
        'ansible_password': 'P@ssw0rd',
    }

# add ansible information to each windows device
for ip, data in gns_data.get('windows', {}).items():
    data['vars'] = {
        'ansible_port': 5985,
        'ansible_user': 'Administrator',
        'ansible_password': 'P@ssw0rd',
        'ansible_connection': 'winrm',
    }

# save new file
write_yaml('ansible_inventory.yaml', gns_data)