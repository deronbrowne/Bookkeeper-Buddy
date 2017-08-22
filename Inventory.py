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
        check='Yes'
        while check=='Yes':
           self.add_name(raw_input('What are you adding? '))
           self.add_num(float(raw_input('How many? ')))
           self.add_cost(float(raw_input('Cost per item? ')))
           x=len(self.num_pieces)
           b=self.num_pieces[x-1]
           x=len(self.cost_per_piece)
           c=self.cost_per_piece[x-1]
           self.subtotals.append(b*c)
           
           choice=['Yes','No']
           print '\n'.join(choice)
           print '\n'
           check=raw_input('Would you like to add another item?\n'
                            '\n')
           while check not in choice:
               print "Sorry, I didn't get that. Try again"
               print '\n'.join(choice)
               print '\n'                
               check=raw_input('Would you like to add another item?\n'
                               '\n')    
               
        if check=='No':
            pass
        
    def view_inventory(self):   
        x=len(self.name)
        for i in xrange(0,x):
            print 'Name: '      + self.name[i]
            print 'Cost: '      + str(self.cost_per_piece[i])
            print 'Quantity: '  + str(self.num_pieces[i])
            print 'Subtotal: '  + str(self.subtotals[i])
            print '\n'
        print 'Inventory value = $'+str(sum(self.subtotals)) #total value of all the items in the inventory       

    def view_item(self): 
        check='Yes'
        while check=='Yes':
            print self.name #shows user the names of all the options he can choose from
            b=raw_input('What would you like to view?\n'
                                       '\n')
            while b not in self.name:
                print '\n'.join(self.name) #shows user the names of all the options he can choose from
                b=raw_input("I'm sorry, that isn't in your inventory. Try again.\n"
                            'What would you like to view?\n'
                            '\n')
            x=self.name.index(b) #user chooses an option; index recorded                                           '\n')                
            #prints all the information associated with an item of the user's choice                
            print 'Name: ' + self.name[x]
            print 'Cost: ' + str(self.cost_per_piece[x])
            print 'Quantity: ' + str(self.num_pieces[x])
            print 'Subtotal: ' + str(self.subtotals[x])
            check=raw_input('Would you like to view another item?\n'
                                   '\n')
            choice=['Yes','No']
            print '\n'.join(choice)
            print '\n'            
            while check not in choice:
                print "Sorry, I didn't get that. Try again"
                print '\n'.join(choice)
                print '\n'
                check=raw_input('Would you like to view another item?\n'
                        '\n')
                
        if check=='No':
            pass

    def edit_item(self):
        check='Yes'
        while check=='Yes': #while the user wants to keep editing, keep executing the edit code
            print '\n'
            print '\n'.join(self.name) #shows user the names of all the options he can choose from
            b=raw_input('What would you like to edit?\n'
                                           '\n')#user chooses an option from the list of item names 
            while b not in self.name: #while loop to catch errors
                print "I'm sorry, that item isn't in your inventory \n"
                print '\n'.join(self.name)
                print '\n'
                b=raw_input('What would you like to edit?\n'
                                           '\n')#user chooses an option from the list of item names
            
            done='No'
            while done=='No':                            
                x=self.name.index(b) #index recorded
                #print the information that is about to be changed
                print '\n'
                print 'Name: '+ str(self.name[x])
                print 'Quantity: '+ str(self.cost_per_piece[x])
                print 'Price: '+ str(self.num_pieces[x])
                print 'Subtotal: '+ str(self.subtotals[x])
                
                
                options=['Name','Quantity','Price']
                print '\n'.join(options)
                print '\n'
                edit=raw_input('What would you like to change?\n'
                               '\n') #user chooses which part of the information he would like to edit
                #catch all
                while edit not in options:
                    print "I'm sorry, that isn't a recorded property \n"
                    print '\n'.join(options)
                    print '\n'
                    edit=raw_input('What would you like to change?\n'
                               '\n') #user chooses which part of the information he would like to edit    
                
                #depending on user response, a different characteristic (item in relevant list) will be changed                    
                if edit=='Name':
                    self.name[x]=raw_input('What are you changing the name to?\n'
                                          '\n')    
                    b=self.name[x]
                                  
                elif edit=='Quantity':
                    self.num_pieces[x]=float(raw_input('What is the new quantity?\n'
                                          '\n'))
                    self.subtotals[x]=self.num_pieces[x]*self.cost_per_piece[x]

                elif edit=='Price':
                    self.cost_per_piece[x]=float(raw_input('What is the new price?\n'
                                          '\n'))
                    self.subtotals[x]=self.num_pieces[x]*self.cost_per_piece[x]
    
                                           
                check=raw_input('Are you done with this item?\n'
                                '\n')
                choice=['Yes','No']
                while check not in choice: #catch all
                    print "Sorry, I didn't get that. Try again"
                    print '\n'.join(choice)
                    print '\n'                    
                    check=raw_input('Would you like to change something else about this item?\n'
                                    '\n')      

            choice=['Yes','No']
            check=raw_input('Would you like to edit another item?\n' #when user is done with an item, he may move on to editing another
                                    '\n')
            while check not in choice:
                print "Sorry, I didn't get that. Try again"
                print '\n'.join(choice)
                print '\n'
                check=raw_input('Would you like to edit another item?\n'
                                '\n')                       
    
    def delete_item(self):
        check='Yes'
        while check=='Yes':
            print self.name #shows user the names of all the options he can choose from
            b=raw_input('What would you like to delete?\n'
                                           '\n')#user chooses an option from the list of item names 
            while b not in self.name: #while loop to catch errors
                print "I'm sorry, that item isn't in your inventory"
                print self.name
                b=raw_input('What would you like to delete?\n'
                                           '\n')#user chooses an option from the list of item names                             
            #grab index of item to be deleted; print and check before deleting
            x=self.name.index(b) 
            print 'Name: ' + self.name[x]
            print 'Cost: ' + str(self.cost_per_piece[x])
            print 'Quantity: ' + str(self.num_pieces[x])
            print 'Subtotal: ' + str(self.subtotals[x])
            print '\n'
            
            choice=['Yes','No']
            print '\n'.join(choice)
            print '\n'
            check=raw_input('Are you sure?\n'
                           '\n')
            while check not in choice:
                print "Sorry I didn't get that. Try again \n"
                print '\n'.join(choice)
                print '\n' 
                check=raw_input("Are you sure you want to delete this?\n"
               '\n')
            
            if check=='Yes':
                del self.name[x]
                del self.cost_per_piece[x]
                del self.num_pieces[x]
                del self.subtotals[x]
            elif check=='No': #shows user that nothing has been changed
                print 'Name: ' + self.name[x]
                print 'Cost: ' + str(self.cost_per_piece[x])
                print 'Quantity: ' + str(self.num_pieces[x])
                print 'Subtotal: ' + str(self.subtotals[x])
                print '\n'                
                
            choice=['Yes','No']
            print '\n'.join(choice)
            print '\n'
            check=raw_input('Would you like to keep deleting?\n'
                    '\n')
            while check not in choice:
                print "Sorry, I didn't get that. Try again"
                print '\n'.join(choice)
                print '\n'
                check=raw_input("Would you like to keep deleting?\n"
                                        '\n')                
                                   
    def delete_inventory(self):
        choice=['Yes','No']
        print '\n'.join(choice)
        print '\n'
        check=raw_input("Are you sure? 'Yes'/'No' \n"
                        '\n')
        while check not in choice: #while loop to catch errors
            print "I'm sorry, I didn't get that."
            print '\n'.join(choice)
            print '\n'
            check=raw_input('Are you sure you want to delete your inventory?\n'
                                       '\n')        
        if check=='Yes':
          self.name=[]
          self.num_pieces=[]
          self.cost_per_piece=[]
          self.subtotals=[]
        
        elif check=='No':
            self.view_inventory()
        
        
    def get_inventory_value(self): #used if user wants to see the value of his inventory
        print sum(self.subtotals)
