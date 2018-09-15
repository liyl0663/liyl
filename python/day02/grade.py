#!/usr/bin/env python3
# -*- coding: utf-8 -*-
grade = int(input("请输入你的成绩："))

if grade >= 60 and grade <70:
    print("及格")
#elif grade >= 70 and grade < 80:
elif 70 <= grade <80:
    print("良")
#elif grade >= 80 and grade < 90:
elif 80 <= grade <90:
    print("好")
elif grade >= 90:
    print("优秀")
else:
    print("你要努力了")
########################################################################
score = int(input('分数：'))
if score >= 90:
    print("优")
elif score >=80:
    print("良")
elif score >=70:
    print("良")
elif score >=60:
    print("及格")
else:
    print("再接再厉")