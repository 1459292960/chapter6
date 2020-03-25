
cities={'Harbin':{'country':'China','population':'1000万','fact':'cold'},
        'glasgow':{'country':'Scotland','population':'60万','fact':'frigid'},
        'amsterdam':{'country':'Netherlands','population':'110万','fact':"beatiful"},}
for city,infos in cities.items():
    print(city)
    for item,info in infos.items():
        print("\t",item+':'+info)
