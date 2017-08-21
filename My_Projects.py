#initialize lists to keep track of all the projects, their totals
#and to track which inctances of the class "my_projects correspond to each title
projects=[]
instances=[]
project_total=[]
#record hourly rate to enable user to pay himself absed on hours worked
hourly_rate=float(raw_input('What is your hourly rate? '))

class my_projects:
    #lists to record information about the items from the inventory being used in a project
    items=[]
    item_cost=[]
    item_count=[]
    item_subtotal=[]
    #lists to record information about the overhead costs associated with this projects    
    overheads=[]
    overhead_cost=[]
    #lists to record information for paying yourself   
    day=[]
    time=[]
    salary=[]
    #lists to record information about the profit
    percent_profit=[]
    profit=[]
    choice = ['Yes', 'No']  
    
#####################################################################################
#handling project items
#####################################################################################    
    def add_item(self): #adding items to the project
        add_another='Yes'
        while add_another=='Yes':#allows user to add multiple items
            self.items.append(raw_input('What are you adding?\n'))
            self.item_cost.append(float(raw_input('How much does it cost?\n')))
            self.item_count.append(float(raw_input('How many are you adding?\n')))
            a=self.item_cost[len(self.item_cost)-1] #grabs the value of the last added item
            b=self.item_count[len(self.item_count)-1] #grabs the count of the last added item
            self.item_subtotal.append(a*b) #calculates the total cost for all of a particular item          
            print '\n'.join(self.choice)
            add_another=raw_input('Would you like to add another item?\n'
            '\n')
            while add_another not in self.choice: #catch all
                print "Sorry, that isn't an option.\n"
                print '\n'.join(self.choice)
                add_another=raw_input('Would you like to add another item?\n'
                '\n')
        
    def view_items(self): #view all the information on project items
        x=len(self.items)-1
        for index in xrange(1,x):
            print self.items[index]
            print self.item_cost[index]
            print self.item_count[index]
            print self.item_subtotal[index]
            print '\n'
        print 'Subtotal for this project = $'+sum(self.item_subtotal) #total value of all the items in the project
        
    def delete_items(self):
        delete_another='Yes'
        while delete_another=='Yes':#allows user to delete multiple items
            print '\n'.join(self.items) #shows user the available options
            a=raw_input('Which item would you like to delete?\n') #asks for a choice
            while a not in self.items: #catch all
                print '\n'.join(self.items)
                a=raw_input("Sorry that item isn't part of your project\n"
                            "Which item would you like to delete?\n"
                           "\n")         
            x=self.items.index(a) #grab index and show user what is about to be deleted
            print self.items[x]
            print self.item_cost[x]
            print self.item_count[x]
            print self.item_subtotal[x]
            print '\n'
            print '\n'.join(self.choice)
            confirm=raw_input('Are you sure?\n'
                                '\n')
            while confirm not in self.choice: #catch all
                print '\n'.join(self.choice)
                confirm=raw_input("I didn't quite catch that. Are you sure?\n"
                '\n')                
            if confirm=='Yes': #deletes item and associated information if choice is 'Yes'
                del self.items[x]
                del self.item_cost[x]
                del self.item_count[x]
                del self.item_subtotal[x]
                print '\n'.join(self.choice)
                delete_another=raw_input('Would you like to delete another item?\n'
                                            '\n')
                while delete_another not in self.choice: #catch all
                    print "Sorry, that isn't an option.\n"
                    print '\n'.join(self.choice)
                    delete_another=raw_input('Would you like to delete another item?\n'
                    '\n')                                            
            elif confirm=='No': #shows user that item was not deleted if the choice is 'No'
                print self.items[x]
                print self.item_cost[x]
                print self.item_count[x]
                print self.item_subtotal[x]
                print '\n'
                print '\n'.join(self.choice)
                delete_another=raw_input('Would you like to delete another item?\n'
                                            '\n')
                while delete_another not in self.choice: #catch all
                    print "Sorry, that isn't an option.\n"
                    print '\n'.join(self.choice)
                    delete_another=raw_input('Would you like to delete another item?\n'
                    '\n')                  
#####################################################################################
#handling overheads
#####################################################################################         
    def add_overhead_item(self): #adding overheads to the project; name & cost
        add_another='Yes'
        while add_another=='Yes':
            self.overheads.append(raw_input('What are you adding?\n'))
            self.overhead_cost.append(float(raw_input('How much does it cost?\n')))
            print '\n'.join(self.choice)
            add_another=raw_input('Would you like to add another?\n'
                                    '\n')
            while add_another not in self.choice:
                print "Sorry, that isn't an option.\n"
                print '\n'.join(self.choice)
                add_another=raw_input('Would you like to add another?\n'
                                        '\n')  
                
        if add_another=='No':
            self.view_overheads()
        
    def view_overheads(self,a):#view all the information on overheads
        x=len(self.overheads)-1
        for index in range(1,x):
            print self.overheads[index]
            print self.overhead_cost[index]
            print '\n'#shows each overhead and the associated cost
        print 'Total overhead = ' + sum(self.overhead_cost) #shows total cost of overheads
        
    def delete_overhead(self):
        delete_another='Yes'
        while delete_another=='Yes':#allows user to delete multiple items
            self.view_overheads() #shows user the available options
            a=raw_input('Which item would you like to delete?\n') #asks for a choice
            while a not in self.overheads: #catch all
                self.view_overheads()
                a=raw_input("Sorry that overhead isn't part of your project\n"
                            "Which overhead would you like to delete?\n"
                           "\n") 
            x=self.overheads.index(a)
            print self.overheads[x]
            print self.overhead_cost[x]
            print '\n'
            print '\n'.join(self.choice)
            confirm=raw_input('Are you sure?\n'
                            '\n')
            while confirm not in self.choice: #catch all
                print '\n'.join(self.choice)
                confirm=raw_input("I didn't quite catch that. Are you sure? Yes/No\n"
                                    "\n")                
            if confirm=='Yes': #deletes item and associated information if choice is 'Yes'
                del self.overheads[x]
                del self.overhead_cost[x]
                print '\n'
                print '\n'.join(self.choice)                
                delete_another=raw_input('Would you like to delete another item?\n'
                                            '\n')
                while delete_another not in self.choice: #catch all
                    print "Sorry, that isn't an option.\n"
                    print '\n'
                    print '\n'.join(self.choice)
                    delete_another=raw_input('Would you like to delete another item?\n'
                    '\n')             
            elif confirm=='No': #shows user that item was not deleted if the choice is 'No'
                print self.overheads[x]
                print self.overhead_cost[x]
                delete_another=raw_input('Would you like to delete another item?\n'
                                            '\n')
                while delete_another not in self.choice: #catch all
                    print "Sorry, that isn't an option.\n"
                    print '\n'
                    print '\n'.join(self.choice)
                    delete_another=raw_input('Would you like to delete another item?\n'
                    '\n')             
                
#####################################################################################
#handling hours worked and salary
#####################################################################################             
    def log_hours(self): #allows user to record the number of hours worked and the value of that time based on his hourly rate
        self.day.append(raw_input('What date are you adding hours for?\n'))
        self.time.append(float(raw_input('How many hours did you work?\n')))
        a=self.time[len(self.time)-1]
        self.salary.append(a*self.hourly_rate)
        
    def view_hours(self):
        x=len(self.hours)-1
        print 'Hourly rate = $'+self.hourly_rate
        for index in range(1,x):
            print self.date[index], self.hours[index], self.salary[index]
        print 'Salary for this project = $'+sum(self.salary)
        
    def delete_hours(self):
        delete_another='Yes'
        while delete_another=='Yes':#allows user to delete multiple items
            self.view_hours() #shows user the available options
            a=raw_input('Which date would you like to delete?\n') #asks for a choice
            while a not in self.date: #catch all
                print self.view_hours()
                a=raw_input("Sorry there aren't any hours logged for that date.\n"
                            "Which date would you like to delete?\n"
                           "\n") 
        x=raw_input('Which date would you like to delete?\n')
        print self.date[x]
        print self.time[x]
        print self.salary[x]
        confirm=raw_input('Are you sure?\n'
                            '"Yes"/"No"\n'
                            '\n')
        while confirm!='Yes' or confirm!='No': #catch all
            confirm=raw_input("I didn't quite catch that. Are you sure?\n"
                                '"Yes"/"No"\n'
                                "\n")                
        if confirm=='Yes': #deletes item and associated information if choice is 'Yes'
            del self.overheads[x]
            del self.overhead_cost[x]
            delete_another=raw_input('Would you like to delete another date?\n'
                                        '"Yes"/"No"\n'
                                        '\n')
            while delete_another!='Yes' or delete_another!='No': #catch all
                print "Sorry, that isn't an option.\n"
                delete_another=raw_input('Would you like to delete another date?\n'
                '"Yes"/"No"\n'
                '\n')             
        elif confirm=='No': #shows user that item was not deleted if the choice is 'No'
            print self.date[x]
            print self.time[x]
            print self.salary[x]
            delete_another=raw_input('Would you like to delete another date?\n'
                                        '"Yes"/"No"\n'
                                        '\n')
            while delete_another!='Yes' or delete_another!='No': #catch all
                print "Sorry, that isn't an option.\n"
                delete_another=raw_input('Would you like to delete another item?\n'
                '"Yes"/"No"\n'
                '\n') 
           
            
    def set_profit(self): #allows user to set a desired profit that is calculated based on overheads and cost of raw materials
        self.percent_profit = float(('How much profit would you like to make? %')/100) #asks for a percentage and converts to a decimal
        self.profit=self.percent_profit*sum(self.overhead_total+sum(self.item_subtotal)) #calculates the profit in dollars and cents
        
    def view_profit(self): #displays the percentage of profit set for a project and the current equivalent dollar value
        print 'Profit '+'('+self.percent_profit+')'+'% = $'+self.profit
    
    def calc_project_total(self): #shows the user how much he should sell the project for
                                  #in order to cover the cost of all items, overheads, labour and profit
        print projects #shows a list of all projects
        x=projects.index(raw_input('Which project are you inquiring about?\n'
                                    '\n'))
        #calculate & display updated project total                                    
        project_total[x]= (sum(self.item_subtotal)+sum(self.overhead_cost)+sum(self.salary)+self.profit)
        print 'Sell this project for $'+project_total(x)
