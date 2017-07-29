print 'Inventory initialized'
class inventory:
    #initialize lists that will store information about the inventory
    name = []
    num_pieces = []
    cost_per_piece = []
    subtotals=[]

    def add_name(self, name): #adds a name to the list 'name'
        self.name.append(name)

    def add_num(self, num): #adds a corresponding number of items to the list 'num_pieces'
        self.num_pieces.append(num)
        
    def add_cost(self, cost): #adds a corresponding cost to the list 'cost_per_piece'
        self.cost_per_piece.append(cost)
               
    def subtotal(self, num, cost): #adds a corresponding subtotal to the list of 'subtotals'
        self.subtotals.append(float(num)*float(cost))
              
    def add_item(self): #adds an item to the list by saving the name, count, price and 
                        #subtotal of the addition
        self.add_name(raw_input('What are you adding? '))
        self.add_num(float(raw_input('How many? ')))
        self.add_cost(float(raw_input('Cost per item? ')))
        x=len(self.num_pieces)
        b=self.num_pieces[x-1]
        x=len(self.cost_per_piece)
        c=self.cost_per_piece[x-1]
        self.subtotals.append(b*c)
          
    def view_item(self): 
        print self.name #shows user the names of all the options he can choose from
        x=self.name.index(raw_input('What would you like to edit?\n'
                                   '\n')) #user chooses an option; index recorded
        #prints all the information associated with an item of the user's choice                
        print self.name[x]
        print self.cost_per_piece[x]
        print self.num_pieces[x]
        print self.subtotals[x]
        
    def edit_item(self):
        print self.name #shows user the names of all the options he can choose from
        x=self.name.index(raw_input('What would you like to edit?\n'
                                   '\n')) #user chooses an option; index recorded
        print self.name[x]
        print self.cost_per_piece[x]
        print self.num_pieces[x]
        print self.subtotals[x]
        
        edit=raw_input('What would you like to change?\n'
                       'a "Name"\n'
                       'a "Quantity"\n'
                       'or a "Price"?\n'
                       '\n')
        if edit=='Name':
            self.name[x]=raw_input('What are you changing the name to?\n'
                                  '\n')
        elif edit=='Quantity':
            self.num_pieces[x]=float(raw_input('What is the new quantity?\n'
                                  '\n'))
            self.subtotals[x]=self.num_pieces[x]*self.cost_per_piece[x]
        elif edit=='price':
            self.cost_per_piece[x]=float(raw_input('What is the new price?\n'
                                  '\n'))
            self.subtotals[x]=self.num_pieces[x]*self.cost_per_piece[x]
        else:
            print "I'm sorry, that item isn't in your inventory"
            print self.name
    
    def delete_item(self):
        print self.name
        x=self.name.index(raw_input('What would you like to delete?\n'
                                   '\n'))
        if x in self.name:
            print self.name[x]
            print self.cost_per_piece[x]
            print self.num_pieces[x]
            print self.subtotals[x]
            check=raw_input('Are you sure? Yes/No\n'
                           '\n')
            if check=='Yes':
                del self.name[x]
                del self.cost_per_piece[x]
                del self.num_pieces[x]
                del self.subtotal[x]
            elif check=='No':
                print self.name[x]
                print self.cost_per_piece[x]
                print self.num_pieces[x]
                print self.subtotals[x]
        else:
            print "I'm sorry, that item isn't in your inventory"
            print self.name          
        
    def get_inventory_value(self):
        print sum(self.subtotals)