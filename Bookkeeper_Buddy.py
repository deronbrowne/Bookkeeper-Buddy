# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 21:24:08 2017

@author: Deron

Title: Bookkeeper Buddy

Description:    This project is aimed at small businesses who want a simple and 
                easy way to track inventory, how new projects affect the inventory
                and to keep track of how and when to restock. You can also set goals
                to ensure that targets are met.                
"""

#class restock:
    


#class set_goal:


state='on'
execfile('Inventory_Class.py')
execfile('My_Projects_Class.py')

print 'Welcome to "Bookkeeper Buddy"!'

while state=='on': 
    
    action=raw_input('Choose one of the following options:\n'
    '"Inventory"\n'
    '"Project"\n'
    '"Restock"\n'
    '"Set Goal"\n'
    '\n')

    if action=='Inventory':
        
        query=raw_input('What would you like to do?\n'
        '"Create" an inventory\n'
        '"Edit" the inventory\n'
        '"View inventory"\n'
        '"View item"\n'
        '"Delete" an inventory item\n'
        '"Quit"?\n'
        '\n')
                      
        if query=='Create':
            Save = 'keep adding'
            while Save=='keep adding':
                    a=inventory()
                    inventory.add_item(a)
                    Save=raw_input('Would you like to save your inventory or keep adding? Save/keep adding ')
            del a
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Quit"?\n'
            '\n')
                
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
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Quit"?\n'
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
                '"Quit"?\n'
                '\n')
            else:
                Save=raw_input('Try again.\n'
                'Would you like to:\n'
                '"Save"\n'
                'or"Keep editing"\n')
         
        elif query=='View inventory':
            print inventory.name
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Quit"?\n'
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
            '"Quit"?\n'
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
            '"Quit"?\n'
            '\n')  
        
        elif query=='Quit':
            action=raw_input('Choose one of the following options:\n'
            '"Inventory"\n'
            '"Project"\n'
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
            query=raw_input('What would you like to do?\n'
            '"Create" a project\n'
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
                
            elif sub_query== 'Add to overheads':
                
            elif sub_query== 'Log hours':
                
            elif sub_query== 'Set profit':
                
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
                
            elif sub_query== 'View overheads':
                
            elif sub_query== 'View hours':
                
            elif sub_query== 'View profit':
                
            elif sub_query== 'Project total':
                
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
                
            elif sub_query== 'Delete overheads':
                
            elif sub_query== 'Delete hours':
                
            elif sub_query== 'Delete profit':
                               
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
            
               
        if query=='Save and Exit':
            action=raw_input('Choose one of the following options:\n'
            '"Inventory"\n'
            '"Project"\n'
            '"Restock"\n'
            '"Set Goal"\n'
            '\n')
                
        else:
            print "Sorry I didnt get that. Try again."
            query=raw_input('What would you like to do?\n'
            '"Create" a project\n'
            '"Edit" a project\n'
            '"View" a project\n'
            '"Delete" a project\n'
            '"Save and Exit"\n'
            '\n')              
                        
    elif action=='Restock':
        print 'Coming soon!'
    
    elif action=='Set Goal':
        print 'Coming soon!'

print 'Goodbye'
state='off'

        

