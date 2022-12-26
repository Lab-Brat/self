import yaml
from pprint import pprint

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
        return result
        # match result:
        #     case 1.0:
        #         print(f'{name} {dash}> Done!')
        #     case _:
        #         print(f'{name} {dash}> {result*100:.2f}%')

    def _get_full_stat(self, section):
        '''
        Get completetion rate of the section.
        '''
        sm = 0
        for i, task in enumerate(self.yml[section]):
            sm += len(task['status']) / task['times']
        # return f"{(sm/(i+1))*100:.2f}%"
        return ((sm/(i+1))*100)

    def _pass_or_fail(self, result, classes):
        pass_or_fail = result/classes
        if pass_or_fail < 80.0:
            print('weekly goals _FAILED_')
        else:
            print('weekly goals _COMPLETED_')

    def show_results(self):
        '''
        Get information about every task.
        '''
        # final_result = 0.0
        for i, section in enumerate(self.yml):
            section_stat = self._get_full_stat(section)
            # final_result += section_stat
            # print(f"{section} [{section_stat:.2f}%]:")
            for task in self.yml[section]:
                task_stat = self._get_task_info(task)
                task['stat'] = task_stat
            self.yml[section].append({'stat': section_stat})
        return self.yml
        # self._pass_or_fail(final_result, (i+1))


if __name__ == '__main__':
    ya = SelfYAML('self.yaml')
    yy = ya.show_results()
    pprint(yy)
