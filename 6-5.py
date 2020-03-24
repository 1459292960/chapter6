river_country={'nile':'egypt','yangtse':'China',
               'Panama canal':'panama'}
for river,country in river_country.items():
    print("The %s runs through %s"%(river.title(),country.title()))
for river in set(river_country.keys()):
    print(river)
for country in set(river_country.values()):
    print(country)
