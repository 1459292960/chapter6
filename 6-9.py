favorite_places={'raul':['Harbin','Qingdao'],
                 'pengbin':['Shenzhen','Shanghai'],
                 'pengwei':['Hangzhou','Beijing']}
for name,places in favorite_places.items():
    print(name)
    for place in places:
        print('\t'+place)