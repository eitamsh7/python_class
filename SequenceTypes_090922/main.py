#list:
#רשימה תומכת בלהביא איברים מתוכה על ידי שימוש באינדקס
# אם אנחנו רוצים לקחת איבר מסויים זה לוקח לנו הרבה עבודה
some_lst1 = [1, 2, 3]
some_lst1.append(4)
some_lst2 = [5, 6, 7]
some_lst1 += some_lst2
print(some_lst1)

#range:
some_range = range(10) # כל המספרים מ0 עד 10 לא כולל
some_range = range(5, 10) #כל המספרים מ5 ל10 לא כולל
some_range = range(1, 10, 2) # כל המספרים מ1 עד עשר לא כולל בקפיצות של 2
#כל טיפוס שניתך לרוץ על באיטרציות נקרא iterable
# An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.

#dictionary:
# מבנה נתונים זה מסוג מיליו. כל טיפוס נתונים יכול להיות כערך אך לא כל טיפוס יכול להיות מפתח
# רק טיפוס נתונים שלא יוכל להשתנות לאחר יצירה יכול להיות כמפתח
num_to_word = {1: "one", 2: "two", 3: "three", 100: "six"}
print(num_to_word[2])
num_to_word[100] = "one hundred"
print(num_to_word)


for num in num_to_word.items():
    print(num)
    print("~~~~~~~~~~~~~~~~~~~~")


#tuple:
some_tuple = (1, 2, 3)
print(some_tuple)
dict_with_tuple = {(1,2): "one, two", (2,3): "two, three"}
print(dict_with_tuple[(1,2)])

for num in some_tuple:
    print(num)

#set:
some_set = {1, 2, 3}