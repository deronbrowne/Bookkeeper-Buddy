state='on' #'state' is supposed to represent the app/program being tuned on or accessed
print '\n'
print 'Welcome to "Bookkeeper Buddy"!'
import input_check
import Inventory
import My_Projects

#import pprint, pickle
#
#pkl_file = open('data.pkl', 'rb')
#
#Inventory.inventory_record = pickle.load(pkl_file)
#pprint.pprint(Inventory.inventory_record)
#
#My_Projects.projects = pickle.load(pkl_file)
#pprint.pprint(My_Projects.projects)
#
#My_Projects.instances = pickle.load(pkl_file)
#pprint.pprint(My_Projects.instances)
#
#My_Projects.project_total = pickle.load(pkl_file)
#pprint.pprint(My_Projects.project_total)
#
#pkl_file.close()


while state=='on':
    #allows user to choose which part of their records to access
    level=1
    prompt=('Pick an option')
    action=input_check.check(level,prompt)
        
###############################################################################
# Inventory actions
###############################################################################
    while action=='inventory':
        #allows user to choose which part of their records to access
        level=2
        prompt=('What would you like to do')
        query=input_check.check(level,prompt)
        
        #Create
        ##################################################################
        if query=='create': #as long as user wants to create an inventory
            new_name=raw_input('Name this inventory! \n'
                                            '\n')
            Inventory.inventory_record[new_name]=Inventory.inventory() #initialize instance; want to allow user to create more than one inventory...need to assign user input to instance name       
            names=Inventory.inventory_record.keys()
            a=names.index(new_name)
            Inventory.inventory_record[Inventory.inventory_record.keys()[a]].add_item() #add items
        
        #Edit
        ##################################################################
        elif query=='edit':
            #allows user to choose which of his inventories he'd like to edit
            level=13
            prompt='Which inventory would you like to edit?'
            key=input_check.check(level,prompt) #saves the name of the inventory the user wants to access
            a=Inventory.inventory_record.keys().index(key) #saves the index of the key the user is accessing
            
            #allows user to choose which part of their records to access            
            level=3
            prompt=('What would you like to do')
            sub_query=input_check.check(level,prompt)
            
            #------------------------------------#
            if sub_query=='add':
                Inventory.inventory_record[key].add_item()

            #-----------------------------------#
            elif sub_query=='change':
                Inventory.inventory_record[key].edit_item() 
       
            #------------------------------------#    
            elif sub_query== 'delete':
                #asks user which inventory characteristic he would like to delete
                level=4
                prompt=('What are you deleting')
                sub_sub_query=input_check.check(level,prompt)
                
                if sub_sub_query=='items':
                    if Inventory.inventory_record[key].name==[]:
                        print 'Your inventory is empty. Add some items!'
                        pass                
                    else:                    
                        Inventory.inventory_record[key].delete_item()
                        
                elif sub_sub_query=='inventory':
                    Inventory.inventory_record[key].delete_inventory(key)
                    
                elif sub_sub_query=='done':
                    pass         
            #--------------------------------------#
            elif sub_query=='save & exit':
                level=2
                prompt=('What would you like to do')
                query=input_check.check(level,prompt)
        
        #View                                             
        ########################################################################
        elif query=='view':
            #allows user to choose which of his inventories he'd like to view
            level=13
            prompt='Which inventory would you like to view?'
            key=input_check.check(level,prompt) #saves the name of the inventory the user wants to access
            a=Inventory.inventory_record.keys().index(key) #saves the index of the key the user is accessing            
            
            #allows user to choose which part of their records to access
            level=4
            prompt=('What are you viewing')
            sub_query=input_check.check(level,prompt)
            
            #---------------------------------------#            
            if sub_query=='summary':
                if Inventory.inventory_record[key].name==[]:
                    print 'Your inventory is empty. Add some items!'
                    pass                
                else:
                    Inventory.inventory_record[key].view_inventory()
            #---------------------------------------#
            elif sub_query=='items':
                if Inventory.inventory_record[key].name==[]:
                    print 'Your inventory is empty. Add some items!'
                    pass                
                else:
                    Inventory.inventory_record[key].view_item()
            #---------------------------------------#
            elif sub_query=='done':
                pass

        #Save & Exit
        ######################################################################
        elif query=='save & exit':
            #allows user to choose which part of their records to access
            level=1
            prompt=('Pick an option')
            action=input_check.check(level,prompt)
            pass
            
            
###############################################################################
# Project actions
###############################################################################   
    while action=='projects':
        #ask user what he'd like to do. Choose from the options
        level=2
        prompt=('What would you like to do')
        query=input_check.check(level,prompt)

        #Create
        #######################################################################
        while query=='create':# if user wants to create a project
            My_Projects.projects.append(raw_input('Name your project! '))
            My_Projects.instances.append(My_Projects.my_projects()) #my attempt at using user input to initialize an instance
            x=len(My_Projects.instances)-1
            My_Projects.instances[x].add_item()

        #Edit
        #######################################################################
        while query=='edit': #if user wants to edit something
            level=5
            prompt=('Which project are you editing')
            input_check.check(level,prompt)
            
            
            #asks user what kind of edit he'd like to carry out
            level=3
            prompt=('How would you like to edit this project?')
            sub_query=input_check.check(level,prompt)
                
            #executes based on user input
            if sub_query== 'add':
                #asks user which project characteristic he'd like to add to
                level=6
                prompt=('What are you adding to?')
                sub_sub_query=input_check.check(level,prompt)
                pass
                
            elif sub_query== 'change':
                level=6
                prompt=('What are you changing?')
                sub_sub_query=input_check.check(level,prompt)
                pass
                                       
            elif sub_query== 'delete':
                #asks user which project characteristic he would like to delete
                level=6
                prompt=('What are you deleting?')
                sub_sub_query=input_check.check(level,prompt)
                pass
               
            elif sub_query== 'save & exit':
                #once user is finished editing, ask user what he'd like to do next
                level=2
                prompt=('What would you like to do?')
                query=input_check.check(level,prompt)
                pass  

        #View
        #######################################################################
        while query=='View': #ask user to identify which part of the project he'd like to view
            level=6
            prompt=('What would you like to view?')
            sub_query=input_check.check(level,prompt)
            pass        

# at this point I'd like to be able to reference particular instances of the My_Projects class based on the user defined name for the class. Not sure how to do that.
            if sub_query== 'item':
                print 'items'
                pass
            
            elif sub_query== 'overheads':
                print 'overheads'
                pass
            
            elif sub_query== 'hours':
                print 'hours'
                pass
            
            elif sub_query== 'profit':
                print 'profit'
                pass

            elif sub_query== 'done':
                level=2
                prompt=('What would you like to do?')
                query=input_check.check(level,prompt)
                pass             

        #Delete
        #######################################################################
        while query=='delete':
            level=6
            prompt=('What would you like to delete?')
            sub_query=input_check.check(level,prompt)
            pass 

            if sub_query== 'item':
                print 'Deleting item'

            elif sub_query== 'overheads':
                print 'Deleting overheads'

            elif sub_query== 'hours':
                print 'Deleting hours'

            elif sub_query== 'profit':
                print 'Deleting profit'

            elif sub_query== 'done':
                level=2
                prompt=('What would you like to do?')
                query=input_check.check(level,prompt)
                pass  
           

        #Exit without saving
        #######################################################################
        if query=='Exit without saving':
            print "Write code to undo previous actions"
            level=1
            prompt=('Pick an option')
            action=input_check.check(level,prompt)      

        #Save & Exit
        #######################################################################
        elif query=='Save & Exit':
            level=1
            prompt=('Pick an option')
            action=input_check.check(level,prompt)         
                        
    while action=='Restock':
        print 'Coming soon!'
        pass
    
    while action=='Set Goal':
        print 'Coming soon!'
        pass
    
    while action=='Sell item':
        print 'Coming soon!'
        pass
        
    if action=='quit':       
        print 'Goodbye'
        state='off'

#import pickle
#
#output = open('data.pkl', 'wb')
#
## Pickle dictionary using protocol 0.
#pickle.dump(Inventory.inventory_record, output)
#pickle.dump(My_Projects.projects, output, -1)
#pickle.dump(My_Projects.instances, output, -1)
#pickle.dump(My_Projects.project_total, output, -1)
#
#output.close()