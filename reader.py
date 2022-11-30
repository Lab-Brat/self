import yaml
from pprint import pprint

with open('self.yaml', 'r') as file:
    yml = yaml.safe_load(file)

def show_results(yml):
    for section in yml:
        print(f"{section}:")
        for task in yml[section]:
            name = task['task']
            result = len(task['status']) / task['times']
            match result:
                case 1.0:
                    print(f'{name} ---> Done!')
                case _:
                    print(f'{name} ---> {result*100:.2f}% done')
        print('\n')


if __name__ == '__main__':
    show_results(yml)
