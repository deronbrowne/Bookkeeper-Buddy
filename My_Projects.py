print 'My_Projects initialized'

projects=[]
instances=[]
project_total=[]
#hourly_rate=float(raw_input('What is your hourly rate? '))

class my_projects:
    items=[]
    item_cost=[]
    item_count=[]
    item_subtotal=[]
    overheads=[]
    overhead_cost=[]
    day=[]
    time=[]
    salary=[]
    percent_profit=[]
    profit=[]
    
    def add_item(self):
        question='Add another'
        while question=='Add another':
            name=raw_input('What are you adding?\n')
            cost=raw_input('How much does it cost?\n')
            count=raw_input('How many are you adding?\n')
            self.items.append(name)
            self.item_cost.append(cost)
            self.item_count.append(count)
            a=float(self.item_cost[len(self.item_cost)-1])
            b=float(self.item_count[len(self.item_count)-1])
            self.item_subtotal.append(a*b)
            question=raw_input('Would you like to:\n'
            '"Save"\n'
            'or"Add another\n'
            '\n')
        
    def view_items(self):
        x=len(self.items)-1
        for index in range(1,x):
            print self.items[index], self.item_cost[index], self.item_count[index], self.item_subtotal[index]
        print 'Subtotal for this project = $'+sum(self.item_subtotal)
        
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
