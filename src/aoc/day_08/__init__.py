from aoc.base import BaseChallenge
import re


class Challenge(BaseChallenge):
    def part_1(self):
        lines = self.input_lines()
        instructions = [tuple(line.strip()) for line in lines[0].split()]

        nodes = {}
        for line in lines[2:]:
            parts = line.strip().split('=')
            node_name = parts[0].strip()
            neighbors = tuple(part.strip() for part in parts[-1].lstrip(' (').rstrip(')\n').split(','))
            nodes[node_name] = neighbors

        start_node = nodes['AAA']
        current_node = start_node
        visited_nodes = set()
        max_steps = 100

        for step in range(max_steps):
            for instruction in instructions:
                for direction in instruction:
                    if direction == 'L':
                        current_node = current_node[0]
                    elif direction == 'R':
                        current_node = current_node[1]
                    else:
                        raise ValueError("Invalid instruction: {}".format(direction))

                    if current_node in visited_nodes:
                        break
                    visited_nodes.add(current_node)

                    if current_node == 'ZZZ':
                        return step + 1

        return current_node

    def part_2(self):
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
