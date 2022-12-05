import yaml

class SelfYAML:
    def __init__(self, yaml_file):
        self.yml = self._read_yaml(yaml_file)
    
    def _read_yaml(self, yaml_file):
        '''
        Read self.yaml, return a dictionary
        '''
        with open(yaml_file, 'r') as file:
            return yaml.safe_load(file)

    def _get_task_info(self, task):
        '''
        Get information about a task,
        print the result.
        '''
        name = task['task']
        dash = (20 - len(name)) * '-'
        result = len(task['status']) / task['times']
        match result:
            case 1.0:
                print(f'{name} {dash}> Done!')
            case _:
                print(f'{name} {dash}> {result*100:.2f}% done')

    def show_results(self):
        '''
        Get information about every task.
        '''
        for section in self.yml:
            print(f"{section}:")
            for task in self.yml[section]:
                self._get_task_info(task)
            print('\n')


if __name__ == '__main__':
    ya = SelfYAML('self.yaml')
    ya.show_results()
