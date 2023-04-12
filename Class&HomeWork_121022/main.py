# 1:
# כתבו פונקציה של המחשבון. הפונקציה מקבלת מחרוזת שבה שני המספרים ובינהן אופרטור מתמטי (אחד מהארבע הבסיסיים)
# תשתמשו ב-try except למקרה והמשתמש ניסה לחלק באפס ותדפיסו לו הודעה מתאימה

def calc(string: str) -> float:
        list_of_calc = string.split()
        num1 = float(list_of_calc[0])
        num2 = float(list_of_calc[2])
        if (list_of_calc[1] == '+'):
            return num1 + num2
        elif (list_of_calc[1] == '-'):
            return num1 - num2
        elif (list_of_calc[1] == '*'):
            return num1 * num2
        elif(list_of_calc[1] == '/'):
            try:
                return num1 / num2
            except ZeroDivisionError as err:
                print("Not allowed to divide by 0")
                raise err


# 2:
# אתם חוקרי אבטחה שמקבלים לידיים שלכם מילון שממפה בין מספר לסיסמא. אתם לא יכולים להסתכל על התוכן של המילון,
# אלא רק להשתמש בפעולה של לקחת ערך על פי מפתח
# שימו לב שכאשר במילון מנסים לשים בסוגריים מרובעות ערך שלא קיים נזרקת שגיאה.
# נסו רנדומלית מספרים בין 1-1000 (לא לפי הסדר) למצוא סיסמא בתוך המילון. השתמשו ב try...except

from random import randint

def find_password(some_dict: dict) -> str:
    while True:
        rand_num = randint(1, 1001)
        try:
            password = some_dict[rand_num] # הערך שיש בתוך ה-key
            return password
        except KeyError:
            pass

# 3:
# הקוד יוצר רשימה חדשה שאיבריה הם התו החמישי בכל אחת מהמילים שיש ברשימה שמוגדרת בשורה הראשונה.
# עם זאת, הקוד מעלה שגיאות. הוסיפו בלוקים של try...except כך שהקוד ירוץ כמצופה. במידה ומילה אינה מספיק ארוכה,
# אין להוסיף את התו שלה לרשימה או להדפיס משהו בכלל. רמז: תיזכרו במילה השמורה pass ומה היא עושה.

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except BaseException:
        pass

# 4:
# תכתוב תוכנית פייתון שיוצרת קבצים בשם A.txt, B.txt וכך הלאה עד Z.
# בכל קובץ שיהיה את כל האלפ-בית באנגלית מופרדים על ידי ירידת שורה,
# לפני האותיות a i o e u תוסיפו את התו טאב (רמז: חיפשו באינטרנט איך לעשות את זה).

import string

alphabet = list(string.ascii_lowercase)
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in alphabet:
     with open(f"{char}.txt", "w") as file:
        for letter in alphabet:
            if letter in vowels:
                file.write(f"\t{letter}\n")
            else:
                file.write(f"{letter}\n")

# 5:
# תכתוב פונקציית פייתון שמקבלת שם של קובץ, היא קוראת אותו ומחזירה היסטוגרמה של המילים בקובץ.
# כלומר, מילון שממפה בין מילה לבין כמות הפעמים שהיא מופיעה.
# לאחר מכן, כתבו פונקציית main שמדפיסה את פלט פונקציית ההיסטוגרמה בעבור הקובץ alice_in_wonderland.txt (תקחו אותו מגוגל).

his_dict = dict()
def histogram(file_name: str) -> dict[str, int]:
    with open(f"{file_name}.txt") as text_file:
        for word in text_file.read().split():
            his_dict[word] = his_dict.get(word, 0) + 1 # אם ה-key לא קיים\נמצא, הפעולה get תחזיר 0(ה- value) ולאחר מכן תוסיף 1
    return his_dict

def main():
    # 1:
    print(calc("123 + 456"))

    # 2:
    print(find_password({23: 1234, 34: 456, 45: 789, 56: 969})) # כאשר הפעולה החזירה את ה-value, זאת אומרת שהמחשב הגריל את ה-key המתאים(אחד מהמפתחות שנמצאים ב-dict שקיבלנו)

    # 3:
    print(fifth)

    # 4:
    # done!

    # 5:
    print(histogram("Eitam"))

main()


