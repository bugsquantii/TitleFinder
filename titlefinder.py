import requests
from base64 import b64encode

class TitleFinder:

    def get_title(self, url):

        #Get the domain from the url
        domain = url.split('/')[2]
        #If there is a www, remove it
        if domain.startswith('www.'):
            domain = domain[4:]
        
        #Remove domain extension
        domain = domain.split('.')[0]

        print(domain)

        #Check domain and call the right function
        match domain:
            #case 'youtube' or 'youtu':
            case 'youtube' | 'youtu':
                return self.get_youtube_title(url)
            case _:
                return 'Unknown domain'
        
            

    def get_youtube_title(self, url):

        #Open this url and looking for the video title, using requests
        response = requests.get(url)
        
        #Looking for <title> tag
        start = response.text.find("<title>") + len("<title>")
        end = response.text.find("</title>")
        title = response.text[start:end]

        encoded_title = b64encode(title.encode('utf-8')).decode('utf-8')
        return encoded_title
