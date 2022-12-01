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
from typing import Sequence


def find_max_calories(calories_list: Sequence[str]) -> int:
    """AoC 2022 Day 1 Part 1.

    Args:
      calories_list: A list of calories carried by each elf,
      separated by blank lines.
    Returns:
      Max calories carried by one elf.
    """
    calories_sums = []
    elf_counter = 0
    for calories in calories_list:
        if calories == '':
            elf_counter += 1  # Next elf.
        else:
            if elf_counter == len(calories_sums):
                calories_sums.append(0)
            calories_sums[elf_counter] += int(calories)
    return max(calories_sums)
