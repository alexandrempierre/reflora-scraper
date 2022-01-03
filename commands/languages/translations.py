'''translations module
'''


__all__ = ['translations', 'save']
__author__ = 'Alexandre Pierre'


import os
import itertools
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString


def end_node(tag):
  '''Indentify a leaf of the tree that represents the web page.'''
  if tag.name in {'style', 'script'}:
    return False
  if not tag.text:
    return False
  if len(tag.find_all(text=False)) > 0:
    return False
  if isinstance(tag, NavigableString):
    return False
  
  return True

def find_leaves_texts(soup):
  ''' '''
  return map(lambda el: el.getText().strip(), soup.find_all(end_node))

def read_languages(endpoint):
  ''' '''
  filepath = f'{os.getcwd()}/data/{endpoint}/languages_available.json'
  if not os.path.isfile(filepath):
    raise Exception('No languages available file.')
  with open(filepath, 'r', encoding='ASCII') as file_ptr:
    languages = file_ptr.read().split('\n')
  return languages

def translations(address, endpoint):
  ''' '''
  languages = read_languages(endpoint)
  text = dict()
  for lang in languages:
    resp = requests.get(f'{address}/{endpoint}?lingua={lang}')
    soup = BeautifulSoup(resp.text, 'html.parser')
    text[lang] = find_leaves_texts(soup)
  
  return text

def save(text_dict, endpoint):
  ''' '''
  filepath = f'{os.getcwd()}/data/{endpoint}/translations.csv'
  with open(filepath, 'w') as file_ptr:
    header = True
    for row in itertools.zip_longest(*text_dict.values(), fillvalue=''):
      filerow = f'"{endpoint}"\t"' + '"\t"'.join(row) + '"\n\r'
      file_ptr.write(filerow)

  return os.path.isfile(filepath)