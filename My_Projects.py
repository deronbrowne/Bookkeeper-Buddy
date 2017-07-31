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
    
    def add_item(self): #adding items to the project
        question='Add another'
        while question=='Add another':#allows user to add multiple items
            self.items.append(raw_input('What are you adding?\n'))
            self.item_cost.append(float(raw_input('How much does it cost?\n')))
            self.item_count.append(float(raw_input('How many are you adding?\n')))
            a=self.item_cost[len(self.item_cost)-1] #grabs the value of the last added item
            b=self.item_count[len(self.item_count)-1] #grabs the count of the last added item
            self.item_subtotal.append(a*b) #calculates the total cost for all of a particular item
            question=raw_input('Would you like to:\n'
            '"Save"\n'
            'or"Add another\n'
            '\n')
            if question!='Save' or question!='Add another': #catch all
                print "Sorry, that isn't an option.\n"
                question=raw_input('Would you like to:\n'
                '"Save"\n'
                'or"Add another\n'
                '\n')         
        
    def view_items(self): #view all the information on project items
        x=len(self.items)-1
        for index in range(1,x):
            print self.items[index], self.item_cost[index], self.item_count[index], self.item_subtotal[index]
        print 'Subtotal for this project = $'+sum(self.item_subtotal) #total value of all the items in the project
        
    def delete_items(self):
        self.view_hours()
        x=raw_input('What date would you like to delete?\n')
        del self.items[x]
        del self.item_cost[x]
        del self.item_count[x]
        del self.item_subtotal[x]        
        
    def add_overhead_item(self):
        name=raw_input('What are you adding?\n')
        cost=raw_input('How much does it cost?\n')
        self.overheads.append(name)
        self.overhead_cost.append(cost)
        
    def view_overheads(self,a):
        x=len(self.overheads)-1
        for index in range(1,x):
            print self.overheads[index], self.overhead_cost[index]
        print 'Total overhead = ' + sum(self.overhead_cost)
        
    def delete_overhead(self):
        self.delete_overhead()
        x=raw_input('What date would you like to delete?\n')
        del self.overheads[x]
        del self.overhead_cost[x]
            
    def log_hours(self):
        self.day.append(raw_input('What date are you adding hours for?\n'))
        self.time.append(raw_input('How many hours did you work?\n'))
        a=float(self.hours[len(self.hours)-1])
        self.salary.append(a*self.hourly_rate)
        
    def view_hours(self):
        x=len(self.hours)-1
        print 'Hourly rate = $'+self.hourly_rate
        for index in range(1,x):
            print self.date[index], self.hours[index], self.salary[index]
        print 'Salary for this project = $'+sum(self.salary)
        
    def delete_hours(self):
        self.view_hours()
        x=raw_input('What date would you like to delete?\n')
        del self.day[x]
        del self.time[x]
        del self.salary[x]
            
    def set_profit(self):
        self.percent_profit = float(('How much profit would you like to make? %')/100)
        self.profit=self.percent_profit*sum(self.overhead_total+sum(self.item_subtotal))
        
    def view_profit(self):
        print 'Profit '+'('+self.percent_profit+')'+'% = $'+self.profit
    
    def calc_project_total(self):
        print projects
        x=raw_input('Which project are you inquiring about?\n')
        del project_total[x]
        project_total.insert(x,(sum(self.item_subtotal)+sum(self.overhead_cost)+sum(self.salary)+self.profit))
        print 'Sell this project for $'+project_total(x)
