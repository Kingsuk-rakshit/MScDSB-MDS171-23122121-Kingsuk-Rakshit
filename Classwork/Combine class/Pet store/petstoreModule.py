# Create a petstore class where you have the details of pets available and their details.
# The class will have methods
#- Store a new pet details
#- Sell a pet
#- List all pets
# Importingg your petstore class
# Create a petstore main file where you will implement a menu driven program for admin who will manage a store user who will see pets and buy pets

class PetStore:
    def __init__(self):
        self.pets = []

    def store_new_pet(self, name, species, age, price):
        pet = {"name": name, "species": species, "age": age, "price": price}
        self.pets.append(pet)
        print(f"New pet '{name}' added to the store.")

    def sell_pet(self, pet_name):
        for pet in self.pets:
            if pet["name"] == pet_name:
                self.pets.remove(pet)
                print(f"Sold pet '{pet_name}'.")
                return True
        print(f"Pet '{pet_name}' not found in the store.")
        return False

    def list_all_pets(self):
        print("Available Pets:")
        for pet in self.pets:
            print(f"Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}, Price: {pet['price']}")

