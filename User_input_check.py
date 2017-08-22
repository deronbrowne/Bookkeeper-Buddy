################################
#Inventory
################################
def yes_no(check):
	str.lower(check)
	choice=['yes','no']
 	while check not in choice:
		print "Sorry, I didn't get that. Try again."
		print '\n'.join(choice)
		print '\n'
		check=raw_input()
		return check


def edit_item_check(edit):
	str.lower(edit)
	options=['name','quantity','price']
	while edit not in options:
		print "I'm sorry, that isn't a recorded property \n"
		print '\n'.join(options)
		print '\n'
		edit=raw_input()
		return edit


	
################################
#Bookkeeper_Buddy
################################
def main_choices_check(action):
	str.lower(action)
	choices=['inventory', 'projects', 'restock', 'set goal', 'quit']
	while action not in choices:
		print "Sorry, I didn't get that. Try again. \n"
		print '\n'.join(choices)
		print '\n'
		action=raw_input()
		return action
	
def inventory_choices_check(query):
	str.lower(query)
	options=['create', 'edit', 'view', 'save & exit']
	while query not in options:
		print "Sorry, I didn't get that. Try again. \n"
		print '\n'.join(options)
		print '\n'
		query=raw_input()
		return query	
	
def edit_inventory_check(sub_query):
	str.lower(sub_query)
	sub_options=['add','change','delete','save & exit']
	while sub_query not in sub_options:
		print "Sorry, I didn't get that. Try again. \n"
		print '\n'.join(sub_options)
		print '\n'
		sub_query=raw_input()
		return sub_query
	
def edit_inventory_delete_check(sub_sub_query):
	str.lower(sub_sub_query)
	sub_sub_options=['items', 'inventory', 'done']
	while sub_sub_query not in sub_sub_options:
		print "Sorry, I didn't get that. Try again. \n"
		print '\n'.join(sub_sub_options)
		print '\n'
		sub_sub_query=raw_input()
		return sub_sub_query
	
def view_inventory_check(sub_query):
	str.lower(sub_query)
	sub_options=['items','inventory','done']
	while sub_query not in sub_options:
		print "Sorry, I didn't get that. Try again. \n"
		print '\n'.join(sub_options)
		print '\n'
		sub_query=raw_input()
		return sub_query	
