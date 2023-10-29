from petstore import PetStore

def admin_menu(pet_store):
    while True:
        print("\nAdmin Menu:")
        print("1. Store a new pet")
        print("2. List all pets")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            age = input("Enter pet age: ")
            price = input("Enter pet price: ")
            pet_store.store_new_pet(name, species, age, price)

        elif choice == "2":
            pet_store.list_all_pets()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

def user_menu(pet_store):
    while True:
        print("\nUser Menu:")
        print("1. List all pets")
        print("2. Buy a pet")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pet_store.list_all_pets()

        elif choice == "2":
            pet_name = input("Enter the name of the pet you want to buy: ")
            if pet_store.sell_pet(pet_name):
                print(f"Congratulations! You have bought {pet_name}.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    pet_store = PetStore()

    while True:
        print("\nWelcome to the PetStore:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        role_choice = input("Enter your role: ")

        if role_choice == "1":
            admin_menu(pet_store)

        elif role_choice == "2":
            user_menu(pet_store)

        elif role_choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
