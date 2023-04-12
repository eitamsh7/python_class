"""
1. כתוב פונקצייה בפייתון שמחזירה את מכפלת כל האיברים ברשימה של מספרים
"""
def mul_list(list: list) -> list:
    result = 1
    for num in range(len(list)):
        result *= num
    return result

"""
2. כתוב פונקצייה בפייתון שמקבלת רשימה של מספרים ומחזירה רשימה של אותם מספרים באותו הסדר, רק בלי חזרות
"""
def no_repeat_list(list: list) -> list:
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

"""
3. כתוב פונקצייה בפייתון שמקבלת מספר ומחזירה האם הוא ראשוני או לא
"""
def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    return False

"""
4. כתוב פונקציית פייתון שמקבלת מחרוזת ומחזירה האם המחרוזת פולינדרום או לא
"""
def is_palindrome(string_lst: str) -> bool:
    for i in range(0, len(string_lst) / 2):
        if string_lst[i] != str[len(string_lst) - i - 1]:
            return False
    return True