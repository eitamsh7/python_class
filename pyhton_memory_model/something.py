def do_something(my_num: int):
    print(my_num)
    my_num = 234
    print(my_num)


num = 123
print(num)
do_something(num)
print(num)

print("---------------------------------------")

from typing import  List

def do_something2(my_nums: List[int]):
    print(my_nums)
    my_nums[0] = 4
    print(my_nums)


nums = [1, 2, 3]
print(nums)
do_something2(nums)
print(nums)