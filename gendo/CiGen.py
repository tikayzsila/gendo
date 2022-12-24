from gendo.Generator import Generator as g
from jinja2 import Environment, FileSystemLoader
import os

DIR = f'{os.getcwd()}/ci_files'
DIR_ROLE = f'{os.getcwd()}/role'

class DockerfileGen(g):
    def create_dockerfile(self):
        conf = self.__get_lang_conf__()
        name = self.__get_key__('project_name')
        keys = {}
        keys['project_name'] = name
        env = Environment(loader = FileSystemLoader('templates/dockerfiles'),   
                        trim_blocks=True, lstrip_blocks=True)

        template = env.get_template(conf['templ_name'])
        
        file=open(f"{DIR}/Dockerfile", "w")
        file.write(template.render(keys))
        file.close

class ComposeGen(g):
    def check_webserver(self):
        conf = self.__get_lang_conf__()
        if conf['needs_webserver']:
            env = Environment(loader = FileSystemLoader('templates'),   
                    trim_blocks=True, lstrip_blocks=True)
            template = env.get_template('nginx.j2')
                
            file=open(f"{DIR}/nginx.conf", "w")  
            file.write(template.render())  
            file.close()

    def gen_compose_file(self):
        conf = self.__get_lang_conf__()
        name = self.__get_key__('project_name')
        keys = self.__get_key__('compose')
        keys['project_name'] = name

        
        env = Environment(loader = FileSystemLoader('templates/compose'),   
                trim_blocks=True, lstrip_blocks=True)
        template = env.get_template(conf['templ_name'])

        file=open(f'{DIR}/docker-compose.yml', "w")
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

class AnsibleGen(g):
    def __create_hosts_file__(self):
        keys = self.__get_key__('ansible')
        name = self.__get_key__('project_name')
        keys["project_name"] = name
        env = Environment(loader = FileSystemLoader('templates/ansible'),   
                trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('hosts.j2')
        file=open(f'{DIR_ROLE}/hosts', "w")
        file.write(template.render(keys))  
        file.close()

    def __create_vars_files__(self):
        name = self.__get_key__('project_name')
        keys = {}
        keys['project_name'] = name
        env = Environment(loader = FileSystemLoader('templates/ansible'),   
                trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('group_vars.j2')
        
        if not os.path.exists(DIR_ROLE + "/group_vars"):
            os.makedirs(DIR_ROLE + "/group_vars")
        
        
        file=open(f'{DIR_ROLE}/group_vars/stage.yml', "w")
        file.write(template.render(keys))  
        file.close()
        
        file=open(f'{DIR_ROLE}/group_vars/prod.yml', "w")
        file.write(template.render(keys))  
        file.close()
        
    
    def gen_ansible_role(self):
        env = Environment(loader = FileSystemLoader('templates/ansible'),   
                trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('deploy.j2')
        file=open(f'{DIR_ROLE}/deploy.yml', "w")
        file.write(template.render())  
        file.close()
        
        self.__create_hosts_file__()
        self.__create_vars_files__()