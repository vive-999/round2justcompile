user_num = int(input("Enter your Number to get total odd numbers before : "))


def oddnumbefore(num):
    odd_num = []
    for i in range(num):
        if (i % 2)!=0:
            odd_num.append(i)
    print (f" There are {len(odd_num)} odd numbers before {user_num}")
    for nums in odd_num:
        print (nums)

result = oddnumbefore(user_num)