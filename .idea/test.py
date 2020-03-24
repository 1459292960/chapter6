alien_0={'color':'green','points':5,'x_position':0,
         'y_pisition':25,'speed':'medium'}
if alien_0['speed'] == 'slow':
    x_increment=1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment

favorite_languages = {'jen': 'python','sarah': 'c',
                      'edward': 'ruby','phil': 'python',}
for value in set(favorite_languages.values()):
    print(value.title())
