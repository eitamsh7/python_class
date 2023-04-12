# שאלה 1
"""
1. כתוב תוכנית פייתון שמקבלת מחרוזת מהקלט ומדפיסה מילון שממפה בין אות בקלט לבין כמה פעמים היא מופיעה במחרוזת למשל, עבור Hello World נקבל
{"h": 1, "e": 1, "l": 3, "o": 2 ," ": 1, "W": 1, "r": 1, "d": 1}
"""
"""
input_text = input("enter text:")
char_apear = {}
for char in input_text:
    char_apear[char] = input_text.count(char)
print(char_apear)
"""
# שאלה 2
"""
2. כתוב תוכנית פייתון שמוגדרות בה שתי רשימות והיא מדפיסה TRUE אם בשתי הרשימות יש איבר משותף אחד לפחות אחרת היא תדפיס FALSE השתמש ב-Set.
"""

#lst1 = [1, 2, 3, 4, 5]
#lst2 = [1, 8, 3, 6, 7]
lst1 = []
n = int(input("Enter number of elements for list 1: "))
for i in range(0, n):
    element = int(input("Enter an Element: "))
    lst1.append(element)
print("")

lst2 = []
n2 = int(input("Enter number of elements for list 2: "))
for i in range(0, n2):
    element2 = int(input("Enter an Element: "))
    lst2.append(element)
count = 0
for charlst1 in lst1:
    for charlst2 in lst2:
        if charlst1 == charlst2:
            count += 1
if count >= 1:
    print('\n' 'True')
else:
    print('\n' 'False')

