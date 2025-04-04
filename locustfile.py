from locust import HttpUser, task, between
import random
import string

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def fetch_subjects(self):
        self.client.get("api/subjects/")

    @task
    def fetch_contents(self):
        subject_id = self.random_subjects()
        self.client.get(f"api/contents/{subject_id}")

    @task
    def fetch_activities(self):
        content_id = self.random_contents()
        self.client.get(f"api/activities/{content_id}")

    @task
    def register_user(self):
        username = self.random_username()
        email = f"{username}@example.com"
        password = "TestPass123"

        self.client.post(
            "account/register/",
            json={
                "user_name": username,
                "user_email": email,
                "user_password": password
            }
        )

    def random_subjects(self):
        num = random.choice([5, 7, 1])
        return num
    
    def random_contents(self):
        num = random.choice([2, 3, 5])
        return num
    
    def random_username(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))