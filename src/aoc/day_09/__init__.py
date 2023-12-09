from aoc.base import BaseChallenge


class Challenge(BaseChallenge):

    def part_1(self):
        lines = self.input_lines()
        extrapolated_values = []
        for line in lines:
            sequences = [list(map(int, line.split()))]

            while any(sequences[-1]):
                next_sequence = [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
                sequences.append(next_sequence)

            for i in range(len(sequences) - 2, -1, -1):
                sequences[i] = [sequences[i][j] + (sequences[i + 1][j - 1] if j > 0 else 0) for j in
                                range(len(sequences[i]))]

            extrapolated_values.append(sequences[0][-1])

        return sum(extrapolated_values)

    def part_2(self):
        lines = self.input_lines()
        extrapolated_values = []
        for line in lines:
            sequences = [list(map(int, line.split()))]

            while any(sequences[0]):
                prev_sequence = [sequences[0][i] - sequences[0][i - 1] for i in range(1, len(sequences[0]))]
                sequences.insert(0, prev_sequence)

            for i in range(1, len(sequences)):
                sequences[i] = [sequences[i][j] + (sequences[i][j - 1] if j > 0 else 0) for j in
                                range(len(sequences[i]))]

            extrapolated_values.append(sequences[-1][-1])
        # does not work :(
        return sum(extrapolated_values)


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
