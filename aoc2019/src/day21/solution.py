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


def run_springscript(vm: Intcode) -> (int, str):
    ascii_image = []
    while True:
        ascii_int = vm.run_until_io_or_done()
        if ascii_int is None:
            break
        if ascii_int > 127:  # ascii table size
            return ascii_int, ''
        ascii_image.append(chr(ascii_int))
    return -1, ''.join(ascii_image)


def load_springscript(vm: Intcode, script: list):
    ascii_chars = list(map(ord, list('\n'.join(script) + '\n')))
    while len(ascii_chars) > 0:
        ascii_int = ascii_chars.pop(0)
        vm.set_input(ascii_int)
        vm.run_until_input_or_done()


def get_hull_damage(vm: Intcode, script: list) -> int:
    load_springscript(vm, script)
    damage, ascii_images = run_springscript(vm)
    if ascii_images:
        print(ascii_images)
    return damage


def part_one(program: str) -> int:
    # (!A or !B or !C) and D
    script = [
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'WALK']
    return get_hull_damage(Intcode(read_intcode(program)), script)


def part_two(program: str) -> int:
    script = [
        # (!A or !B or !C) and D and (E or H)
        # Inferred experimentally by inspecting the failed scenarios
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'NOT E T',
        'NOT T T',
        'OR H T',
        'AND T J',
        'RUN']
    return get_hull_damage(Intcode(read_intcode(program)), script)
