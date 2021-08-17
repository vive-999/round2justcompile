count = int(input("Enter how many odd number squares sequence you want: "))

def oddsquares(num):
    i = 0
    odd_num =1
    while i< count:
        print(odd_num**2)
        i+=1
        odd_num+=2

result = oddsquares(count)