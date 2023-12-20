import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def port(self):
        with self.client.get("/port", catch_response=True, timeout=0.5) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed!")
