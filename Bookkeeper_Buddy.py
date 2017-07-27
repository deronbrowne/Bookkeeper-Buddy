state='on'
execfile('Inventory_Class.py')
execfile('My_Projects_Class.py')

print 'Welcome to "Bookkeeper Buddy"!'

while state=='on': 
    
    action=raw_input('Choose one of the following options:\n'
    '"Inventory"\n'
    '"Projects"\n'
    '"Restock"\n'
    '"Set Goal"\n'
    '"Quit"\n'
    '\n')

    if action=='Inventory':
        
        query=raw_input('What would you like to do?\n'
        '"Create" an inventory\n'
        '"Edit" the inventory\n'
        '"Add" an item\n'
        '"View inventory"\n'
        '"View item"\n'
        '"Delete" an inventory item\n'
        '"Done"?\n'
        '\n')
                      
        if query=='Create':
            Save = 'keep adding'
            while Save=='keep adding':
                    a=inventory()
                    inventory.add_item(a)
                    Save=raw_input('Would you like to save your inventory or keep adding? Save/keep adding\n'
                                  '\n')
            del a
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"Add" an item\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')
        
        elif query=='Edit':
            Save = 'Keep editing'
            while Save=='Keep editing':
                inventory.edit_item()
                Save=raw_input('Would you like to:\n'
                '"Save"\n'
                'or"Keep editing"\n')
            if Save=='Save':
                query=raw_input('What would you like to do?\n'
                '"Create" an inventory\n'
                '"Edit" the inventory\n'
                '"View inventory list"\n'
                '"View item info"\n'
                '"Delete" an inventory item\n'
                '"Done"?\n'
                '\n')
            else:
                Save=raw_input('Try again.\n'
                'Would you like to:\n'
                '"Save"\n'
                'or"Keep editing"\n')
                        
        elif query=='Add':
            Save = 'keep adding'
            while Save=='keep adding':
                    a=inventory()
                    inventory.add_item(a)
                    Save=raw_input('Would you like to save your entries or keep adding? Save/keep adding ')
            del a
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"Add" an item\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')
            
        elif query=='View inventory':
            x=len(inventory.name)-1
            for i in range(1,x):
              print inventory.name[x], inventory.item_count[x], inventory.item_cost[x], inventory.subtotals[x]
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"Add" an item\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')
                 
        elif query=='View item':
            print inventory.name
            State='view another'
            while State=='view another':
                x=inventory.name.index(raw_input('Which item would you like to view? '))
                a=inventory()
                inventory.view_item(a,x)
                State=raw_input('Would you like to "return" to the main menu or "view another"? ')
            del a
            del x
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')
                
        elif query=='Delete':
            print inventory.name
            State='delete another'
            while State=='delete another':
                x=inventory.name.index(raw_input('What would you like to delete?'))
                a=inventory()
                inventory.delete_item(a,x)
                State=raw_input('Would you like to "save" your changes or "delete another"? ')
            del a
            del x
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')  
        
        elif query=='Done':
            action=raw_input('Choose one of the following options:\n'
            '"Inventory"\n'
            '"Projects"\n'
            '"Restock"\n'
            '"Set Goal"\n'
            '\n')
            
        else:
            print "Sorry I didnt get that. Try again."
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Quit"?\n'
            '\n')     
    
        
    elif action=='Projects':
        query=raw_input('What would you like to do?\n'
        '"Create" a project\n'
        '"Add" to a project\n'
        '"Edit" a project\n'
        '"View" a project\n'
        '"Delete" a project\n'
        '"Exit without saving"\n'
        '"Save and Exit"\n'
        '\n')
        
        if query=='Create':
            projects.append(raw_input('Name your project! '))
            instances.append(my_projects())
            a=my_projects()
            my_projects.add_item(a)
            query=raw_input('What would you like to do?\n'
            '"Create" a project\n'
            '"Add" to a project\n'
            '"Edit" a project\n'
            '"View" a project\n'
            '"Delete" a project\n'
            '"Exit without saving"\n'
            '"Save and Exit"\n'
            '\n')
            
        while query=='Edit':
            sub_query=raw_input('Would you like to:\n'
            '"Add item"?\n'
            '"Add to overheads"?\n'
            '"Log hours"?\n'
            '"Set profit"?\n'
            '"Quit"\n'
            '\n')
            
            if sub_query== 'Add':
               print 'Add' 
            elif sub_query== 'Add to overheads':
               print 'Add' 
            elif sub_query== 'Log hours':
               print 'Add' 
            elif sub_query== 'Set profit':
               print 'Add' 
            elif sub_query== 'Quit':
                query=raw_input('What would you like to do?\n'
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'
                '"Delete" a project\n'
                '"Save and Exit"\n'
                '\n')
                
            else:
                print "Sorry I didnt get that. Try again."
                sub_query=raw_input('Would you like to:\n'
                '"Add item"?\n'
                '"Add to overheads"?\n'
                '"Log hours"?\n'
                '"Set profit"?\n'
                '\n')
            
        while query=='View':
            sub_query=raw_input('Would you like to:\n'
            '"View item"?\n'
            '"View overheads"?\n'
            '"View hours"?\n'
            '"View profit"?\n'
            'View the "Project total"?\n'
            '"Quit"\n'
            '\n')
            
            if sub_query== 'View item':
                print 'Add'
                
            elif sub_query== 'View overheads':
                print 'Add'
                
            elif sub_query== 'View hours':
                print 'Add'
                
            elif sub_query== 'View profit':
                print 'Add'
                
            elif sub_query== 'Project total':
                print 'Add'
                
            elif sub_query== 'Quit':
                query=raw_input('What would you like to do?\n'
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'
                '"Delete" a project\n'
                '"Save and Exit"\n'
                '\n')
                
            else:
                print "Sorry I didnt get that. Try again."
                sub_query=raw_input('Would you like to:\n'
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'
                '"Delete" a project\n'
                '"Save and Exit"\n'
                '\n')              
        
        while query=='Delete':
            sub_query=raw_input('Would you like to:\n'
            '"Delete item"?\n'
            '"Delete overheads"?\n'
            '"Delete hours"?\n'
            '"Delete profit"?\n'
            '"Quit"\n'
            '\n')
            
            if sub_query== 'Delete item':
                print 'Add'
                
            elif sub_query== 'Delete overheads':
                print 'Add'
                
            elif sub_query== 'Delete hours':
                print 'Add'
                
            elif sub_query== 'Delete profit':
                print 'Add'
                               
            elif sub_query== 'Quit':
                query=raw_input('What would you like to do?\n'
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'
                '"Delete" a project\n'
                '"Save and Exit"\n'
                '\n')
                
            else:
                print "Sorry I didnt get that. Try again."
                sub_query=raw_input('Would you like to:\n'
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'
                '"Delete" a project\n'
                '"Save and Exit"\n'
                '\n')              
            
               
        if query=='Exit without saving':
            print "Write code to undo previous actions"
            action=raw_input('Choose one of the following options:\n'
            '"Inventory"\n'
            '"Project"\n'
            '"Restock"\n'
            '"Set Goal"\n'
            '"Quit"\n'
            '\n')        
        
        elif query=='Save and Exit':
            action=raw_input('Choose one of the following options:\n'
            '"Inventory"\n'
            '"Project"\n'
            '"Restock"\n'
            '"Set Goal"\n'
            '"Quit"\n'
            '\n')
                
        else:
            print "Sorry I didnt get that. Try again."
            query=raw_input('What would you like to do?\n'
            '"Create" a project\n'
            '"Add" to a project\n'
            '"Edit" a project\n'
            '"View" a project\n'
            '"Delete" a project\n'
            '"Exit without saving"\n'
            '"Save and Exit"\n'
            '\n')            
                        
    elif action=='Restock':
        print 'Coming soon!'
    
    elif action=='Set Goal':
        print 'Coming soon!'
        
    elif action=='Quit':
        print 'Goodbye'
        state='off'