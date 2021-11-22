'''languages_available module

Module containing the code corresponding to languages-available subcommand.
'''


__all__ = ['languages_available', 'language_name']
__author__ = 'Alexandre Pierre'


import json


LANGUAGES = {
        'PT': 'Português 🇧🇷',
        'ES': 'Espanhol 🇪🇸',
        'EN': 'Inglês 🇺🇸',
        'FR': 'Francês 🇫🇷'}

def language_name(abbr, abbr2name=None):
    ''' '''
    if abbr2name is None:
        abbr2name = LANGUAGES

    return abbr2name[abbr]


def languages_available(soup):
    ''' '''
    return map(
        lambda li: li.getText().strip(),
        soup.find('ul', {'class': 'nav idioma'}).find_all(
            'li', {'class': 'submenu'}))

def save(filename, *values):
    ''' '''
    with open(filename, 'w') as file_ptr:
        json.dump([{'lingua': value.lower()} for value in values], file_ptr)