
from locust import FastHttpUser, task
import random
import json
import time


class WebsiteUser(FastHttpUser):
    """
    User class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """

    host = ''
    # some things you can configure on FastHttpUser
    # connection_timeout = 60.0
    insecure = True
    # max_redirects = 5
    max_retries = 1
    network_timeout = 60.0
    token = None
    api_headers = None
    login_header_hash = ''
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()


    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        # self.logout()
        pass



    def login(self):
        print('do login')
        loginUrl = self.host+'/api/portal_common/login'
        login_headers = {
            'wimes':self.login_header_hash,
            'Content-Type': 'application/json',
        }
        
        payload = {
            'userId': '',
            'password': ''
        }
        response = self.client.post(loginUrl, data=json.dumps(payload), headers=login_headers)
        res_data = response.json()
        '''Get authentication token from response data'''
        self.token = str(res_data['token'])
                
        self.api_headers = {
            'wimes':self.login_header_hash,
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.token
        }
        print(self.api_headers)

    def logout(self):
        self.client.post('/logout', {"username":"ellen_key", "password":"education"})

    # '''
    # get percetage for each task by using @task decorator
    # '''
    @task
    def do_CimApplication(self):        
        res = self.client.get('api/', headers=self.api_headers)
        print(res.json())
