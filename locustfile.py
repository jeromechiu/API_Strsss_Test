
from locust import FastHttpUser, task
import random
import json
import time





class WebsiteUser(FastHttpUser):
    """
    User class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """

    host = "http://127.0.0.1:8000"
    # some things you can configure on FastHttpUser
    # connection_timeout = 60.0
    insecure = True
    # max_redirects = 5
    max_retries = 1
    network_timeout = 60.0
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        # self.logout()
        pass



    def login(self):
        loginUrl = 'http://wiles-portal-new.k8s-dev.k8s.wistron.com/api/portal_common/login'
        login_header = {
            'wimes':'eyJ1c2VySWQiOm51bGwsInBsYW50IjoiRjEzMCIsImltYWdlIjoicGxhdGZvcm0ucG9ydGFsd2VidWkiLCJhcElkIjoiQ0lNX1NJR05JTl9XV19XRUJVSSIsInZlcnNpb24iOiIwLjIuNDAiLCJsYW5ndWFnZSI6InpoLVRXIiwicmVxdWVzdFRpbWUiOiIyMDIyLTEwLTI3VDA5OjUxOjQ5LjEzN1oifQ=='
            }
        payload = {
            "userId": "lmsuser2020",
            "password": "lmsuser2020"
            }
        response = self.client.post(loginUrl, )
        res_data = response.json()
        '''Get authentication token from response data'''

    def logout(self):
        self.client.post("/logout", {"username":"ellen_key", "password":"education"})


    '''
    get percetage for each task by using @task decorator
    '''
    @task(20)
    def get_single_Prod(self):
        pid = 27
        self.client.get(f"/api/prods?pid={pid}")

    @task(9)
    def get_all_Prod(self):
        self.client.get(f"/api/prods")
    
    @task(1)
    def add_a_prod(self):
        
        headers = {
            'content-type': 'application/json',
            # 'Authorization': 'Basic YWxpY2U6c3VwZXJtYW4='
            }
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890'
        subName = random.sample(alphabet, 13)
        subName = ''.join(subName)
        padName = f'pr_{subName}'
        payload = {
            "name": padName,
            "amount": 10,
            "delete_able": False
        }
        self.client.post('/api/prods', data=json.dumps(payload), headers=headers)
        
    @task(1)
    def update_a_prod(self):
        
        headers = {
            'content-type': 'application/json',
            # 'Authorization': 'Basic YWxpY2U6c3VwZXJtYW4='
            }
        
        padName = 'I406'
        payload = {
            "name": padName,
            "amount": 10,
            "delete_able": False
        }
        self.client.put('/api/prods', data=json.dumps(payload), headers=headers)
        
    @task(1)
    def delete_a_prod(self):
        
        headers = {
            'content-type': 'application/json',
            # 'Authorization': 'Basic YWxpY2U6c3VwZXJtYW4='
            }
        pid = 27
        # self.client.delete('/api/prods?pid={pid}', headers=headers)
    
