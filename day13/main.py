from common.intcode import Intcode


def read_program(file) -> list:
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def get_num_blocks(program: list) -> int:
    block_tile_count = 0
    vm = Intcode(program)
    while True:
        x = vm.run()
        if x is None:
            break
        vm.run()  # ignore y value
        tile_id = vm.run()
        block_tile_count += 1 if tile_id == 2 else 0
    return block_tile_count


def part_one(filename: str) -> int:
    return get_num_blocks(read_program(filename))


def move_joystick(vm: Intcode, paddle_x: int, ball_x: int):
    vm.set_input(-1 if paddle_x > ball_x else 1 if paddle_x < ball_x else 0)


def beat_game(vm: Intcode) -> int:
    score = 0
    paddle_x = 0
    while True:
        x = vm.run()
        if x is None:
            break
        y = vm.run()
        data = vm.run()
        if x == -1 and y == 0:
            score = data
        else:
            if data == 3:  # paddle
                paddle_x = x
            if data == 4:  # ball
                move_joystick(vm, paddle_x, x)
    return score


def part_two(filename: str) -> int:
    program = read_program(filename)
    program[0] = 2  # play game
    return beat_game(Intcode(program))


print(part_one('input'))  # 298
print(part_two('input'))  # 13956
