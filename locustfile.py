from locust import HttpUser, task, between
import random


class FastAPITestUser(HttpUser):
    wait_time = between(3, 5)  # 요청 간 대기 시간

    def on_start(self):
        """테스트 시작 시 실행: 로그인하여 토큰 가져오기"""
        response = self.client.post("/login/", data={"username": "admin123", "password": "admin123"})
        if response.status_code == 200:
            self.token = response.json()["access_token"]
        else:
            self.token = None

    def get_valid_token(self):
        """유효한 토큰 목록을 조회"""
        response = self.client.get(f"/tokens/{str(1234)}")
        if response.status_code == 200 and response.json()["tokens"]:
            return random.choice(response.json()["tokens"])  # 무작위로 하나 선택
        return None

    @task(1)
    def get_item(self):
        token = self.get_valid_token()
        if token:
            self.client.get(f"/items/{random.randint(1, 100)}", headers={"Authorization": f"Bearer {token}"})

    @task(1)  # POST 요청 실행
    def create_item(self):
        token = self.get_valid_token()
        if token:
            data = {"name": "Test Item", "price": random.uniform(10, 100)}
            self.client.post("/items/", json=data, headers={"Authorization": f"Bearer {token}"})

    @task(2)
    def create_image(self):
        token = self.get_valid_token()
        if token:
            self.client.post("/process_images/", headers={"Authorization": f"Bearer {token}"})

    @task(2)
    def get_files(self):
        token = self.get_valid_token()
        file_name = random.choice(["MainBefore.jpg", "brain.jpg", "free-nature-images.jpg"])
        if token:
            self.client.get(f"/get_files/{file_name}", headers={"Authorization": f"Bearer {token}"})

    @task(1)
    def get_large_files(self):
        token = self.get_valid_token()
        file_name = "svs_image.png"
        if token:
            self.client.get(f"/get_files/{file_name}", headers={"Authorization": f"Bearer {token}"}, timeout=30)