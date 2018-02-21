# for loop
a = ["banana", "apple", "microsoft"]
# for element in a:
    # print(element)

# sum
b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
# print(total)

# range
c = list(range(1, 5))
# print(c)

total2 = 0
for i in range(1, 5):
    total2 += i
    # print(total2)

# excercise
z = list((range(1, 100)))

for i in z:
    #odd numbers in range 1 - 100
    if i % 2 != 0:
        print(i)

