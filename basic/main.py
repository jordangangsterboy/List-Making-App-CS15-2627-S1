the_list = [] 
 
while True: 
    user_input = input( 
        "Choose an option, from 1, 2, 3, 4, and 5.\n 1: add an item.\n 2: remove an item.\n 3: display the list.\n 4: undo the previous change.\n 5: exit.\n") 
    if user_input == "1": 
        previous_list = the_list.copy() 
        item = input("What item would you like to add? ") 
        the_list.append(item) 
    elif user_input == "2": 
        previous_list = the_list.copy() 
        index = int(input("Enter the index of the item to remove: ")) 
        the_list.pop(index) 
    elif user_input == "3": 
        for index, item in enumerate(the_list): 
            print(index, item) 
    elif user_input == "4": 
        the_list = previous_list.copy() 
    elif user_input == "5": 
        break 
