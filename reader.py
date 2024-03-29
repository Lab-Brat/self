import sys
import yaml
from pprint import pprint


class ReadYAML:
    def __init__(self, yaml_file):
        self.file = yaml_file
        self.yml = self._read_yaml(yaml_file)
        self.stat_dict = dict()

        # file vars
        self.count = "time" if yaml_file == "self.yaml" else "details"
        self.gls = "weekly" if self.file == "self.yaml" else "monthly study"

    def _read_yaml(self, yaml_file):
        """
        Read self.yaml, return a dictionary.
        """
        with open(yaml_file, "r") as file:
            return yaml.safe_load(file)

    def _get_count(self, counts):
        """
        For each file, get file-specific countable parameters,
        i.e time parameter self, and details parameter in study_plan.
        """
        if self.file == "self.yaml":
            if isinstance(counts, int):
                return counts
            elif isinstance(counts, list):
                return len(counts)
            else:
                print("Im confused")
                sys.exit(0)
        elif self.file == "study_plan.yaml":
            return len(counts)

    def _read_seciton_stat(self, section_stat):
        """
        Read 'stat' parameter string of the section,
        parse * ^ _ @ symbols to determine the completion integer.
        """
        stat_all = 0
        for char in section_stat:
            match char:
                case "*" | "^":
                    stat_all += 1
                case "_" | "@":
                    stat_all += 0
                case _:
                    continue
        return stat_all

    def _add_stats(self):
        """
        Get statistics for the whole block, then
        get statistics for each section in the block.
        Save everyting to stat_dict,
        format: {<block/section name>: <stats>}
        """
        for block in self.yml:
            sm = 0
            for i, section in enumerate(self.yml[block]):
                section_stat = self._read_seciton_stat(
                    section["status"]
                ) / self._get_count(section[self.count])
                self.stat_dict[section["name"]] = section_stat
                sm += section_stat
            self.stat_dict[block] = (sm / (i + 1)) * 100

    def _pass_or_fail(self, result, classes):
        """
        Determine whether the weekly goals were achieved or not.
        Print out the final score, and the result message.
        """
        pass_or_fail = result / classes
        pass_bar = 80.0
        print(f"{self.gls} score: {pass_or_fail:.2f}/100")
        if pass_or_fail < pass_bar:
            print(f"{self.gls} goals: _FAILED_")
        else:
            print(f"{self.gls} goals: _COMPLETED_")
        print(f'{"-"*40}\n')

    def _print_section(self, section):
        """
        Print individual section with detailed statistics.
        """
        dash = (30 - len(section["name"])) * "-"
        stat = self.stat_dict[section["name"]]
        match stat:
            case 1.0:
                print(f"{section['name']} {dash} Done!")
            case _:
                print(f"{section['name']} {dash} { stat*100:.2f}%")

    def show_result(self):
        """
        Calculate statistics for blocks and all sections with _add_stats.
        Output detailed statistics for the document and the final result.
        """
        self._add_stats()
        final_result = 0.0

        for i, cat in enumerate(self.yml):
            stat = self.stat_dict[cat]
            final_result += stat
            print(f"{cat} [{stat:.2f}%]:")
            [
                self._print_section(section)
                for section in self.yml[cat]
                if len(section) > 1
            ]
            print("")
        self._pass_or_fail(final_result, (i + 1))


if __name__ == "__main__":
    se = ReadYAML("self.yaml")
    plan = ReadYAML("study_plan.yaml")
    try:
        if len(sys.argv) == 1:
            se.show_result()
        elif sys.argv[1] == "--study-plan":
            plan.show_result()
        elif sys.argv[1] == "--all":
            se.show_result()
            plan.show_result()
        else:
            print("I don't understand the input :(")
    except:
        pass
