#initialize lists to keep track of all the projects, their totals
#and to track which inctances of the class "my_projects correspond to each title
projects=[]
instances=[]
project_total=[]
import input_check

class my_projects:
    def __init__(self):
        #record hourly rate to enable user to pay himself absed on hours worked
        self.hourly_rate=30
        level=7
        prompt= 'Your default hourly rate has been set to $30/hr. Would you like to change it?'
        add_another=input_check.check(level,prompt)
        if add_another=='yes':
            self.hourly_rate=raw_input('What would you like to change it to?')
        #lists to record information about the items from the inventory being used in a project
        self.items=[]
        self.item_cost=[]
        self.item_count=[]
        self.item_subtotal=[]
        #lists to record information about the overhead costs associated with this projects    
        self.overheads=[]
        self.overhead_cost=[]
        #lists to record information for paying yourself   
        self.day=[]
        self.time=[]
        self.salary=[]
        #lists to record information about the profit
        self.percent_profit=[]
        self.profit=[]
    
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
            
            level=7
            prompt= 'Would you like to add another item?'
            add_another=input_check.check(level,prompt)
        
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
            print '\n'
            print '\n'.join(self.items)
            b=str.lower(raw_input('Which item would you like to delete?\n'
                                        '\n'))
            while b not in self.items:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.items)
                print '\n'
                b=str.lower(raw_input()) 
            
            x=self.items.index(b) #grab index and show user what is about to be deleted           
            print self.items[x]
            print self.item_cost[x]
            print self.item_count[x]
            print self.item_subtotal[x]
            print '\n'
            
            level=7
            prompt= 'Are you sure?'
            confirm=input_check.check(level,prompt)
              
            if confirm=='Yes': #deletes item and associated information if choice is 'Yes'
                del self.items[x]
                del self.item_cost[x]
                del self.item_count[x]
                del self.item_subtotal[x]
                
                level=7
                prompt= 'Would you like to delete another item?'
                delete_another=input_check.check(level,prompt)                                           
                
            elif confirm=='No': #shows user that item was not deleted if the choice is 'No'
                print self.items[x]
                print self.item_cost[x]
                print self.item_count[x]
                print self.item_subtotal[x]
                print '\n'
                print '\n'.join(self.choice)
                level=7
                prompt= 'Would you like to delete another item?'
                delete_another=input_check.check(level,prompt)
                
#####################################################################################
#handling overheads
#####################################################################################         
    def add_overhead_item(self): #adding overheads to the project; name & cost
        add_another='Yes'
        while add_another=='Yes':
            self.overheads.append(raw_input('What are you adding?\n'))
            self.overhead_cost.append(float(raw_input('How much does it cost?\n')))
            
            level=7
            prompt= 'Would you like to add another?'
            add_another=input_check.check(level,prompt)  
                
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
            print '\n'
            print '\n'.join(self.overheads)
            b=str.lower(raw_input('Which overhead would you like to delete?\n'
                                        '\n'))
            while b not in self.overheads:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.overheads)
                print '\n'
                b=str.lower(raw_input()) 

            x=self.overheads.index(b)
            print self.overheads[x]
            print self.overhead_cost[x]
            print '\n'
            
            level=7
            prompt= 'Are you sure?'
            confirm=input_check.check(level,prompt)  
              
            if confirm=='Yes': #deletes item and associated information if choice is 'Yes'
                del self.overheads[x]
                del self.overhead_cost[x]
                print '\n'
                
                level=7
                prompt= 'Would you like to delete another?'
                delete_another=input_check.check(level,prompt)
                
            elif confirm=='No': #shows user that item was not deleted if the choice is 'No'
                print self.overheads[x]
                print self.overhead_cost[x]
                
                level=7
                prompt= 'Would you like to delete another?'
                delete_another=input_check.check(level,prompt)           
                
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
        
            print '\n'
            print '\n'.join(self.day)
            b=str.lower(raw_input('What would you like to view?\n'
                                        '\n'))
            while b not in self.day:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.day)
                print '\n'
                b=str.lower(raw_input())
                
            x=self.day.index(b)
            print self.day[x]
            print self.time[x]
            print self.salary[x]
            
            level=7
            prompt= 'Are you sure?'
            confirm=input_check.check(level,prompt)
             
            if confirm=='Yes': #deletes item and associated information if choice is 'Yes'
                del self.overheads[x]
                del self.overhead_cost[x]
                
                level=7
                prompt= 'Would you like to delete another entry?'
                delete_another=input_check.check(level,prompt)
                
            elif confirm=='No': #shows user that item was not deleted if the choice is 'No'
                print self.date[x]
                print self.time[x]
                print self.salary[x]

                level=7
                prompt= 'Would you like to delete another entry?'
                delete_another=input_check.check(level,prompt)
            
    def set_profit(self): #allows user to set a desired profit that is calculated based on overheads and cost of raw materials
        level=5
        prompt= 'Which project are you setting the profit for?'
        choice=input_check.check(level,prompt)
        
        x=projects.index(choice) 
        self.percent_profit[x]= float(('How much profit would you like to make? %')/100) #asks for a percentage and converts to a decimal
        self.profit[x]=self.percent_profit*sum(self.overhead_total+sum(self.item_subtotal)) #calculates the profit in dollars and cents
        
    def view_profit(self): #displays the percentage of profit set for a project and the current equivalent dollar value
        level=5
        prompt= 'Which project are you inquiring about?'
        choice=input_check.check(level,prompt)
        x=projects.index(choice)    
        print 'Profit '+'('+self.percent_profit[x]+')'+'% = $'+self.profit[x]
    
    def calc_project_total(self): #shows the user how much he should sell the project for
        level=5
        prompt= 'Which project are you inquiring about?'
        choice=input_check.check(level,prompt)
        x=projects.index(choice)
        #calculate & display updated project total                                    
        project_total[x]= (sum(self.item_subtotal)+sum(self.overhead_cost)+sum(self.salary)+self.profit)
        print 'Sell this project for $'+project_total(x)
