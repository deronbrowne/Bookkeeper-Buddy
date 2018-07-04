def check(level,prompt):

    a=['inventory', 'projects', 'restock', 'set goal', 'quit']
    b=['create', 'edit', 'view', 'save & exit']
    c=['add','change','delete','save & exit']	
    d=['inventory', 'items', 'done']
    import My_Projects
    f=['items','overheads','hours','profit','done']
    g=['yes','no']
    h=['name','price']
    import Inventory
    i=['name','quantity','price']
    j=['date','time']
    m=Inventory.inventory_record.keys()
    n=My_Projects.projects.keys()

    if level==1:
        options=a
    elif level==2:
        options=b
    elif level==3:
        options=c
    elif level==4:
        options=d
    elif level==6:
        options=f
    elif level==7:
        options=g
    elif level==8:
        options=h        
    elif level==9:
        options=i
    elif level==10:
        options=j         
    elif level==13:
        options=m
    elif level==14:
        options=n
        
    print ('\n')
    print ('\n'.join(options))
    choice=str.lower(input(prompt + '\n'
                                '\n'))
    while choice not in options:
        print ("Sorry, that isn't a valid choice. Try again.")
        print ('\n'.join(options))
        print ('\n')
        choice=str.lower(input())
    
    return choice
