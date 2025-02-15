# Copyright 2022 Google LLC
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

from aoc2022.src.day05.python.solution import read_message_at_top
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay05Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsMessage(self):
    self.assertEqual('CMZ', read_message_at_top(self.examples[0]))

  def test_part1_withPuzzleInput_returnsMessage(self):
    self.assertEqual('LBLVVTVLP', read_message_at_top(self.input))

  def test_part2_withExampleInput_returnsMessage(self):
    self.assertEqual('MCD',
                     read_message_at_top(self.examples[0], keep_order=True))

  def test_part2_withPuzzleInput_returnsMessage(self):
    self.assertEqual('TPFFBDRJD',
                     read_message_at_top(self.input, keep_order=True))


if __name__ == '__main__':
  unittest.main()
