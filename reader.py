import yaml
from pprint import pprint

with open('self.yaml', 'r') as file:
    yml = yaml.safe_load(file)

def show_results(yml):
    for section in yml:
        print(f"{section}:")
        for task in yml[section]:
            get_task_info(task)
        print('\n')

def get_task_info(task):
    name = task['task']
    dash = (20 - len(name)) * '-'
    result = len(task['status']) / task['times']
    match result:
        case 1.0:
            print(f'{name} {dash}> Done!')
        case _:
            print(f'{name} {dash}> {result*100:.2f}% done')


if __name__ == '__main__':
    show_results(yml)
