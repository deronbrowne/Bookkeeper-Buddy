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
        
    def edit_item(self,index):
        print self.name[index]
        print self.cost_per_piece[index]
        print self.num_pieces[index]
        print self.subtotals[index]
        edit=raw_input('Would you like to change a "quantity" or a "price"? ')
        if edit=='quantity':
            #how do I edit a list that is defined within a class?
            del self.num_pieces[index]
            self.num_pieces.insert(index,float(raw_input('New quantity: ')))
            self.subtotals[x]=inventory.num_pieces[index]*inventory.cost_per_piece[index]
        elif edit=='price':
            #how do I edit a list that is defined within a class?
            del self.cost_per_piece[index]
            self.cost_per_piece.insert(index,float(raw_input('New cost: ')))
            self.subtotals[index]=self.num_pieces[index]*self.cost_per_piece[index]
        else:
            print "I'm sorry, that item isn't in your inventory"
            print self.name
    
    def view_item(self,index):
        print self.name[index]
        print self.cost_per_piece[index]
        print self.num_pieces[index]
        print self.subtotal[index]
        
    def delete_item(self,index):
        del self.name[index]
        del self.cost_per_piece[index]
        del self.num_pieces[index]
        del self.subtotal[index]
        
    def get_inventory_value(self):
        print sum(self.subtotals)
