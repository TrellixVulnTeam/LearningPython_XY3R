# # standard 
# def function1():
#     print('this is function')

# # mapping
# def function2(x):
#     return 2*x

# a = function2(3)
# # return value or output
# print(a)

# IMI calculator

name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 25:
        return name + " not overweight"
    else:
        return name + " is overweight"

res1 = bmi_calculator(name1, height_m1, weight_kg1)
res2 = bmi_calculator(name2, height_m2, weight_kg2)
res3 = bmi_calculator(name3, height_m3, weight_kg3)

print(res1)
print(res2)
print(res3)