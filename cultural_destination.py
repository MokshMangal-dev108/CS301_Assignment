class CulturalDestination:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        self.talents = []

    def add_talent(self, talent):
        self.talents.append(talent)

    def remove_talent(self, talent):
        self.talents.remove(talent)

class Talent:
    def __init__(self, name, description):
        self.name = name
        self.description = description

if __name__ == '__main__':
    name = input("Enter the name of the new cultural destination: ")
    location = input("Enter the location of the new cultural destination: ")
    description = input("Enter the description of the new cultural destination: ")

    new_cultural_destination = CulturalDestination(name, location, description)

    while True:
        print("\n1. Add talent")
        print("2. Remove talent")
        print("3. View talents")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name of the talent: ")
            description = input("Enter the description of the talent: ")
            talent = Talent(name, description)
            new_cultural_destination.add_talent(talent)
            print("Talent added successfully.")

        elif choice == 2:
            name = input("Enter the name of the talent to be removed: ")
            talents = new_cultural_destination.talents
            talent = next((t for t in talents if t.name == name), None)
            if talent:
                new_cultural_destination.remove_talent(talent)
                print("Talent removed successfully.")
            else:
                print("Talent not found.")

        elif choice == 3:
            talents = new_cultural_destination.talents
            if talents:
                print("Talents:")
                for talent in talents:
                    print(f"{talent.name} - {talent.description}")
            else:
                print("No talents added yet.")

        elif choice == 4:
            break

        else:
            print("Invalid choice. Please try again.")
