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
from typing import Sequence
from aoc2019.src.common.nat import NAT
from aoc2019.src.common.net_intcode import NetIntcode
from aoc2019.src.common.intcode import read_intcode


def init_network(program: Sequence[int], num_computers: int, nat_address: int) -> list:
  network = []
  for address in range(num_computers):
    network.append(NetIntcode(program, address, nat_address, network))
  return network


def part_one(program: str, num_computers: int, target_address: int) -> int:
  network = init_network(read_intcode(program), num_computers, target_address)
  while True:
    for computer in network:
      packet = computer.run_until_io()
      if packet is not None and packet[0] == target_address:
        return packet[2]  # Y value


def part_two(program: str, num_computers: int, nat_address: int) -> int or None:
  network = init_network(read_intcode(program), num_computers, nat_address)
  nat = NAT(network)
  while True:
    for computer in network:
      packet = computer.run_until_io()
      if packet is not None and packet[0] == nat_address:
        nat.packet = (packet[1], packet[2])
    if nat.is_network_idle() and nat.has_packet():
      if nat.is_repeated_y():
        return nat.last_y_delivered
      else:
        nat.last_y_delivered = None
      nat.send_packet()
