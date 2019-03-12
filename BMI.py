# -*- BMI-Calculator -*-
"""
https://github.com/Andyli0123/BMI-Calculator
Last edited: 2019/3/12
"""
height1=0
weight1=0
height2=0
weight2=0
null=1
lang=input("1-English    2-繁體中文\nPlease select a language (1 or 2): ")
while null!=0:
    if lang=="2" or lang=="繁體中文" or lang=="中文" or lang=="Chinese" or lang=="chinese" or lang=="zh":
        finallang=2
        height2=input("請輸入您的身高(公分): ")
        weight2=input("請輸入您的體重(公斤): ")
        if height2=="" and weight2=="":
            null=0
        else:
            if height2 and weight2 !="":
                bmi2=float(weight2)/((float(height2)/100)**2)
                print("您的BMI為: %.2f"%bmi2)
            if bmi2<18.5:
                print("您的體重太輕！\n\n(按兩次Enter離開)")
            elif bmi2>=18.5 and bmi2<24:
                print("您的體重正常！\n\n(按兩次Enter離開)")
            elif bmi2>=24 and bmi2<27:
                print("您的體重過重！\n\n(按兩次Enter離開)")
            elif bmi2>=27 and bmi2<30:
                print("您的體重輕度肥胖！\n\n(按兩次Enter離開)")
            elif bmi2>=30 and bmi2<35:
                print("您的體重中度肥胖！\n\n(按兩次Enter離開)")
            else:
                print("您的體重重度肥胖！\n\n(按兩次Enter離開)")
    else:
        finallang=1
        height1=input("Please enter your height(cm): ")
        weight1=input("Please enter your weight(kg): ")
        if height1=="" and weight1=="":
            null=0
        else:
            if height1 and weight1 !="":
                bmi1=float(weight1)/((float(height1)/100)**2)
                print("Your BMI is: %.2f"%bmi1)
            if bmi1<18.5:
                print("Your weight is too light!\n\n(Press Enter twice to leave)")
            elif bmi1>=18.5 and bmi1<24:
                print("Your weight is normal!\n\n(Press Enter twice to leave)")
            elif bmi1>=24 and bmi1<27:
                print("Your weight is overweight!\n\n(Press Enter twice to leave)")
            elif bmi1>=27 and bmi1<30:
                print("Your weight is mildly fat!\n\n(Press Enter twice to leave)")
            elif bmi1>=30 and bmi1<35:
                print("Your weight is moderately fat!\n\n(Press Enter twice to leave)")
            else:
                print("Your weight is severely obese!\n\n(Press Enter twice to leave)")
if null==0:
    if finallang==2:
        input("確定要離開 BMI Calculator 嗎？ 再按一次Enter即可離開！")
    else:
        if finallang==1:
            input("Are you sure you want to leave the BMI Calculator? Press Enter again to leave!")
