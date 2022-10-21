# API_Strsss_Test
This project is made by python Locust.


## Step
1. Install python in local. Refer to use python3.10

2. Setup virtual environment
    
        python3 -m venv env

3. Install all necessary module

        pip install -r requirements.txt

3. Edit your python script

4. Run stress test

        locust -f locustfile.py -H http://{api_server_ip}:{port}

5. Go to Locus Web UI at http://0.0.0.0:8089