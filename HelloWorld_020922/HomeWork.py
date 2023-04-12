# question 1:

for num in range(1220, 2701):
    if num % 7 == 0 and num % 10 == 5:
        print(num)


# question 2:

input_string: str = input("enter text: ")
LetterCount = 0
NumCount = 0
ABC = "abcdefghijklmnopqrstuvwxyz"
for char in ABC:
    LetterCount += input_string.count(char)
    LetterCount += input_string.count(char.upper())
for num in range(10):
    if str(num) in input_string:
        NumCount += 1
print(f"there are {LetterCount} letters in the string")
print(f"there are {NumCount} digits in the string")


# question 3:

lst = [0 , 1]
for i in range(8):
    lst.append(lst[i] + lst[i + 1])
print(lst)



