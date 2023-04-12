"""
2. תכתבו פונקציה רקורסיבית שמקבלת רשימה של מספרים ומחזירה את סכום האיברים.
רמז: תחשבו על איך אפשר לעשות את צעד הרקורסיה (עוד רמז: אולי נקטין את הרשימה?)
"""
def count_elements(some_list: list ) -> int:
    if len(some_list) == 1:
        return some_list[0]
    return some_list[0] + count_elements(some_list[1:])
    #return some_list[-1] + count_elements(some_list[:-1])

lst = [1, 2, 3, 4, 5]
print(count_elements(lst))

"""
3. תכתבו פונקציה רקורסיבית שמקבלת מספר שלם ומחשבת את סכום הספרות של המספר. 
אל תמירו את המספר למחרוזת בשום שלב.
"""
def sum_digits_in_num(num: int) -> int:
    if num < 10:
        return num
    return sum_digits_in_num(num // 10) + num % 10

num = 123
print(sum_digits_in_num(num))

"""
4. תכתבו פונקציה רקורסיבית שמקבלת מחרוזת,
 ומחזירה מחרוזת שבה סדר התווים הפוך משבמחרוזת הקלט.
"""
def reverse_string(some_string: str) -> str:
    if some_string == "":
    #if len(some_string) <= 1:
        return some_string
    return  reverse_string(some_string[1:]) + some_string[0]

some_string = "Hello World"
print(reverse_string(some_string))

"""
5. תכתבו פונקציה רקורסיבית שמקבלת רשימה של מספרים ומחזירה את המקסימום ברשימה. 
חשבו רקורסיבית - האיבר המקסימלי הוא או האיבר הראשון או האיבר המקסימלי בשאר הרשימה.
"""
def max_in_list(some_list: list ) -> int:
    if len(some_list) == 1:
        return some_list[0]
    maximum = max_in_list(some_list[1:])
    if maximum > some_list[0]:
        return maximum
    else:
        return some_list[0]

lst = [1, 2, 3, 4, 3]
print(max_in_list(lst))