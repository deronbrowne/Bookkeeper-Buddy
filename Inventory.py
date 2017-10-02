import input_check
inventory_record={}

class inventory:
    #initialize lists that will store information about the inventory
    def __init__ (self):    
        self.name = []
        self.num_pieces = []
        self.cost_per_piece = []
        self.subtotals=[]

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
        check='yes'
        while check=='yes':
           self.add_name(raw_input('What are you adding? '))
           self.add_num(float(raw_input('How many? ')))
           self.add_cost(float(raw_input('Cost per item? ')))
           x=len(self.num_pieces)
           b=self.num_pieces[x-1]
           x=len(self.cost_per_piece)
           c=self.cost_per_piece[x-1]
           self.subtotals.append(b*c)
           
           level=7
           prompt= 'Would you like to add another item?'
           check=input_check.check(level,prompt)
        
    def view_inventory(self):   
        x=len(self.name)
        for i in xrange(0,x):
            print 'Name: '      + self.name[i]
            print 'Cost: $'      + str(self.cost_per_piece[i])
            print 'Quantity: '  + str(self.num_pieces[i])
            print 'Subtotal: $'  + str(self.subtotals[i])
            print '\n'
        print 'Inventory value = $'+str(sum(self.subtotals)) #total value of all the items in the inventory       

    def view_item(self): 
        check='yes'
        while check=='yes':
            print '\n'
            print '\n'.join(self.name)
            b=str.lower(raw_input('What would you like to view?\n'
                                        '\n'))
            while b not in self.name:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.name)
                print '\n'
                b=str.lower(raw_input())            

            x=self.name.index(b) #user chooses an option; index recorded              
            #prints all the information associated with an item of the user's choice                
            print 'Name: ' + self.name[x]
            print 'Cost: $' + str(self.cost_per_piece[x])
            print 'Quantity: ' + str(self.num_pieces[x])
            print 'Subtotal: $' + str(self.subtotals[x])
            level=7
            prompt= 'Would you like to view another item?'
            check=input_check.check(level,prompt) 

    def edit_item(self):
        check='yes'
        while check=='yes': #while the user wants to keep editing, keep executing the edit code
            print '\n'
            print '\n'.join(self.name)
            b=str.lower(raw_input('What would you like to edit?\n'
                                        '\n'))
            while b not in self.name:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.name)
                print '\n'
                b=str.lower(raw_input()) 
            
            done='no'
            while done=='no':                            
                x=self.name.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.name[x])
                print 'Quantity: '+ str(self.num_pieces[x])
                print 'Price: $'+ str(self.cost_per_piece[x])
                print 'Subtotal: $'+ str(self.subtotals[x])
                
                
                level=9
                prompt= 'What would you like to change?'
                edit=input_check.check(level,prompt)   
                
                #depending on user response, a different characteristic (item in relevant list) will be changed                    
                if edit=='name':
                    self.name[x]=raw_input('What are you changing the name to?\n'
                                          '\n')    
                    b=self.name[x]
                                  
                elif edit=='quantity':
                    self.num_pieces[x]=float(raw_input('What is the new quantity?\n'
                                          '\n'))
                    self.subtotals[x]=self.num_pieces[x]*self.cost_per_piece[x]

                elif edit=='price':
                    self.cost_per_piece[x]=float(raw_input('What is the new price?\n'
                                          '\n'))
                    self.subtotals[x]=self.num_pieces[x]*self.cost_per_piece[x]
    
                                           
                level=7
                prompt= 'Are you done with this item?'
                done=input_check.check(level,prompt)     

            if done=='yes':                            
                x=self.name.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.name[x])
                print 'Quantity: '+ str(self.num_pieces[x])
                print 'Price: $'+ str(self.cost_per_piece[x])
                print 'Subtotal: $'+ str(self.subtotals[x])
                
            level=7
            prompt= 'Would you like to edit another item?'
            check=input_check.check(level,prompt)                       
    
    def delete_item(self):
        check='yes'
        while check=='yes':
            print '\n'
            print '\n'.join(self.name)
            b=str.lower(raw_input('What would you like to view?\n'
                                        '\n'))
            while b not in self.name:
                print "Sorry, that isn't a valid choice. Try again."
                print '\n'.join(self.name)
                print '\n'
                b=str.lower(raw_input()) 
                             
            #grab index of item to be deleted; print and check before deleting
            x=self.name.index(b) 
            print 'Name: ' + self.name[x]
            print 'Cost: $' + str(self.cost_per_piece[x])
            print 'Quantity: ' + str(self.num_pieces[x])
            print 'Subtotal: $' + str(self.subtotals[x])
            print '\n'
            
            level=7
            prompt= 'Are you sure?'
            check=input_check.check(level,prompt)
            
            if check=='yes':
                del self.name[x]
                del self.cost_per_piece[x]
                del self.num_pieces[x]
                del self.subtotals[x]
                
            elif check=='no': #shows user that nothing has been changed
                print 'Name: ' + self.name[x]
                print 'Cost: $' + str(self.cost_per_piece[x])
                print 'Quantity: ' + str(self.num_pieces[x])
                print 'Subtotal: $' + str(self.subtotals[x])
                print '\n'                

            level=7
            prompt= 'Would you like to keep deleting?'
            check=input_check.check(level,prompt)           
                                   
    def delete_inventory(self, inventory):
        level=7
        prompt= 'Are you sure?'
        check=input_check.check(level,prompt)
        
        if check=='yes':
            del inventory_record[inventory]
        
        elif check=='no':
            self.view_inventory()
        
        
    def get_inventory_value(self): #used if user wants to see the value of his inventory
        print sum(self.subtotals)
