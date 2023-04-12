# חלק א:

# 1. תיצרו רשימה של כל המספרים מ-1 עד 1000
list_of_nums = [num for num in range(1, 1001)]
print(list_of_nums)
# תיצרו רשימה של כל המספרים מ-1 עד 1000 שמתחלקים ב-8 (השתמשו ברשימה של 1)
new_list_divided_by_8 = [num for num in list_of_nums if num % 8 == 0]
print(new_list_divided_by_8)
# 3. תיצרו רשימה של כל המספרים מ-1 עד 1000 שיש בהם את הספרה 6 (השתמשו ברשימה של סעיף 1)
new_list_contain_6 = [num for num in list_of_nums if '6' in str(num)]
print(new_list_contain_6)
# 4. תכתבו מחרוזת כלשהי, תיצרו רשימה שיש בה את כל המילים שאורכם קטן מ-5 תווים
some_string = "Or Water Ice Call Computer Print"
some_list = [word for word in some_string.split() if len(word) < 5]
#5. תיצרו מילון שממפה בין מילה (מפתח) לבין אורכה (ערך) במחרוזת כלשהי
dict1 = {word: len(word) for word in some_string.split()}
print(dict1)


# חלק ב:

def selection_sort(arr: list) -> list:
    for i in range(len(arr)-1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        if i != cur_min_idx:
            arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i] # swap
            # another way to swap:
            """
            temp = arr[i]
            arr[i] = arr[cur_min_idx]
            arr[cur_min_idx] = temp
            """
    return arr

arr = [1, 6, 3, 9, 10, 4]
print(selection_sort(arr))

# יתרונות מיון הבחירה:
"""
1. היתרון העיקרי של מיון הבחירה הוא שהוא מתפקד היטב ברשימה קטנה.
2. מכיוון שמדובר באלגוריתם מיון במקום, אין צורך באחסון זמני נוסף מעבר למה שנדרש כדי להחזיק את הרשימה המקורית
"""

# חסרונות מיון הבחירה
"""
1. החיסרון העיקרי של מיון הבחירה הוא היעילות הירודה שלו כאשר מתמודדים עם רשימה ענקית של פריטים.
 2. מיון הבחירה דורש מספר n בריבוע של שלבים למיון n אלמנטים - מספר איטרציות מאוד גבוה - לא יעילה בזמן הריצה
3. מיון מהיר הוא הרבה יותר יעיל ממיון בחירה
"""

# תיאור מיון הבחירה - פירוט האלגוריתם
"""
1. מצא את האיבר בעל הערך הנמוך ביותר במערך
2. החלף אותו עם האיבר הראשון במערך
3. המשך באותה שיטה על שאר המערך (ללא האיבר הראשון)
"""