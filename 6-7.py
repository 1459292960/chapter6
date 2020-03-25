pengwei={'first_name':'wei','last_name':'peng',
         'age':'24','city':'BeiJing'}
pengbin={'first_name':'bin','last_name':'peng',
         'age':'25','city':'Harbin'}
CaoHongqing={'first_name':'Hongqing','last_name':'Cao',
             'age':'24','city':'BeiJing'}
people=[pengwei,pengbin,CaoHongqing]
for person in people:
    Fullname =person['last_name'].title()+person['first_name'].title()
    print('Username:'+ Fullname)
    for item,info in person.items():
        print("\t"+item+':'+info)


