#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv
import os
import requests
from bs4 import BeautifulSoup
import commands


ADDRESS = 'http://reflora.jbrj.gov.br'


def languages_available(soup):
    ''' '''
    languages = tuple(commands.languages_available.languages_available(soup))
    language_names = map(commands.languages_available.language_name, languages)
    for lang, lang_name in zip(languages, language_names):
        print(f'{lang} - {lang_name}')
    print(end='\n')

    return languages, language_names

def mkdir(pathname):
    ''' '''
    os.makedirs(pathname, exist_ok=True)
    return os.path.isdir(pathname)

def languages_available_save(languages, endpoint):
    ''' '''
    endpointdir = f'{os.getcwd()}/data/{endpoint}'
    filepath = f'{endpointdir}/languages_available.json'

    if not mkdir(endpointdir):
        raise Exception(f'Unable to create directory: {endpointdir}')
    
    if commands.languages_available.save(
        f'{endpointdir}/languages_available.json', *languages):
        print('Available languages saved.')
    else:
        raise Exception(f'''Error. Available languages have not been saved.
Attempted path: {filepath}''')
    
    return True

if __name__ == '__main__':
    url = f'{ADDRESS}/{argv[1]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if argv[2] == 'languages-available':
        languages, language_names = languages_available(soup)
        if len(argv) > 3 and argv[3] == 'save':
            languages_available_save(languages, argv[1])
    if argv[2] == 'translations':
        text = commands.translations.translations(ADDRESS, argv[1])
        if len(argv) > 3 and argv[3] == 'save':
            if commands.translations.save(text, argv[1]):
                print('Translations saved.')
            else:
                raise('Error. Translations couldn\'t be saved.')
    if argv[2] == 'save':
        pass