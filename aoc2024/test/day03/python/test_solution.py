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

from aoc2024.src.day03.python.solution import calculate
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay03Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestDay03Solution, self)
     .__init__(__file__, read_raw=True, *args, **kwargs))

  def test_part1_withExample_calculates(self):
    self.assertEqual(161, calculate(self.examples[0]))

  def test_part1_withPuzzleInput_calculates(self):
    self.assertEqual(170807108, calculate(self.input))


if __name__ == '__main__':
  unittest.main()
