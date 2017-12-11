from unittest import TestCase

from .puzzle import new_coordinates, count_movements


class TestNew_coordinates(TestCase):

   def test_movement_n(self):
      assert new_coordinates(0, 0, 'n') == (0, -1)

   def test_movement_ne(self):
      assert new_coordinates(0, 0, 'ne') == (1, -1)

   def test_movement_se(self):
      assert new_coordinates(0, 0, 'se') == (1, 0)

   def test_movement_s(self):
      assert new_coordinates(0, 0, 's') == (0, 1)

   def test_movement_sw(self):
      assert new_coordinates(0, 0, 'sw') == (-1, 1)

   def test_movement_w(self):
      assert new_coordinates(0, 0, 'nw') == (-1, 0)

   def test_count_steps_away_ne_ne_ne(self):
       movements = ['ne', 'ne', 'ne', ]
       away = count_movements(movements)
       assert away == 3

   def test_count_steps_away_ne_ne_sw_sw(self):
      movements = ['ne', 'ne', 'sw', 'sw', ]
      away = count_movements(movements)
      assert away == 0

   def test_count_steps_away_ne_ne_s_s(self):
      movements = ['ne', 'ne', 's', 's']
      away = count_movements(movements)
      assert away == 2

   def test_count_tests_away_se_sw_se_sw_sw(self):
      movements = ['se', 'sw', 'se', 'sw', 'sw']
      away = count_movements(movements)
      assert away == 3

