def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
res = apply_to_list(ints, lambda x: x * 2)
print(res)

# 커링 - 일부 인자만 취하기
def add_numbers(x, y):
    return x+y

add_five = lambda y: add_numbers(5, y)
from functools import partial
add_five = partial(add_numbers, 5)
