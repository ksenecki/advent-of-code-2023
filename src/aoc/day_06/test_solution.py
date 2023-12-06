from aoc.base import BaseTestChallenge, NotSet

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (288, NotSet)
    expected_results_from_real_data = (4811940, NotSet)
