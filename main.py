#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv
import requests
from bs4 import BeautifulSoup
import commands
import commands.languages

ADDRESS = 'http://reflora.jbrj.gov.br'


if __name__ == '__main__':
    url = f'{ADDRESS}/{argv[1]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if argv[2] == 'languages-available':
        languages = map(
            commands.languages.language_name, 
            commands.languages_available(soup))
        print(*languages, sep='\n')
