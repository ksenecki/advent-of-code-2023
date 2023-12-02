# mypy: ignore-errors

from collections import Counter

from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        lines = self.input_lines()
        cube_counts = {"red": 12, "green": 13, "blue": 14}

        not_possible_game_ids = []
        possible_game_ids = []

        for line in lines:
            game_id, cubes_info = line.split(":")
            game_id = int(game_id.split()[1])
            game = cubes_info.split(";")
            counts = {"red": 0, "green": 0, "blue": 0}
            for cubes in game:
                for cube in cubes.split(","):
                    count, cube_color = cube.split()
                    count = int(count)
                    counts[cube_color] = max(counts[cube_color], count)

                    if int(count) <= cube_counts.get(cube_color):
                        possible_game_ids.append(game_id)
                    else:
                        not_possible_game_ids.append(game_id)

        not_possible_game_ids = Counter(not_possible_game_ids)
        possible_game_ids = Counter(possible_game_ids)
        possible_game_ids = [
            x for x in possible_game_ids if x not in not_possible_game_ids
        ]

        return sum(possible_game_ids)

    def part_2(self):
        lines = self.input_lines()
        water = 0

        for line in lines:
            game_id, cubes_info = line.split(":")

            game = cubes_info.split(";")
            counts = {"red": 0, "green": 0, "blue": 0}
            for cubes in game:
                for cube in cubes.split(","):
                    count, cube_color = cube.split()
                    count = int(count)
                    counts[cube_color] = max(counts[cube_color], count)
            cubes_square = 1
            for c in counts.values():
                cubes_square *= c
            water += cubes_square
        return water


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
