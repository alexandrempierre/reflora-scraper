'''languages_available module

Module containing the code corresponding to languages-available subcommand.
'''


__all__ = ['languages_available', 'language_name', 'save']
__author__ = 'Alexandre Pierre'


import json


LANGUAGES = {
        'pt': 'Português 🇧🇷',
        'es': 'Espanhol 🇪🇸',
        'en': 'Inglês 🇺🇸',
        'fr': 'Francês 🇫🇷'}

def language_name(abbr, abbr2name=None):
    '''Given a language abbreviation returns the language name and a flag.'''
    if abbr2name is None:
        abbr2name = LANGUAGES

    return abbr2name[abbr.lower()]


def languages_available(soup):
    '''Returns the languages in which the page is available.'''
    return map(
        lambda li: li.getText().strip(),
        soup.find('ul', {'class': 'nav idioma'}).find_all(
            'li', {'class': 'submenu'}))

def save(filename, *languages):
    '''Save the languages passed as arguments.'''
    with open(filename, 'w') as file_ptr:
        json.dump([{'lingua': lang.lower()} for lang in languages], file_ptr)