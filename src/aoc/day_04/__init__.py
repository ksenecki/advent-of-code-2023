# mypy: ignore-errors

# ruff: noqa

from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        lines = self.input_lines()
        all_points = 0

        for line in lines:
            numbers = line.split(':')[1]
            winning_points, elf_points = numbers.split('|')
            winning_points = set(map(int, winning_points.split()))
            elf_points = list(map(int, elf_points.split()))
            points = sum(point in winning_points for point in elf_points)
            all_points += 2 ** (points - 1) if points > 0 else 0

        return all_points

    def part_2(self):
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
