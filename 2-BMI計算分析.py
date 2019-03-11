"""
【BMI計算分析】

作者: 李培綸
建立日期: 2019/2/24
最後修改: 2019/3/3
"""
height=float(input("請輸入您的身高(公分): "))
weight=float(input("請輸入您的體重(公斤): "))
bmi=weight/((height/100)**2)
del height,weight
print("您的BMI為: %.1f"%bmi)
if bmi<18.5:
    print("您的體重太輕！")
elif bmi>=18.5 and bmi<24:
    print("您的體重正常！")
elif bmi>=24 and bmi<27:
    print("您的體重過重！")
elif bmi>=27 and bmi<30:
    print("您的體重輕度肥胖！")
elif bmi>=30 and bmi<35:
    print("您的體重中度肥胖！")
else:
    print("您的體重重度肥胖！")