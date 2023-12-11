from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        pipes = self.input_lines()

        def get_neighbors(x, y):
            # does not take into account types of pipes :/
            return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        def is_valid(x, y):
            return 0 <= x < len(pipes) and 0 <= y < len(pipes[0])

        distances = [[-1 for _ in range(len(pipes[0]))] for _ in range(len(pipes))]

        start_x, start_y = -1, -1
        for i in range(len(pipes)):
            for j in range(len(pipes[0])):
                if pipes[i][j] == 'S':
                    start_x, start_y = i, j
                    break

        distances[start_x][start_y] = 0

        queue = [(start_x, start_y)]
        while queue:
            current_x, current_y = queue.pop(0)
            current_distance = distances[current_x][current_y]

            # does not take into account the type of pipe :/
            for neighbor_x, neighbor_y in get_neighbors(current_x, current_y):
                if is_valid(neighbor_x, neighbor_y) and pipes[neighbor_x][neighbor_y] != '.' and distances[neighbor_x][neighbor_y] == -1:
                    distances[neighbor_x][neighbor_y] = current_distance + 1
                    queue.append((neighbor_x, neighbor_y))

        max_distance = max(max(row) for row in distances)

        return max_distance

    def part_2(self):
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
