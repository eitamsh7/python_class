from random import randint
from typing import  List

def div_of_num(num: int) -> List[int]: # דרך א:
    new_list = []
    for i in range(1, num):
        if num % i == 0:
            new_list.append(i)
    return new_list

def div_of_num2(num: int) -> List[int]: # דרך ב:
    return (i for i in range(2, num // 2 + 1) if num % i == 0)

def main():
    num_list = [randint(1, 50) for _ in range(0, 10)]
    for i in num_list:
        print(f"The divisors for num {i} are: \n{div_of_num(i)}")


