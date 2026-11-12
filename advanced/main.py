to_do_list = [] 
completed_list = [] 
previous_list = [] 
 
while True: 
    user_input = input( 
        "Choose an option, from 1, 2, 3, 4, 5, 6, and 7.\n 1: add a to-do item.\n 2: remove a to-do item.\n 3: replace a to-do item.\n 4: check off an item.\n 5: view lists.\n 6: undo.\n 7: exit.\n") 
    if user_input == "1": 
        previous_list = to_do_list.copy() 
        item = input("What to-do item would you like to add? ") 
        to_do_list.append(item) 
    elif user_input == "2": 
        previous_list = to_do_list.copy() # saves backup of current state 
        index = int(input("Enter the index of the to-do item to remove: ")) 
        to_do_list.pop(index) 
    elif user_input == "3": 
        previous_list = to_do_list.copy() 
        index = int(input("Enter the index of the item you want to replace: ")) 
        new_item = input("What should the new item be? ") 
        to_do_list[index] = new_item 
    elif user_input == "4": 
        previous_list = to_do_list.copy() 
        index = int(input("Enter the index of the item you completed: ")) 
        completed_item = to_do_list.pop(index) 
        completed_list.append(completed_item) # removes from to-do list and stores as completed item 
    elif user_input == "5": 
        choice = input("Do you want to view (1) To-Do list or (2) Completed list? ") 
        if choice == "1": 
            print("--- To-Do List ---") 
            for index, item in enumerate(to_do_list): 
                print(index, item) 
        elif choice == "2": 
            print("--- Completed List ---") 
            for index, item in enumerate(completed_list): 
                print(index, item) 
    elif user_input == "6": 
        to_do_list = previous_list.copy() 
    elif user_input == "7": 
        break 
