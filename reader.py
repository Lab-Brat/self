import sys
import yaml
from pprint import pprint

class ReadYAML:
    def __init__(self, yaml_file):
        self.file = yaml_file
        self.yml = self._read_yaml(yaml_file)
    
    def _read_yaml(self, yaml_file):
        '''
        Read self.yaml, return a dictionary
        '''
        with open(yaml_file, 'r') as file:
            return yaml.safe_load(file)

    def _get_count(self, counts):
        '''
        '''
        if self.file == 'self.yaml':
            if isinstance(counts, int):
                return counts
            elif isinstance(counts, list):
                return len(counts)
            else:
                print('Im confused')
                sys.exit(0)
        elif self.file == 'study_plan.yaml':
            return len(counts)

    def _get_full_stat(self, block):
        '''
        Get completetion rate of the block.
        '''
        sm = 0
        for i, section in enumerate(self.yml[block]):
            if self.file == 'self.yaml':
                section_counts = self._get_count(section['time'])
            elif self.file == 'study_plan.yaml':
                section_counts = len(section['details'])
            sm += len(section['status']) / section_counts
        return ((sm/(i+1))*100)

    def _add_stats(self):
        '''
        Get information about every section.
        '''
        for block in self.yml:
            section_stat = self._get_full_stat(block)
            for section in self.yml[block]:
                if self.file == 'self.yaml':
                    count = self._get_count(section['time'])
                elif self.file == 'study_plan.yaml':
                    count = self._get_count(section['details'])
                task_stat = (len(section['status']) / count)
                section['stat'] = task_stat
            self.yml[block].append({'stat': section_stat})

    def _pass_or_fail(self, result, classes):
        '''
        Determina wether the weekly goals were achieved or not.
        '''
        pass_or_fail = result/classes
        pass_bar = 80.0
        print(f'Weekly score: {pass_or_fail:.2f}/100')
        if pass_or_fail < pass_bar:
            print(f'weekly goals _FAILED_')
        else:
            print(f'weekly goals _COMPLETED_')

    def _print_task(self, section):
        '''
        Print section statistics.
        '''
        dash = (20 - len(section['name'])) * '-'
        match section['stat']:
            case 1.0:
                print(f"{section['name']} {dash} Done!")
            case _:
                print(f"{section['name']} {dash} { section['stat']*100:.2f}%")

    def show_self_result(self):
        '''
        Print weekly detailed statistics.
        '''
        self._add_stats()
        final_result = 0.0
        for i, cat in enumerate(self.yml):
            stat = self.yml[cat][-1]['stat']
            final_result += stat
            print(f"{cat} [{stat:.2f}%]:")
            [self._print_task(section) for section in self.yml[cat] if len(section) > 1]
            print('\n')
        self._pass_or_fail(final_result, (i+1))

if __name__ == '__main__':
    # se = ReadYAML('self.yaml')
    # se.show_self_result()

    plan = ReadYAML('study_plan.yaml')
    plan.show_self_result()
