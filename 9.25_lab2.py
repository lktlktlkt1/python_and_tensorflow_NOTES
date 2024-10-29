import sys
#ex1
print("hello,world!")
print("hello,'world'")

#ex2
#use#to comment on it
print("print it")
#print("not print it")

#ex3
print(2+3>=5+1) #判断
print(3+2)
print(int(100-25*3/15))
print(100-25*3/15)
print(2%5)

cars=100
space_in_a_car=4.0
drivers = 30
passengers = 90
cars_not_driven=cars-drivers
cars_driven=drivers

print("there are",cars,"cars available")

#ex6
my_age=18
my_name="LI KUNTAI"
my_eyes="black"
print(f"let's talk about my name,my name is {my_name}")
print(f"my eyes are {my_eyes} and my age is {my_age}")

types_of_people=10
x=f"there are {types_of_people} types of people"

binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}"

print(f"{x}","\n",f"{y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?{}"
print(joke_evaluation.format(hilarious))


#ex8
formatter="{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))

#ex9
print(" hello \v world")