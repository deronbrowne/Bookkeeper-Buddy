state='on' #'state' is supposed to represent the app/program being tuned on or accessed
print '\n'
print 'Welcome to "Bookkeeper Buddy"!'

while state=='on':
    #allows user to choose which part of their records to access
    choices = ['Inventory', 'Projects', 'Restock', 'Set Goal', 'Quit']
    print '\n'
    print '\n'.join(choices)
    action=raw_input('Pick an option:\n'
                    '\n')

    #catch all    
    while action not in choices:
        print '\n'
        print '\n'.join(choices)
        action=raw_input("I didn't get that. Pick an option:\n"
                        '\n')
        
###############################################################################
# Inventory actions
###############################################################################
    while action=='Inventory':
        import Inventory
        
        options=['Create', 'Edit', 'View', 'Save & Exit'] #create list with available options
        print '\n'
        print '\n'.join(options) #display list members each on a new line
        query=raw_input('What would you like to do?\n' #ask for user choice
        '\n')
        
        #catch all
        while query not in options:
            print '\n'
            print '\n'.join(options)
            query=raw_input("I didn't get that. Choose one of the options:\n"
            '\n')
        
        #Create
        ##################################################################
        if query=='Create': #as long as user wants to create an inventory
            a=Inventory.inventory() #initialize instance; want to allow user to create more than one inventory...need to assign user input to instance name
            Inventory.inventory.add_item(a) #add items
        
        #Edit
        ##################################################################
        if query=='Edit':
            #ask for user choice & check
            sub_options=['Add','Change','Delete','Save & Exit']
            print '\n'
            print '\n'.join(sub_options)
            sub_query=raw_input('What would you like to do?\n'
            '\n')
            while sub_query not in sub_options:
                print '\n'.join(sub_options)
                sub_query=raw_input("I didn't get that. Choose one of the options:\n"
                '\n')
            #------------------------------------#
            if sub_query=='Add':
                Inventory.inventory.add_item(a)

            #-----------------------------------#
            elif sub_query=='Change':
                Inventory.inventory.edit_item(a) 
       
            #------------------------------------#    
            elif sub_query== 'Delete':
                #asks user which inventory characteristic he would like to delete
                sub_sub_options=['Items', 'Inventory', 'Done']
                print'\n'
                print '\n'.join(sub_sub_options)                                
                sub_sub_query=raw_input('What are you deleting?\n'
                                   '\n')
                #catch all
                while sub_sub_query not in sub_sub_options:
                    print '\n'.join(sub_sub_options)                                
                    sub_sub_query=raw_input('What are you deleting?\n'
                                       '\n')
                
                if sub_sub_query=='Items':
                    Inventory.inventory.delete_item(a)
                    
                elif sub_sub_query=='Inventory':
                    Inventory.inventory.view_inventory(a)
                    Inventory.inventory.delete_inventory(a)
                    
                elif sub_sub_query=='Done':
                    pass         
            #--------------------------------------#
            elif sub_query=='Save & Exit':
                #allows user to choose which part of their records to access
                choices = ['Inventory', 'Projects', 'Restock', 'Set Goal', 'Quit']
                print '\n'
                print '\n'.join(choices)
                action=raw_input('Pick an option:\n'
                                '\n')
            
                #catch all    
                while action not in choices:
                    print '\n'
                    print '\n'.join(choices)
                    action=raw_input("I didn't get that. Pick an option:\n"
                                    '\n')
        
        #View                                             
        ########################################################################
        if query=='View':
            sub_options=['Items','Inventory','Done']
            print '\n'.join(sub_options)
            
            sub_query=raw_input('What would you like to view?\n'
            '\n')

            while sub_query not in sub_options:
                print '\n'.join(sub_options)
                sub_query=raw_input("I didn't get that. Choose one of the options:\n"
                '\n')
            #---------------------------------------#            
            if sub_query=='Inventory':
                if Inventory.inventory.name==[]:
                    print 'Your inventory is empty. Add some items!'
                    pass                
                else:
                    Inventory.inventory.view_inventory(a)
            #---------------------------------------#
            elif sub_query=='Items':
                if Inventory.inventory.name==[]:
                    print 'Your inventory is empty. Add some items!'
                    pass                
                else:
                    Inventory.inventory.view_item(a)
            #---------------------------------------#
            elif sub_query=='Done':
                pass

        #Save & Exit
        ######################################################################
        if query=='Save & Exit':
            #allows user to choose which part of their records to access
            choices = ['Inventory', 'Projects', 'Restock', 'Set Goal', 'Quit']
            print '\n'
            print '\n'.join(choices)
            action=raw_input('Pick an option:\n'
                            '\n')
        
            #catch all    
            while action not in choices:
                print '\n'
                print '\n'.join(choices)
                action=raw_input("I didn't get that. Pick an option:\n"
                                '\n')
            
###############################################################################
# Project actions
###############################################################################   
    while action=='Projects':
        import My_Projects
        #ask user what he'd like to do. Choose from the options
        options=['Create','Edit','View','Delete','Exit']
        print '\n'.join(options)
        query=raw_input('What would you like to do?\n'
        '\n')
        
        #catch all
        while query not in options:
            print '\n'.join(options)
            query=raw_input("That isn't a valid option. What would you like to do?\n"
            '\n')

        #Create
        #######################################################################
        while query=='Create':# if user wants to create a project
            My_Projects.projects.append(raw_input('Name your project! '))
            My_Projects.instances.append(My_Projects.my_projects()) #my attempt at using user input to initialize an instance
            x=len(My_Projects.instances)-1
            My_Projects.instances[x].add_item()

        #Edit
        #######################################################################
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
            sub_options=['Add','Change','Delete','Quit']
            print '\n'.join(sub_options)
            sub_query=raw_input('How would you like to edit this project:\n'            
            '\n')
            #catch all
            while sub_query not in sub_options:
                print '\n'.join(sub_options)
                sub_query=raw_input("That's not a valid option. How would you like to edit this project:\n"            
                '\n')                
                
            #executes based on user input
            if sub_query== 'Add':
                #asks user which project characteristic he'd like to add to
                sub_sub_options=['Project items','Overheads','Hours worked','Done']
                print sub_sub_options
                sub_sub_query=raw_input('What are you adding to?\n'
                                   '\n')
                #catch all
                while sub_sub_query not in sub_sub_options:            
                    print sub_sub_options
                    sub_sub_query=raw_input("That isn't a valid option. What are you adding to?\n"
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

        #View
        #######################################################################
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
                pass
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

        #Delete
        #######################################################################
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

        #Exit without saving
        #######################################################################
        if query=='Exit without saving':
            print "Write code to undo previous actions"
            action=raw_input('Choose one of the following options:\n'
            '"Inventory"\n'
            '"Project"\n'
            '"Restock"\n'
            '"Set Goal"\n'
            '"Quit"\n'
            '\n')        

        #Save & Exit
        #######################################################################
        elif query=='Save & Exit':
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
                        
    while action=='Restock':
        print 'Coming soon!'
    
    while action=='Set Goal':
        print 'Coming soon!'
        
    if action=='Quit':
        print 'Goodbye'
        state='off'
