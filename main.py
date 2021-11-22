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
    languages = commands.languages_available.languages_available(soup)
    language_names = map(commands.languages_available.language_name, languages)
    
    return languages, language_names

def languages_available_save(languages, endpoint):
    ''' '''
    endpointdir = f'{os.getcwd()}/data/{endpoint}'
    os.makedirs(endpointdir, exist_ok=True)
    commands.languages_available.save(
        f'{endpointdir}/languages_available.json', *languages)
    if os.path.isfile(f'{endpointdir}/languages_available.json'):
        print('Saved.')
    else:
        print('Error. File have not been saved.')

if __name__ == '__main__':
    url = f'{ADDRESS}/{argv[1]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if argv[2] == 'languages-available':
        languages, language_names = languages_available(soup)
        print(*language_names, sep='\n', end='\n\n')
        if len(argv) > 3 and argv[3] == 'save':
            languages_available_save(languages, argv[1])