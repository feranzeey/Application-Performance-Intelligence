from locust import HttpUser, task

class WebsiteUser(HttpUser):

    @task
    def home(self):
        self.client.get("/")