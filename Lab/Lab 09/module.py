import petstore
pt=petstore.petstore()

while(True):
    print("\nOptions:")
    print("1. Add Pet")
    print("2. List pet") 
    print("3. Search pet")
    print("4. Sell pet")
    print("5. Quit")

    choice=input("Enter your choice")
    if choice=="1":
        name= input ("enter the pet name")
        age=input ("enter the age of the pet")
        breed=input ("enter the breed of the pet")
        price =input("enter the price of the pet")
        pt.add_pet(name,age,breed,price)
        print("Details has been entred")
    elif choice=="2":
        pt.list_pet()
        print(pt)
    elif choice=="3":
        name=input("enter the name to be search")
        pt.search_pet(name)
    elif choice=="4":
        name=input("enter the name to be search")
        pt.remove_pet(name)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")