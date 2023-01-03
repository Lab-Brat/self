import sys
import yaml
from pprint import pprint

class ReadYAML:
    def __init__(self, yaml_file):
        self.file = yaml_file
        self.yml  = self._read_yaml(yaml_file)
        self.stat_dict = dict()

        # file vars
        self.count = 'time' if yaml_file == 'self.yaml' else 'details'
        self.gls = 'weekly' if self.file == 'self.yaml' else 'monthly study'

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
            section_counts = self._get_count(section[self.count])
            sm += len(section['status']) / section_counts
        return ((sm/(i+1))*100)

    def _add_stats(self):
        '''
        Get information about every section.
        '''
        for block in self.yml:
            self.stat_dict[block] = self._get_full_stat(block)
            for section in self.yml[block]:
                count = self._get_count(section[self.count])
                self.stat_dict[section['name']] = len(section['status'])/count

    def _pass_or_fail(self, result, classes):
        '''
        Determina wether the weekly goals were achieved or not.
        '''
        pass_or_fail = result/classes
        pass_bar = 80.0
        print(f'{self.gls} score: {pass_or_fail:.2f}/100')
        if pass_or_fail < pass_bar:
            print(f'{self.gls} goals: _FAILED_')
        else:
            print(f'{self.gls} goals: _COMPLETED_')
        print(f'{"-"*40}\n')

    def _print_section(self, section):
        '''
        Print section statistics.
        '''
        dash = (30 - len(section['name'])) * '-'
        stat = self.stat_dict[section['name']]
        match stat:
            case 1.0:
                print(f"{section['name']} {dash} Done!")
            case _:
                print(f"{section['name']} {dash} { stat*100:.2f}%")

    def show_result(self):
        '''
        Print weekly detailed statistics.
        '''
        self._add_stats()
        final_result = 0.0

        for i, cat in enumerate(self.yml):
            stat = self.stat_dict[cat]
            final_result += stat
            print(f"{cat} [{stat:.2f}%]:")
            [self._print_section(section) for section in self.yml[cat] if len(section) > 1]
            print('')
        self._pass_or_fail(final_result, (i+1))


if __name__ == '__main__':
    se = ReadYAML('self.yaml')
    se.show_result()

    plan = ReadYAML('study_plan.yaml')
    plan.show_result()
