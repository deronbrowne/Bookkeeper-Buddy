class inventory:
    name = []
    num_pieces = []
    cost_per_piece = []
    subtotals=[]

    def add_name(self, name):
        self.name.append(name)

    def add_num(self, num):
        self.num_pieces.append(num)
        
    def add_cost(self, cost):
        self.cost_per_piece.append(cost)
               
    def subtotal(self, num, cost):
        self.subtotals.append(float(num)*float(cost))
              
    def add_item(self):
        self.add_name(raw_input('What are you adding? '))
        self.add_num(float(raw_input('How many? ')))
        self.add_cost(float(raw_input('Cost per item? ')))
        x=len(self.num_pieces)
        b=self.num_pieces[x-1]
        x=len(self.cost_per_piece)
        c=self.cost_per_piece[x-1]
        self.subtotals.append(b*c)
          
    def view_item(self):
        print self.name
        x=self.name.index(raw_input('What would you like to edit?\n'
                                   '\n'))
        print self.name[x]
        print self.cost_per_piece[x]
        print self.num_pieces[x]
        print self.subtotals[x]
        
    def edit_item(self):
        print self.name
        x=self.name.index(raw_input('What would you like to edit?\n'
                                   '\n'))
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
        print self.name[x]
        print self.cost_per_piece[x]
        print self.num_pieces[x]
        print self.subtotals[x]
        check=raw_input('Are you sure? Yes/No\n'
                       '\n')
        if check=='Yes':
            del self.name[index]
            del self.cost_per_piece[index]
            del self.num_pieces[index]
            del self.subtotal[index]
        elif check='No':
            print self.name[x]
            print self.cost_per_piece[x]
            print self.num_pieces[x]
            print self.subtotals[x]         
            
        
    def get_inventory_value(self):
        print sum(self.subtotals)
