################################
#Inventory
################################
choice=['yes','no']
def yes_no(check):
    check=str.lower(check)
    while check not in choice:
        print "Sorry, I didn't get that. Try again."
        print '\n'.join(choice)
        print '\n'
        check=raw_input()
        check=str.lower(check)
        return check

options=['name','quantity','price']
def edit_item_check(edit):
    edit=str.lower(edit)
    while edit not in options:
        print "I'm sorry, that isn't a recorded property \n"
        print '\n'.join(options)
        print '\n'
        edit=raw_input()
        edit=str.lower(edit)
        return edit


	
################################
#Bookkeeper_Buddy
################################
choices=['inventory', 'projects', 'restock', 'set goal', 'quit']
def main_choices_check(action):
	action=str.lower(action)
	while action not in choices:
         print "Sorry, I didn't get that. Try again. \n"
         print '\n'.join(choices)
         print '\n'
         action=raw_input()
         action=str.lower(action)
         return action

options=['create', 'edit', 'view', 'save & exit']	
def inventory_choices_check(query):
    query=str.lower(query)
    while query not in options:
        print "Sorry, I didn't get that. Try again. \n"
        print '\n'.join(options)
        print '\n'
        query=raw_input()
        query=str.lower(query)
        return query	

sub_options=['add','change','delete','save & exit']	
def edit_inventory_check(sub_query):
    sub_query=str.lower(sub_query)
    while sub_query not in sub_options:
        print "Sorry, I didn't get that. Try again. \n"
        print '\n'.join(sub_options)
        print '\n'
        sub_query=raw_input()
        sub_query=str.lower(sub_query)
        return sub_query

sub_sub_options=['items', 'inventory', 'done']	
def edit_inventory_delete_check(sub_sub_query):
    sub_sub_query=str.lower(sub_sub_query)
    while sub_sub_query not in sub_sub_options:
        print "Sorry, I didn't get that. Try again. \n"
        print '\n'.join(sub_sub_options)
        print '\n'
        sub_sub_query=raw_input()
        sub_sub_query=str.lower(sub_sub_query)
        return sub_sub_query
	
def view_inventory_check(sub_query):
    sub_query=str.lower(sub_query)
    while sub_query not in sub_sub_options:
        print "Sorry, I didn't get that. Try again. \n"
        print '\n'.join(sub_sub_options)
        print '\n'
        sub_query=raw_input()
        sub_query=str.lower(sub_query)
        return sub_query	
