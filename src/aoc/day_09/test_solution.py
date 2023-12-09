from aoc.base import BaseTestChallenge, NotSet

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (114, 2)
    expected_results_from_real_data = (1938731307, NotSet)
