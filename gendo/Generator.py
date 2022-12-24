
import yaml
import os

class Generator():
    def __get_key__(self, key: str):
        path = os.getcwd() + '/gendo.yml'
        lang = yaml.full_load(open(path))
        return lang[key]

    def __get_lang_conf__(self):
        lang = self.__get_key__('lang')
        lang_info = {}

        
        lang_info['config'] = f'{lang}.yml'
        lang_info['templ_name'] = f'{lang}.j2'
        lang_info['needs_webserver'] = False
        
        if lang == 'angular' or lang == 'react':
            lang_info['needs_webserver'] = True
        return lang_info
