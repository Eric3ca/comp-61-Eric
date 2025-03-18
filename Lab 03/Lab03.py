def display_list(list):
    if list:
        print("Current list:", list)
    else:
        print("The list is currently empty.")

def menu():
    list = []
    print("Welcome to the List Operations Program!\n") 
    while True:
        print("\nMenu:")
        print("1. Add a number to the list")
        print("2. Remove a number from the list")
        print("3. Insert a number at a specific position")
        print("4. Pop a number from the list")
        print("5. Find the sum, average, and maximum of the list")
        print("6. Search for a number in the list")
        print("7. Remove all odd numbers from the list")
        print("8. Exit")

        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            num = float(input("Enter a number to add: "))
            list.append(num)
            print("Number added.")
            
        elif choice == "2":
            num = float(input("Enter a number to remove: "))
            if num in list:
                list.remove(num)
                print("Number removed.")
            else:
                print("Number not found.")
                
        elif choice == "3":
            index = int(input("Enter position: "))
            num = float(input("Enter a number: "))
            if index >= 0 and index <= len(list):
                list.insert(index, num)
                print("Number inserted.")
            else:
                print("Invalid position.")
                
        elif choice == "4":
            index = int(input("Enter index to pop: "))
            if index >= 0 and index < len(list):
                print("Popped:", list.pop(index))
            else:
                print("Invalid index.")
                
        elif choice == "5":
            if len(list) > 0:
                sum_list = sum(list)
                avg = sum_list / len(list)
                max_list = max(list)
                print("Sum:", sum_list, "Avg:", avg, "Max:", max_list)
            else:
                print("List is empty.")
                
        elif choice == "6":
            num = float(input("Enter number to search: "))
            if num in list:
                print("Found at index", list.index(num))
            else:
                print("Number not found.")
                
        elif choice == "7":
            new_list = []
            for num in list:
                if num % 2 == 0:
                    new_list.append(num)
            list = new_list
            print("Removed all odd numbers.")
            
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        
        if input("\nWould you like to print the current list? (yes/no): ").lower() == "yes":
            display_list(list)

if __name__ == "__main__":
    menu()