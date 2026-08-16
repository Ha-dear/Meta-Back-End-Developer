num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]


# instruction_1 :
for num in num_list:
    print(num)

# instruction_2/3 :
for num in num_list:
    if num > 45 :
        print(f"this number {num} is over 45")
    else :
        print(f"this number {num} is under 45")

# instruction_4/5/6/7/8 :
counter = 0
for idx , num in enumerate(num_list):
    counter += 1
    if num == 36 :
        print(f"the number 36 is found at postion {idx}")
        break
print(f"the numbber of the iterations of the loop is:: {counter}")

