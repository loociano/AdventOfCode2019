# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from aoc2024.src.day04.python.solution import count_xmas_words, count_xmas_shapes
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_part1_withExample_counts(self):
    self.assertEqual(4, count_xmas_words(self.examples[0]))

  def test_part1_withExample2_counts(self):
    self.assertEqual(18, count_xmas_words(self.examples[1]))

  def test_part1_withPuzzleInput_counts(self):
    self.assertEqual(2603, count_xmas_words(self.input))

  def test_part2_withExample_counts(self):
    self.assertEqual(1, count_xmas_shapes(self.examples[2]))

  def test_part2_withExample2_counts(self):
    self.assertEqual(9, count_xmas_shapes(self.examples[3]))

  def test_part2_withPuzzleInput_counts(self):
    self.assertEqual(1965, count_xmas_shapes(self.input))


if __name__ == '__main__':
  unittest.main()
