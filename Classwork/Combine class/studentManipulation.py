import myModule

kingsuk = myModule.student("Kingsuk Rakshit", "87878785")

kingsuk.printStudent()





### Create a petstore class where you have the details of pets available and their details.
### The class will have methods
### - Store a new pet detail
### - Search for a pet
### - Sell a pet
### - List all pets
### - import your petstore class, create a petStoreMain file, where you will implement a menu-deiven program for Admin- who will manage the store & User who will see the pets and buy pets.


class PetStore:
    def __init__(self):
        self.pets = []

    def store_pet(self, name, speciesp, price):
        pet = {"name": name, "species": species, "price": price}
        self.pets.append(pet)
        print(f"Pet {name} ({species}) has been added to the store.")

    def search_pet(self, name):
        for pet in self.pets:
            if pet["name"] == name:
                return pet
        return None

    def sell_pet(self, name):
        pet = self.search_pet(name)
        if pet:
            self.pets.remove(pet)
            print(f"Pet {name} has been sold.")
            return pet
        else:
            print(f"Pet {name} not found in the store.")
            return None

    def list_pets(self):
        if not self.pets:
            print("The store is currently empty.")
        else:
            print("Available Pets:")
            for pet in self.pets:
                print(f"Name: {pet['name']}, Species: {pet['species']}, Price: ${pet['price']}")

def main():
    pet_store = PetStore()

    while True:
        print("\nMenu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            print("\nAdmin Menu:")
            print("1. Store a new pet detail")
            print("2. List all pets")
            print("3. Back to main menu")
            admin_choice = input("Select an option: ")
            
            if admin_choice == "1":
                name = input("Enter pet name: ")
                species = input("Enter pet species: ")
                price = float(input("Enter pet price: "))
                pet_store.store_pet(name, species, price)
            elif admin_choice == "2":
                pet_store.list_pets()
            elif admin_choice == "3":
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("\nUser Menu:")
            print("1. List all pets")
            print("2. Search for a pet")
            print("3. Buy a pet")
            print("4. Back to main menu")
            user_choice = input("Select an option: ")
            
            if user_choice == "1":
                pet_store.list_pets()
            elif user_choice == "2":
                name = input("Enter the name of the pet to search for: ")
                pet = pet_store.search_pet(name)
                if pet:
                    print(f"Found: Name: {pet['name']}, Species: {pet['species']}, Price: ${pet['price']}")
                else:
                    print(f"Pet {name} not found in the store.")
            elif user_choice == "3":
                name = input("Enter the name of the pet to buy: ")
                pet = pet_store.sell_pet(name)
                if pet:
                    print(f"Congratulations! You have purchased {pet['name']} for ${pet['price']}.")
            elif user_choice == "4":
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 