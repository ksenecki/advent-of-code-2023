from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        calibration_values = []
        lines = self.input_lines()

        for line in lines:
            first_digit = next(char for char in line if char.isdigit())
            last_digit = next(char for char in reversed(line) if char.isdigit())

            calibration_values.append(int(first_digit + last_digit))

        total_calibration = sum(calibration_values)
        return total_calibration

    def part_2(self):
        calibration_values = []
        lines = self.input_lines()
        spelled_digits = {
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
            for spelled_digit, numeric_digit in spelled_digits.items():
                line = line.replace(spelled_digit, numeric_digit)
            first_digit = next(char for char in line if char.isdigit())
            last_digit = next(char for char in reversed(line) if char.isdigit())

            calibration_values.append(int(first_digit + last_digit))

        total_calibration = sum(calibration_values)
        return total_calibration


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
