from gendo.Generator import Generator as g
from jinja2 import Environment, FileSystemLoader
import os

DIR = f'{os.getcwd()}/ci_files'

class DockerfileGen(g):
    def create_dockerfile(self):
        conf = self.__get_lang_conf__()
        if conf['needs_webserver']:
            env = Environment(loader = FileSystemLoader('templates'),   
                    trim_blocks=True, lstrip_blocks=True)
            template = env.get_template('nginx.j2')
                
            file=open(f"{DIR}/nginx.conf", "w")  
            file.write(template.render())  
            file.close()
        name = self.__get_key__('project_name')
        keys = {}
        keys['project_name'] = name
        env = Environment(loader = FileSystemLoader('templates/dockerfiles'),   
                        trim_blocks=True, lstrip_blocks=True)

        template = env.get_template(conf['templ_name'])
        
        file=open(f"{DIR}/Dockerfile", "w")
        file.write(template.render(keys))
        file.close
            
class GitlabGen(g):
    def create_ci_file(self):
        keys = self.__get_key__('gitlab-ci')
        name = self.__get_key__('project_name')
        lang = self.__get_key__('lang')
        keys["project_name"] = name
        keys["lang"] = lang
        env = Environment(loader = FileSystemLoader('templates'),   
                trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('ci.j2')
        file=open(f"{DIR}/.gitlab-ci.yml", "w")  
        file.write(template.render(keys))  
        file.close()