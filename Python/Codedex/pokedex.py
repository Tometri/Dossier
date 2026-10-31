class Pokemon:
    def __init__ (self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        print(f"{self.name}, {self.name}!")
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        print(f"Caught: {self.name} has already been caught!" if self.is_caught else "Not caught yet!")
#Reptar
Reptar = Pokemon(1, "Reptar", ["Dragon", "Ground"], "A fierce dragon that can cause earthquakes with its roar.", False)
Reptar.speak()
Reptar.display_details()

#OG Howard
OG_Howard = Pokemon(2, "OG Howard", ["Musical-ahhh"], "A talented musician with a unique style.", True)
OG_Howard.speak()
OG_Howard.display_details()

#Lil Howard
Lil_Howard_Melly = Pokemon(3, "Lil Howard", ["Fairy"], "A young and energetic offshoot of OG Howard with a passion for music.", False)
Lil_Howard_Melly.speak()
Lil_Howard_Melly.display_details()
