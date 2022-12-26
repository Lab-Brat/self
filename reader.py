import yaml

class SelfYAML:
    def __init__(self, yaml_file):
        self.yml = self._read_yaml(yaml_file)
        self._add_stats()
    
    def _read_yaml(self, yaml_file):
        '''
        Read self.yaml, return a dictionary
        '''
        with open(yaml_file, 'r') as file:
            return yaml.safe_load(file)

    def _get_task_stat(self, task):
        '''
        Get information about a task,
        print the result.
        '''
        return len(task['status']) / task['times']

    def _get_full_stat(self, section):
        '''
        Get completetion rate of the section.
        '''
        sm = 0
        for i, task in enumerate(self.yml[section]):
            sm += len(task['status']) / task['times']
        return ((sm/(i+1))*100)

    def _add_stats(self):
        '''
        Get information about every task.
        '''
        for section in self.yml:
            section_stat = self._get_full_stat(section)
            for task in self.yml[section]:
                task_stat = self._get_task_stat(task)
                task['stat'] = task_stat
            self.yml[section].append({'stat': section_stat})

    def _pass_or_fail(self, result, classes):
        '''
        Determina wether the weekly goals were achieved or not.
        '''
        pass_or_fail = result/classes
        if pass_or_fail < 80.0:
            print('weekly goals _FAILED_')
        else:
            print('weekly goals _COMPLETED_')

    def show_result(self):
        '''
        Print weekly detailed statistics.
        '''
        for cat in self.yml:
            stat = self.yml[cat][-1]['stat']
            print(f"{cat} [{stat:.2f}%]:")
            for task in self.yml[cat]:
                if len(task) > 1:
                    dash = (20 - len(task['task'])) * '-'
                    match task['stat']:
                        case 1.0:
                            print(f"{task['task']} {dash} Done!")
                        case _:
                            print(f"{task['task']} {dash} { task['stat']*100:.2f}%")
            print('\n')



if __name__ == '__main__':
    ya = SelfYAML('self.yaml')
    ya.show_result()
