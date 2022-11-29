import yaml
from pprint import pprint

with open('self.yaml', 'r') as file:
    yml = yaml.safe_load(file)

pprint(yml)
