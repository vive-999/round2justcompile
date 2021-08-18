products = {}

print("Enter a new Choice")


def showoptions():
    choice = int(input(
                   "1 Add Product \n"
                   "2 Remove Product\n"
                   "3 Update Product\n"
                   "4 View Product\n"
                   "5 Exit \n"
                   "Your choice -"))
    return choice

def addproduct():
    product = str(input("Enter Product Name: "))
    price =  input("Enter Product Price: ")
    print('Thanks for adding product. Now enter the new choice.')
    products[product] = price

def removeproduct():
    product = input("Enter Product Name: ")
    if product in products:
        products.pop(product)
        print('You successfully removed a product. Now enter the new choice.')
    else:
        print("Product does not exists.")
        removeproduct()

def updateproduct():
    product = input("Enter Product Name: ")
    if product  in products:
        price = input("Enter new price: ")
        products[product] = price
        print('You successfully updated a product. Now enter the new choice.')
    else:
        print("Product does not exists.")
        updateproduct()

def viewproduct():
    for key,value in products.items():
        print (f"{key}\t\t\t\t\tRs.{value}")



#Looping starts here
while True:
    choice = showoptions()
    if choice ==1:
        print("Your choice: Add Product")
        addproduct()
        print("---"*18)
    elif choice ==2:
        print("Your choice: Remove Product")
        removeproduct()
        print("~~~" * 18)
    elif choice ==3:
        print("Your choice: Update Product")
        updateproduct()
        print("~~~" * 18)
    elif choice==4:
        print("Your choice: View Product")
        print("Your Product in Stock")
        print("~~~" * 18)
        print("Product Name \t\t\tProduct Price")
        print ("---" *18)
        viewproduct()
        print("~~~" * 18)
    elif choice==5:
        user = str(input("Do you want to exit?(yes/No)\n")).lower()
        if user =="yes" or user =='y':
            print("~~~" * 18)
            break
        if user =="no" or user =="n":
            print("~~~" * 18)
            continue
    else:
        print("Please choose from the given options")
        print("~~~" * 18)

print("Thankyou! Have a nice day.")

