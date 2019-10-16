import requests,json
from collections import OrderedDict
from st2common.runners.base_action import Action

class PrintPythonHelloWorldAction(Action):
    def run(self,template_url):
        template_url = template_url.replace("https://github.com","https://raw.githubusercontent.com").replace("tree/","")
        template_name = template_url.rsplit('/', 1)[-1]
        metadata_content = self.get_github_content(template_url+"/metadata.json")
        metadata = json.loads(metadata_content)
        file_content = self.get_github_content(template_url+"/azuredeploy.json")
        return file_content
    
    def get_github_content(self,url):
        f = requests.get(url)
        return json.dumps(f.json(object_pairs_hook=OrderedDict))