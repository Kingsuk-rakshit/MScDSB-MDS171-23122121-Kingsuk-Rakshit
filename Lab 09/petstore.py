class petstore():
    def _init_(slef):
        slef.pet=[]
    
    def add_pet(self,name,age, breed,price):
        pet = {
         'name' : name,
         'age': age,
         'breed':breed,
         'price':price

        }
        self.pet.append(pet)

    def search_pet(self,name):
        for pet in self.pet:
            if pet["name"]==name:
                print (pet)
            else:
                print("Pet not found")

    def list_pet(self):
        if self.pet:
            print(self.pet)
        else:
            print("There are no pets available")
        
    def remove_pet(self,name):
        for pet in self.pet:
            if pet["name"]==name:
                self.pet.remove(pet)
                print(f"{pet}the pet has been removed")
            else:
                print("dose not exist in the store")