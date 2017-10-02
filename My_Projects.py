#initialize lists to keep track of all the projects, their totals
#and to track which inctances of the class "my_projects correspond to each title
import input_check
projects={}

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
        #lists to record information about the overhead costs associated with this project    
        self.overheads=[]
        self.overhead_cost=[]
        #lists to record information for paying yourself   
        self.day=[]
        self.time=[]
        self.salary=[]
        #lists to record information about the profit
        self.percent_profit=20
        level=7
        prompt= 'Your default percentage profit has been set to 20%. Would you like to change it?'
        add_another=input_check.check(level,prompt)
        if add_another=='yes':
            self.hourly_rate=raw_input('What would you like to change it to?')        
    
#####################################################################################
#handling project items
#####################################################################################    
    def add_item(self): #adding items to the project
        add_another='yes'
        while add_another=='yes':#allows user to add multiple items
            self.items.append(raw_input('What are you adding?\n'))
            self.item_cost.append(float(raw_input('How much does it cost?\n')))
            self.item_count.append(float(raw_input('How many are you adding?\n')))
            a=self.item_cost[len(self.item_cost)-1] #grabs the value of the last added item
            b=self.item_count[len(self.item_count)-1] #grabs the count of the last added item
            self.item_subtotal.append(a*b) #calculates the total cost for all of a particular item  
            
            level=7
            prompt= 'Would you like to add another item?'
            add_another=input_check.check(level,prompt)
            
    def edit_item(self):
        check='yes'
        while check=='yes': #while the user wants to keep editing, keep executing the edit code
            print '\n'
            print '\n'.join(self.items)
            b=str.lower(raw_input('What would you like to edit?\n'
                                        '\n'))
            while b not in self.items:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.items)
                print '\n'
                b=str.lower(raw_input()) 
            
            done='no'
            while done=='no':                            
                x=self.items.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.items[x])
                print 'Quantity: '+ str(self.item_count[x])
                print 'Price: '+ str(self.item_cost[x])
                print 'Subtotal: '+ str(self.item_subtotal[x])
                
                
                level=9
                prompt= 'What would you like to change?'
                edit=input_check.check(level,prompt)   
                
                #depending on user response, a different characteristic (item in relevant list) will be changed                    
                if edit=='name':
                    self.items[x]=raw_input('What are you changing the name to?\n'
                                          '\n')    
                    b=self.items[x]
                                  
                elif edit=='quantity':
                    self.item_count[x]=float(raw_input('What is the new quantity?\n'
                                          '\n'))
                    self.subtotals[x]=self.item_count[x]*self.item_cost[x]

                elif edit=='price':
                    self.item_cost[x]=float(raw_input('What is the new price?\n'
                                          '\n'))
                    self.subtotals[x]=self.item_count[x]*self.item_cost[x]
    
                                           
                level=7
                prompt= 'Are you done with this item?'
                done=input_check.check(level,prompt)   
                
            if done=='yes':                            
                x=self.items.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.items[x])
                print 'Quantity: '+ str(self.item_count[x])
                print 'Price: $'+ str(self.item_cost[x])
                print 'Subtotal: $'+ str(self.item_subtotal[x])                

            level=7
            prompt= 'Would you like to edit another item?'
            check=input_check.check(level,prompt)                                   
        
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
        delete_another='yes'
        while delete_another=='yes':#allows user to delete multiple items
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
              
            if confirm=='yes': #deletes item and associated information if choice is 'Yes'
                del self.items[x]
                del self.item_cost[x]
                del self.item_count[x]
                del self.item_subtotal[x]
                
                level=7
                prompt= 'Would you like to delete another item?'
                delete_another=input_check.check(level,prompt)                                           
                
            elif confirm=='no': #shows user that item was not deleted if the choice is 'No'
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
        add_another='yes'
        while add_another=='yes':
            self.overheads.append(raw_input('What are you adding?\n'))
            self.overhead_cost.append(float(raw_input('How much does it cost?\n')))
            
            level=7
            prompt= 'Would you like to add another?'
            add_another=input_check.check(level,prompt)  
                
        if add_another=='no':
            self.view_overheads()
            
    def edit_overheads(self):
        check='yes'
        while check=='yes': #while the user wants to keep editing, keep executing the edit code
            print '\n'
            print '\n'.join(self.overheads)
            b=str.lower(raw_input('What would you like to edit?\n'
                                        '\n'))
            while b not in self.overheads:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.overheads)
                print '\n'
                b=str.lower(raw_input()) 
            
            done='no'
            while done=='no':                            
                x=self.overheads.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.overheads[x])
                print 'Price: $'+ str(self.overhead_cost[x])
                
                
                level=8
                prompt= 'What would you like to change?'
                edit=input_check.check(level,prompt)   
                
                #depending on user response, a different characteristic (item in relevant list) will be changed                    
                if edit=='name':
                    self.overheads[x]=raw_input('What are you changing the name to?\n'
                                          '\n')    
                    b=self.overheads[x]
                                  
                elif edit=='price':
                    self.overhead_cost[x]=float(raw_input('What is the new price?\n'
                                          '\n'))  
                                           
                level=7
                prompt= 'Are you done with this overhead?'
                done=input_check.check(level,prompt)

            if done=='yes':                            
                x=self.items.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.overheads[x])
                print 'Price: $'+ str(self.overhead_cost[x])
                print 'Subtotal: $'+ str(self.overheads[x]*self.overhead_cost[x])                  

            level=7
            prompt= 'Would you like to edit another overhead?'
            check=input_check.check(level,prompt)            
        
    def view_overheads(self,a):#view all the information on overheads
        x=len(self.overheads)-1
        for index in range(1,x):
            print self.overheads[index]
            print self.overhead_cost[index]
            print '\n'#shows each overhead and the associated cost
        print 'Total overhead = ' + sum(self.overhead_cost) #shows total cost of overheads
        
    def delete_overhead(self):
        delete_another='yes'
        while delete_another=='yes':#allows user to delete multiple items
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
              
            if confirm=='yes': #deletes item and associated information if choice is 'Yes'
                del self.overheads[x]
                del self.overhead_cost[x]
                print '\n'
                
                level=7
                prompt= 'Would you like to delete another?'
                delete_another=input_check.check(level,prompt)
                
            elif confirm=='no': #shows user that item was not deleted if the choice is 'No'
                print self.overheads[x]
                print self.overhead_cost[x]
                
                level=7
                prompt= 'Would you like to delete another?'
                delete_another=input_check.check(level,prompt)           
                
#####################################################################################
#handling hours worked and salary
#####################################################################################             
    def log_hours(self): #allows user to record the number of hours worked and the value of that time based on his hourly rate
        keep_adding='yes'
        while keep_adding=='yes':
            self.day.append(raw_input('What date are you adding hours for?\n'))
            self.time.append(float(raw_input('How many hours did you work?\n')))
            a=self.time[len(self.time)-1]
            self.salary.append(a*self.hourly_rate)
            
            level=7
            prompt= 'Would you like to keep adding?'
            keep_adding=input_check.check(level,prompt)
            
        if keep_adding=='no':
            self.view_hours
            
    def edit_hours(self):
        check='yes'
        while check=='yes': #while the user wants to keep editing, keep executing the edit code
            print '\n'
            print '\n'.join(self.day)
            b=str.lower(raw_input("Which date's entries would you like to edit?\n"
                                        '\n'))
            while b not in self.day:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.day)
                print '\n'
                b=str.lower(raw_input()) 
            
            done='no'
            while done=='no':                            
                x=self.day.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Date: '+ str(self.day[x])
                print 'Time: $'+ str(self.time[x])
                print 'Hourly rate: $'+ str(self.hourly_rate[x])
                print 'Pay: $'+ str(self.salary[x])                
                
                
                level=10
                prompt= 'What would you like to change?'
                edit=input_check.check(level,prompt)   
                
                #depending on user response, a different characteristic (item in relevant list) will be changed                    
                if edit=='date':
                    self.day[x]=raw_input('What are you changing the date to?\n'
                                          '\n')    
                    b=self.day[x]
                                  
                elif edit=='time':
                    self.overhead_cost[x]=float(raw_input('What is the new price?\n'
                                          '\n'))

                elif edit=='hourly rate':
                    self.hourly_rate[x]=float(raw_input('What is your new hourly rate?\n'
                                          '\n'))                                           
                                           
                level=7
                prompt= 'Are you done with this item?'
                done=input_check.check(level,prompt)

            if done=='yes':                            
                x=self.items.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Date: '+ str(self.day[x])
                print 'Time: $'+ str(self.time[x])
                print 'Hourly rate: $'+ str(self.hourly_rate[x])
                print 'Pay: $'+ str(self.salary[x])                 

            level=7
            prompt= 'Would you like to edit another date?'
            check=input_check.check(level,prompt)               
        
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
                
#####################################################################################
#handling profit
#####################################################################################                  
            
    def set_profit(self): #allows user to set a desired profit that is calculated based on overheads and cost of raw materials
        self.percent_profit= float(('How much profit would you like to make? %')/100) #asks for a percentage and converts to a decimal
        
    def view_profit(self): #displays the percentage of profit set for a project and the current equivalent dollar value   
        print 'Profit '+'('+self.percent_profit +')'+'% = $'+self.percent_profit*sum(self.overhead_total+sum(self.item_subtotal))
        
    def delete_profit(self):
        self.percent_profit=float(0)
    
    def calc_project_total(self): #shows the user how much he should sell the project for
        #calculate & display updated project total                                    
        project_total= sum(self.item_subtotal)+sum(self.overhead_cost)+sum(self.salary)+(self.percent_profit*sum(self.overhead_total+sum(self.item_subtotal)))
        print 'Sell this project for $'+ project_total
