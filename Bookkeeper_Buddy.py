import My_Projects
import Inventory

state='on' #'state' is supposed to represent the app/program being tuned on or accessed

print 'Welcome to "Bookkeeper Buddy"!'

while state=='on':
    #allows user to choose which part of their records to access
    action=raw_input('Choose one of the following options:\n'
    '"Inventory"\n'
    '"Projects"\n'
    '"Restock"\n'
    '"Set Goal"\n'
    '"Quit"\n'
    '\n')

    #catch all    
    while action!='Inventory' or action!='Projects' or action!='Restock' or action!='Set Goal' or action!='Quit':
        action=raw_input("I didn't get that. Choose one of the following options:\n"
        '"Inventory"\n'
        '"Projects"\n'
        '"Restock"\n'
        '"Set Goal"\n'
        '"Quit"\n'
        '\n')  
        
###############################################################################
#Inventory actions
###############################################################################
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
            a=Inventory.inventory()
            Inventory.inventory.add_item(a)
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
            Inventory.inventory.edit_item(a)
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory list"\n'
            '"View item info"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')

        elif query=='Add':
            Inventory.inventory.add_item(a)
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
            Inventory.inventory.view_inventory(a)
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
            Inventory.inventory.view_item(a)
            query=raw_input('What would you like to do?\n'
            '"Create" an inventory\n'
            '"Edit" the inventory\n'
            '"View inventory"\n'
            '"View item"\n'
            '"Delete" an inventory item\n'
            '"Done"?\n'
            '\n')
                
        elif query=='Delete':
            print Inventory.inventory.name
            Inventory.inventory.delete_item(a)
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
            '"Done"?\n'
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

        while query=='Create':
            My_Projects.projects.append(raw_input('Name your project! '))
            My_Projects.instances.append(My_Projects.my_projects())
            x=len(My_Projects.instances)-1
            My_Projects.instances[x].add_item()
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
                   print 'Adding' 
                elif sub_query== 'Add to overheads':
                   print 'Adding to overheads' 
                elif sub_query== 'Log hours':
                   print 'Logging hours' 
                elif sub_query== 'Set profit':
                   print 'Setting profit' 
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
                    print 'item'

                elif sub_query== 'View overheads':
                    print 'overheads'

                elif sub_query== 'View hours':
                    print 'hours'

                elif sub_query== 'View profit':
                    print 'profit'

                elif sub_query== 'Project total':
                    print 'total'

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
                    print 'Deleting item'

                elif sub_query== 'Delete overheads':
                    print 'Deleting overheads'

                elif sub_query== 'Delete hours':
                    print 'Deleting hours'

                elif sub_query== 'Delete profit':
                    print 'Deleting profit'

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
