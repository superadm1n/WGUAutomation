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

# add ansible information to each switch
for ip, data in gns_data.get('switches', {}).items():
    data['vars'] = {
        'ansible_user': 'admin',
        'ansible_connection': 'ansible.netcommon.network_cli',
        'ansible_network_os': 'exos'
    }

# save new file
write_yaml('ansible_inventory.yaml', gns_data)