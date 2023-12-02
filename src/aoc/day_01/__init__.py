from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        measurements = []
        lines = self.input_lines()

        for line in lines:
            first_value = next(char for char in line if char.isdigit())
            last_value = next(char for char in reversed(line) if char.isdigit())

            measurements.append(int(first_value + last_value))

        total_calibration = sum(measurements)
        return total_calibration

    def part_2(self):
        measurements = []
        lines = self.input_lines()
        spelled_values = {
            "one": "one1one",
            "two": "two2two",
            "three": "three3three",
            "four": "four4four",
            "five": "five5five",
            "six": "six6six",
            "seven": "seven7seven",
            "eight": "eight8eight",
            "nine": "nine9nine",
        }

        for line in lines:
            for spelled_value, numeric_value in spelled_values.items():
                line = line.replace(spelled_value, numeric_value)
            first_value = next(char for char in line if char.isdigit())
            last_value = next(char for char in reversed(line) if char.isdigit())

            measurements.append(int(first_value + last_value))

        total_calibration = sum(measurements)
        return total_calibration


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
