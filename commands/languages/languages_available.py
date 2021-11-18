'''find_languages module
'''


__all__ = ['languages_available', 'language_name']
__author__ = 'Alexandre Pierre'


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
