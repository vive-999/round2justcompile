user_num = int(input("Enter number to find next prime: "))

def nextPrime(num):
     for nextnum in range(num+1, num +200):
         for i in range(2, nextnum):
            if (nextnum % i) == 0:
               break
            else:
                return nextnum

result = nextPrime(user_num)
print ("Next Prime is : ",result)