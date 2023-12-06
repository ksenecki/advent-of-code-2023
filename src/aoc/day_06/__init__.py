from aoc.base import BaseChallenge


class Challenge(BaseChallenge):

    def part_1(self):
        lines = self.input_lines()
        times = list(map(int, lines[0].split(':')[1].split()))
        distances = list(map(int, lines[1].split(':')[1].split()))

        races = []

        print(len(times))

        for i in range(len(times)):
            ways = 0
            for hold_time in range(times[i]):
                speed = hold_time
                remaining_time = times[i] - hold_time
                total_distance = speed * remaining_time
                if total_distance > distances[i]:
                    ways += 1
            races.append(ways)

        result = 1
        for record in races:
            result *= record

        return result

    def part_2(self):
        lines = self.input_lines()
        times = list(map(str, lines[0].split(':')[1].split()))
        times = int("".join(times))
        distances = list(map(str, lines[1].split(':')[1].split()))
        distances = int("".join(distances))

        races = []

        ways = 0
        for hold_time in range(times):
            speed = hold_time
            remaining_time = times - hold_time
            total_distance = speed * remaining_time
            if total_distance > distances:
                ways += 1

        return ways


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
