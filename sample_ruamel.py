## If the project use YAMK 1.2 then ruamel.yaml 0.18.6

from ruamel.yaml import YAML
from tabulate import tabulate
import os

def read_yaml(file_path):
    yaml = YAML(typ='safe')
    yaml.version = (1, 2)
    with open(file_path, 'r') as file:
        return yaml.load(file)

def display_as_table(data, parent_key=''):
    rows = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            rows.extend(display_as_table(value, full_key))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            full_key = f"{parent_key}[{index}]"
            rows.extend(display_as_table(item, full_key))
    else:
        key_type = type(parent_key).__name__
        value_type = type(data).__name__
        rows.append([parent_key, data, key_type, value_type])
    
    return rows

def main(file_path):
    data = read_yaml(file_path)
    table_data = display_as_table(data)
    print(tabulate(table_data, headers=['Key', 'Value', 'Key Type', 'Value Type'], tablefmt='grid'))

if __name__ == "__main__":
    # Assuming the YAML file is in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, 'Scaler.yml')
    main(yaml_file_path)