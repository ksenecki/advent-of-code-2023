# mypy: ignore-errors

# ruff: noqa

from collections import defaultdict

from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        lines = self.input_lines()
        parts_sum = 0
        index = 0
        positions = [-1, 0, 1]
        for line in lines:
            index2 = 0
            item = line.strip()
            part_number = ""
            valid_part = False
            for part_digit in item:
                if part_digit.isdigit():
                    part_number = part_number + part_digit
                    for i in positions:
                        for j in positions:
                            if (index + i) < len(lines) and (index2 + j) < len(
                                lines[0]
                            ):
                                part_digit2 = lines[index + i][index2 + j]
                                if part_digit2 != "." and not part_digit2.isdigit():
                                    valid_part = True
                            else:
                                continue
                if not part_digit.isdigit() or index2 == len(item) - 1:
                    if valid_part:
                        parts_sum += int(part_number)
                        valid_part = False
                    part_number = ""
                index2 += 1
            index += 1
        return parts_sum

    def part_2(self):
        lines = self.input_lines()
        parts_sum = 0
        gear_ratio = 0
        part_gear = False
        gears = defaultdict(list)
        index = 0
        positions = [-1, 0, 1]
        for line in lines:
            index2 = 0
            item = line.strip()
            part_number = ""
            valid_part = False
            for part_digit in item:
                if part_digit.isdigit():
                    part_number = part_number + part_digit
                    for i in positions:
                        for j in positions:
                            if (index + i) < len(lines) and (index2 + j) < len(
                                lines[0]
                            ):
                                part_digit2 = lines[index + i][index2 + j]
                                if part_digit2 != "." and not part_digit2.isdigit():
                                    valid_part = True
                                    if part_digit2 == "*":
                                        part_gear = (index + i, index2 + j)
                            else:
                                continue
                if not part_digit.isdigit() or index2 == len(item) - 1:
                    if valid_part:
                        parts_sum += int(part_number)
                        valid_part = False
                    if part_gear:
                        gears[part_gear].append(part_number)
                        if len(gears[part_gear]) == 2:
                            gear_ratio += int(part_number) * int(gears[part_gear][0])
                        part_gear = False
                    part_number = ""
                index2 += 1
            index += 1
        return gear_ratio


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
