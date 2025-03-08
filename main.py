import os
import time
from uuid import uuid4
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()  # 환경 변수 로드

app = FastAPI()
token_set = set()  # 빠른 검색을 위한 set 사용


# 요청 데이터 모델
class Item(BaseModel):
    name: str
    price: float

class User(BaseModel):
    username: str
    password: str


# 토큰 자동 삭제 (배경 작업)
def remove_token_after_delay(token: str, delay: int = 300):
    """지정된 시간 후 토큰 삭제 (기본 5분)"""
    time.sleep(delay)
    token_set.discard(token)  # 존재하면 삭제


# 로그인 엔드포인트
@app.post('/login/')
async def login(user: User, background_tasks: BackgroundTasks):
    username = os.getenv('USERNAME', 'admin')  # 기본값 설정
    password = os.getenv('PASSWORD', 'password')

    if user.username == username and user.password == password:
        rand_token = uuid4().hex()
        token_set.add(rand_token)

        # 일정 시간이 지나면 토큰 삭제
        background_tasks.add_task(remove_token_after_delay, rand_token, 300)

        return {'token': rand_token}
    else:
        raise HTTPException(status_code=401, detail='Invalid username or password')


# 토큰 검증 함수
def verify_token(token: str):
    if token not in token_set:
        raise HTTPException(status_code=401, detail="Invalid Token")
    return True


# 간단한 GET 엔드포인트
@app.get("/items/{item_id}")
async def read_item(item_id: int, token: str = Depends(verify_token)):
    time.sleep(0.2)  # 응답 지연 시뮬레이션
    return {"item_id": item_id, "name": f"Item {item_id}"}


# POST 요청 엔드포인트 (토큰 필요)
@app.post("/items/")
async def create_item(item: Item, token: str = Depends(verify_token)):
    time.sleep(0.3)  # 응답 지연 시뮬레이션
    return {"message": f"Item {item.name} created", "price": item.price}
