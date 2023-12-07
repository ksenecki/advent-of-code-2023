from aoc.base import BaseChallenge


class Challenge(BaseChallenge):

    def part_1(self):
        lines = self.input_lines()
        hands = []
        bids = []
        powers = []
        for line in lines:
            hand, bid = line.split(' ')
            hands.append(hand)
            bids.append(bid)

        all_hands = list(zip(hands, bids))

        card_order = "AKQJT98765432"

        for hand in all_hands:
            cards_set = set(hand[0])
            card_counts = dict()
            for cards in cards_set:
                count_char = 0
                for card in hand[0]:
                    if card == cards:
                        count_char += 1
                card_counts[cards] = count_char

                # sorted_cards = sorted(hand[0], key=lambda x: card_order.index(x), reverse=True)
                # print(sorted_cards)

            if len(set(card_counts.values())) == 1 and 5 in card_counts.values():
                hand_power = 8
            elif 4 in card_counts.values():
                hand_power = 7
            elif sorted(card_counts.values()) == [2, 3]:
                hand_power = 6
            elif 3 in card_counts.values():
                hand_power = 5
            elif sorted(card_counts.values()) == [1, 2, 2]:
                hand_power = 4
            elif sorted(card_counts.values()) == [1, 1, 1, 2]:
                hand_power = 3
            else:
                hand_power = 2

            powers.append(hand_power)

        hands_with_powers = list(zip(hands, bids, powers))
        hands_with_powers.sort(key=lambda a: a[2], reverse=True)

        # i = 0
        # j = 0
        # for hand in hands_with_powers:
        #     if 0 < i < len(hands_with_powers):
        #         if hand[2] == hands_with_powers[i-1][2]:
        #             for card in hand[0]:
        #                 if card > hands_with_powers[i-1][0][j]:

        i = 1
        total_value = 0
        for hand in hands_with_powers:
            total_value = int(total_value) + i * int(hand[1])

        return total_value

    def part_2(self):
        lines = self.input_lines()
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
