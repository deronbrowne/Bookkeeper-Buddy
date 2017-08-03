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
# Inventory actions
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
        
        while query!='Create' or query!='Edit' or query!='Add' or query!='View inventory' or query!='View item' or query!='Delete' or query!='Done':
            action=raw_input("I didn't get that. Choose one of the following options:\n"
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
###############################################################################
# Project actions
###############################################################################   
    elif action=='Projects':
        #ask user what he'd like to do. Choose from the options
        query=raw_input('What would you like to do?\n'
        '"Create" a project\n'
        '"Edit" a project\n'
        '"View" a project\n'      
        '"Delete" a project\n'
        '"Exit"\n'
        '\n')
        #catch all
        while query!='Create' or query!='Edit' or query!='View' or query!='Delete' or query!='Exit':
            query=raw_input("That isn't a valid option. What would you like to do?\n"
            '"Create" a project\n'
            '"Edit" a project\n'
            '"View" a project\n'      
            '"Delete" a project\n'
            '"Exit"\n'
            '\n')

        while query=='Create':# if user wants to create a project
            My_Projects.projects.append(raw_input('Name your project! '))
            My_Projects.instances.append(My_Projects.my_projects()) #my attempt at using user input to initialize an instance
            x=len(My_Projects.instances)-1
            My_Projects.instances[x].add_item()
            query=raw_input('What would you like to do?\n'
            '"Create" a project\n'
            '"Edit" a project\n'
            '"View" a project\n'      
            '"Delete" a project\n'
            '"Exit"\n'
            '\n')
            #catch all
            while query!='Create' or query!='Edit' or query!='View' or query!='Delete' or query!='Exit':
                query=raw_input("That isn't a valid option. What would you like to do?\n"
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'      
                '"Delete" a project\n'
                '"Exit"\n'
                '\n')

        while query=='Edit': #if user wants to edit something
            print My_Projects.projects #print options
            which_project=raw_input('Which project are you editing?\n'
            '\n')
            #catch all
            while which_project not in My_Projects.projects:
                print My_Projects.projects
                which_project=raw_input("That isn't one of your active projects\n"
                'Which project are you editing?\n'
                '\n') 
            
            #asks user what kind of edit he'd like to carry out
            sub_query=raw_input('Would you like to:\n'
            '"Add" something?\n'
            '"Change" something?\n'    
            '"Delete" something?\n'
            '"Quit"?\n'                    
            '\n')
            #catch all
            while sub_query!='Add' or sub_query!='Change' or sub_query!='Delete' or sub_query!='Quit':            
                sub_query=raw_input("That's not a valid option. Would you like to:\n"
                '"Add" something?\n'
                '"Change" something?\n'    
                '"Delete" something?\n'
                '"Quit"?\n'                    
                '\n')
                
            #executes based on user input
            if sub_query== 'Add':
                #asks user which project characteristic he'd like to add to
                sub_sub_query=raw_input('What are you adding to?\n'
                                   '"Project items"?\n'
                                   '"Overheads"?\n'
                                   '"Hours worked"?\n'
                                   '"Done"\n'
                                   '\n')
                #catch all
                while sub_sub_query!='Project items' or sub_sub_query!='Overheads' or sub_sub_query!='Hours worked' or sub_sub_query!='Done':            
                    sub_sub_query=raw_input("That's not a valid option. What are you adding to?\n"
                                       '"Project items"?\n'
                                       '"Overheads"?\n'
                                       '"Hours worked"?\n'
                                       '"Done"\n'
                                       '\n')
                
            elif sub_query== 'Change':
                #asks user which project characteristic he would like to change
                sub_sub_query=raw_input('What are you editing?\n'
                                   '"Project items"?\n'
                                   '"Overheads"?\n'
                                   '"Hours worked"?\n'
                                   '"Done"\n'
                                   '\n')
                #catch all
                while sub_sub_query!='Project items' or sub_sub_query!='Overheads' or sub_sub_query!='Hours worked' or sub_sub_query!='Done':            
                    sub_sub_query=raw_input("That's not a valid option. What are you editing?\n"
                                       '"Project items"?\n'
                                       '"Overheads"?\n'
                                       '"Hours worked"?\n'
                                       '"Done"\n'
                                       '\n')
                                       
            elif sub_query== 'Delete':
                #asks user which project characteristic he would like to delete
                sub_sub_query=raw_input('What are you deleting?\n'
                                   '"Project items"?\n'
                                   '"Overheads"?\n'
                                   '"Hours worked"?\n'
                                   '"Done"\n'
                                   '\n')
                #catch all
                while sub_sub_query!='Project items' or sub_sub_query!='Overheads' or sub_sub_query!='Hours worked' or sub_sub_query!='Done':            
                    sub_sub_query=raw_input("That's not a valid option. What are you deleting?\n"
                                       '"Project items"?\n'
                                       '"Overheads"?\n'
                                       '"Hours worked"?\n'
                                       '"Done"\n'
                                       '\n')
               
            elif sub_query== 'Quit':
                #once user is finished editing, ask user what he'd like to do next
                query=raw_input('What would you like to do?\n'
                '"Create" a project\n'
                '"Edit" a project\n'
                '"View" a project\n'      
                '"Delete" a project\n'
                '"Exit"\n'
                '\n')
                #catch all
                while query!='Create' or query!='Edit' or query!='View' or query!='Delete' or query!='Exit':
                    query=raw_input("That isn't a valid option. What would you like to do?\n"
                    '"Create" a project\n'
                    '"Edit" a project\n'
                    '"View" a project\n'      
                    '"Delete" a project\n'
                    '"Exit"\n'
                    '\n')  


        while query=='View': #ask user to identify which part of the project he'd like to view
            sub_query=raw_input('Would you like to:\n'
            '"View item"?\n'
            '"View overheads"?\n'
            '"View hours"?\n'
            '"View profit"?\n'
            'View the "Project total"?\n'
            '"Quit"\n'
            '\n')
            
            #catch all
            while sub_query!='View item' or sub_query!='View overheads' or sub_query!='View hours' or sub_query!='View profit' or sub_query!='Project total' or sub_query!='Quit':
                sub_query=raw_input("Sorry, I didn't get that. Would you like to:\n"
                                    '"View item"?\n'
                                    '"View overheads"?\n'
                                    '"View hours"?\n'
                                    '"View profit"?\n'
                                    'View the "Project total"?\n'
                                    '"Quit"\n'
                                    '\n')

# at this point I'd like to be able to reference particular instances of the My_Projects class based on the user defined name for the class. Not sure how to do that.
            if sub_query== 'View item':

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
