from unittest import TestCase
from .puzzle import Puzzle


class TestPuzzle(TestCase):

    # groups function tests

    def test_single_plain_group(self):
        input = '{}'
        result = Puzzle().groups(input)
        assert result == 1

    def test_three_nested_groups(self):
        input = '{{{}}}'
        result = Puzzle().groups(input)
        assert result == 3

    def test_three_groups_with_commas(self):
        input = '{{},{}}'
        assert Puzzle().groups(input) == 3

    def test_six_groups_nested_with_commas(self):
        input = '{{{},{},{{}}}}'
        assert Puzzle().groups(input) == 6

    def test_one_group_with_garbage(self):
        input_stream = '{<{},{},{{}}>}'
        input_stream = Puzzle().clear_input(input_stream)
        assert Puzzle().groups(input_stream) == 1

    def test_one_group_with_many_garbage(self):
        input_stream = '{<a>,<a>,<a>,<a>}'
        input_stream = Puzzle().clear_input(input_stream)
        assert Puzzle().groups(input_stream) == 1

    def test_five_groups_with_garbage(self):
        input_stream = '{{<a>},{<a>},{<a>},{<a>}}'
        input_stream = Puzzle().clear_input(input_stream)
        assert Puzzle().groups(input_stream) == 5

    def test_two_groups_with_ignored_garbages(self):
        stream = '{{<!>},{<!>},{<!>},{<a>}}'
        stream = Puzzle().clear_input(stream)
        assert Puzzle().groups(stream) == 2

    # score function tests

    def test_score_of_single_group(self):
        input_stream = '{}'
        puzzle = Puzzle()
        input_stream = Puzzle.clear_input(input_stream)
        score = puzzle.score(input_stream)
        assert score == 1

    def test_score_of_three_nested_groups(self):
        input_stream = '{{{}}}'
        puzzle = Puzzle()
        input_stream = Puzzle.clear_input(input_stream)
        score = puzzle.score(input_stream)
        assert score == 6

    def test_three_groups_with_commas(self):
        input_stream = '{{},{}}'
        puzzle = Puzzle()
        cleared_stream = Puzzle.clear_input(input_stream)
        score = puzzle.score(cleared_stream)
        assert score == 5

    def test_empty_garbages(self):
        input_stream = '{<a>,<a>,<a>,<a>}'
        puzzle = Puzzle()
        cleared_stream = puzzle.clear_input(input_stream)
        score = puzzle.score(cleared_stream)
        assert score == 1

    def test_score_groups_with_garbage_letters(self):
        input_stream = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
        puzzle = Puzzle()
        cleared_stream = puzzle.clear_input(input_stream)
        score = puzzle.score(cleared_stream)
        assert score == 9

    def test_score_groups_with_ignored_garbages(self):
        input_stream = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
        puzzle = Puzzle()
        cleared_stream = puzzle.clear_input(input_stream)
        score = puzzle.score(cleared_stream)
        assert score == 9

    def test_score_groups_with_letters_ignored_and_garbages(self):
        input_stream = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
        puzzle = Puzzle()
        cleared_stream = puzzle.clear_input(input_stream)
        score = puzzle.score(cleared_stream)
        assert score == 3
