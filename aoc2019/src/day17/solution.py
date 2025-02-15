# Copyright 2019 Google LLC
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
from aoc2019.src.common.intcode import Intcode, read_intcode


def is_intersection(grid: dict, x: int, y: int, width: int, height: int) -> bool:
  if x == 0 or y == 0 or x == width - 1 or y == height - 1:
    return False
  return grid[(x - 1, y)] == ord('#') and grid[(x + 1, y)] == ord('#') \
    and grid[(x, y - 1)] == ord('#') and grid[(x, y + 1)] == ord('#')


def is_grid_char(num: int) -> bool:
  chars = set('#.^v<>')
  return str(chr(num)) in chars or num == 10  # newline


def get_grid(vm: Intcode) -> (dict, int, int):
  grid = {}
  x, y, width, height = 0, 0, 0, 0
  output = vm.run()
  while output is not None:
    if not is_grid_char(output):
      break
    if output == 10:  # newline
      y += 1
      width = max(width, x)
      x = 0
    else:
      grid[(x, y)] = output
      x += 1
    output = vm.run()
  height = y - 1  # input.txt.txt ends with newline
  return grid, width, height


def get_alignment_param_sum(grid: dict, width: int, height: int) -> int:
  alignment_param_sum = 0
  for y in range(0, height):
    for x in range(0, width):
      if grid[(x, y)] == 35 and is_intersection(grid, x, y, width, height):
        alignment_param_sum += x * y
  return alignment_param_sum


def part_one(program: str) -> int:
  vm = Intcode(read_intcode(program))
  grid, width, height = get_grid(vm)
  return get_alignment_param_sum(grid, width, height)


def string_to_ascii_list(string: str) -> list:
  return list(map(ord, list(string)))


def get_collected_dust(vm: Intcode) -> int:
  # This is obtained from inspecting the robot path (grid)
  input_routine = string_to_ascii_list('A,B,A,B,C,B,A,C,B,C\n'
                                       'L,12,L,8,R,10,R,10\n'
                                       'L,6,L,4,L,12\n'
                                       'R,10,L,8,L,4,R,10\n'
                                       'n\n')
  while True:
    if len(input_routine) > 0:
      vm.set_input(input_routine.pop(0))
    output = vm.run_until_input_or_done()
    if output is None:
      collected_dust = vm.get_output()
      break
  return collected_dust


def part_two(program: str) -> int:
  program = list(read_intcode(program))
  program[0] = 2
  vm = Intcode(program=tuple(program))
  return get_collected_dust(vm)
