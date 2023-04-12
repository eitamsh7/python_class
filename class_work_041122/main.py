# 1. תכתבו פונקציה "מיוחדת" שסופרת את מספר הפעמים שמופיעה כל אות בסטרינג
# הפונקציה פועלת ככה: בהינתן מחרוזת כלשהי, ניקח את האות הראשונה, נכניס אותה לסט, ונוציא את האות הזאת לגמרי מהמחרוזת.
# נבדוק את ההבדל בין האורך הישן לחדש של המחרוזת וככה נדע כמה פעמים האות היית הבה.
# נעשה אותו דבר לאות הראשונה והשנייה וכן הלאה עד לכל האותיות.
def countletters(some_str: str) -> dict[str, int]:
    letter_dict: dict[str, int] = dict()
    letter_set: set[str] = set()
    while len(some_str) > 0:
        start_len: int = len(some_str)
        letter: str = some_str[0]
        some_str = some_str.replace(letter, "")
        letter_set.add(letter)
        letter_dict[letter] = start_len - len(some_str)
    return letter_dict

print(countletters("helloclass"))

# 2. תכתבו פונקציה רקורסיבית שמקבלת רשימה של רשימות שמכילות מספרים.
# הפונקציה מוצאת את המספר המינימלי מבין כל הרשימות.
# הפונקציה רקורסיבית
def minimum_lists(some_list: list[list]) -> int:
    if len(some_list) <= 1:
        return min(some_list[0])
    if min(some_list[0]) > min(some_list[1]):
        del some_list[:1]
        return minimum_lists(some_list)
    else:
        del some_list[1:2]
        return minimum_lists(some_list)

list_of_lists = [[4, 5, 6, 7, 8], [5, 4, 2, 1], [8, 9, 7, 6]]
print(minimum_lists(list_of_lists))