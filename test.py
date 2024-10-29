print("please type your height and weight here,we will calculate the BMI for you!")

print("please type your weight(kg) here")
weight = float(input(">"))

print("please type your height(meter) here")
height = float(input(">"))

BMI = weight/(height*height)

print("Your BMI is","%.2f" %BMI)

BMI_float2 = "%.2f" %BMI
print(f"Your BMI is {BMI_float2}")
#注意保留两位小数的写法，line11，14

print("Your BMI is",format(BMI,".2f"))
print("YOur BMI is",round(BMI,2))