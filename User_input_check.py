def yes_no(check):
	str.lower(check)
	choice=['yes','no']
 	print '\n'.join(choice)
 	print '\n'
 	while check not in choice:
		print "Sorry, I didn't get that. Try again"
		print '\n'.join(choice)
		print '\n'
		check=raw_input()
		return check


def edit_item_check(edit):
	str.lower(edit)
	options=['name','quantity','price']
	print '\n'.join(options)
	print '\n'
	while edit not in options:
		print "I'm sorry, that isn't a recorded property \n"
		print '\n'.join(options)
		print '\n'
		edit=raw_input()
		return edit