from random import randint
from typing import Iterable

def linear_search(iter: Iterable, search_item) -> int:
    for index, item in enumerate(iter):
        if item == search_item:
            return index
    return -1

def search_rand_num(iter: Iterable[int]):
    tries = 0
    while True:
        rand_num = randint(1, 100)
        if linear_search(iter, rand_num) != -1:
            print(f"Found number {rand_num} after {tries} tries")
            break
        tries += 1

def binary_search(search_list: list, search_item) -> int:
    left = 0
    right = len(search_list) - 1
    middle = (right + left) // 2
    while left < right:
        middle = (right + left) // 2
        if search_list[middle] > search_item:
            right = middle + 1
        elif search_list[middle] < search_item:
            left = middle - 1
        else:
            return middle
    return -1


num_list = sorted([randint(1, 100) for _ in range(randint(10, 20))])
print(num_list)
search_num = 90

print(linear_search(num_list, 90))
search_rand_num(num_list)


num_list2 = [0,2,3,4,6,77,88,90]
print(binary_search(num_list2, 4))