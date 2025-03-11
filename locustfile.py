from locust import HttpUser, task, between
import random


class FastAPITestUser(HttpUser):
    wait_time = between(1, 3)  # 요청 간 대기 시간

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

    @task(3)  # GET 요청을 3배 더 많이 실행
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
