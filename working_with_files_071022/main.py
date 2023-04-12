Kobie_file = open("Kobie.txt", "w+") # אפשר לחפש בגוגל: python file modes
# open -> filehandle (עצם בפייתון שדרכו אפשר לגשת לקובץ)
Kobie_file.write("Yair Homo Koksinel and Ochel BataHat")
Kobie_file.seek(0,0)
# ההיסט (המיקום הראשון) ביחס לנקודה ממנה אני רוצה להתחיל (המיקום השני)
# 0- תחילת המחרוזת, 1- המקום שעליו אנחנו נמצאים עם הסמן, 2- סוף המחרוזת
# אפשר גם לחפש בגוגל: python seek method
print(Kobie_file.read())
Kobie_file.close()
