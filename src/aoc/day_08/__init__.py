from aoc.base import BaseChallenge
import re


class Challenge(BaseChallenge):
    def part_1(self):
        lines = self.input_lines()
        my_map = {}
        for i, line in enumerate(lines):
            stripped_line = line.strip()
            if i == 0:
                directions = stripped_line
            elif i != 1:
                place, left, right = re.findall(r"\w+", stripped_line)
                my_map[place] = (left, right)

        steps = 0
        starting_node = 'AAA'
        i = -1
        while starting_node != 'ZZZ':
            steps += 1
            i += 1
            if i == len(directions):
                i = 0
            direction = directions[i]
            if direction == 'L':
                starting_node = my_map[starting_node][0]
            else:
                starting_node = my_map[starting_node][1]

        return steps


    def part_2(self):
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
