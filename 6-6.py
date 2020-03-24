favorite_languages = {'jen': 'python','sarah': 'c',
                      'edward': 'ruby','phil': 'python',}
surveys=['jen','Bob','edward','raul']
for survey in surveys:
    if survey in favorite_languages.keys():
        print('Hello,%s. Thank you for joining the survey.'%survey.title())
    else:
        print('Hello,%s. Would you like to join the survey?'%survey.title())
