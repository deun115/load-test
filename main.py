import os
import time
from uuid import uuid4, UUID
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request
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


# 로그인 엔드포인트
@app.post('/login/')
async def login(user: User, background_tasks: BackgroundTasks):
    username = os.getenv('USERNAME', 'admin123')  # 기본값 설정
    password = os.getenv('PASSWORD', 'admin123')

    if user.username == username and user.password == password:
        rand_token = uuid4()
        token_set.add(rand_token)

        return {'token': str(rand_token)}  # UUID를 문자열로 반환
    else:
        raise HTTPException(status_code=401, detail='Invalid username or password')


# 현재 토큰 목록 조회
@app.get("/tokens/")
async def get_tokens():
    """현재 유효한 토큰 목록 반환"""
    return {"tokens": [str(token) for token in token_set]}  # UUID를 문자열로 변환


# 토큰 검증 함수
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    
    if not token:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    try:
        uuid_token = UUID(token)  # 문자열을 UUID로 변환
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Token format")

    if uuid_token not in token_set:
        raise HTTPException(status_code=401, detail="Invalid Token")


# 간단한 GET 엔드포인트
@app.get("/items/{item_id}")
async def read_item(item_id: int, _: None = Depends(verify_token)):  # 검증만 수행
    time.sleep(0.2)  # 응답 지연 시뮬레이션
    return {"item_id": item_id, "name": f"Item {item_id}"}


# POST 요청 엔드포인트 (토큰 필요)
@app.post("/items/")
async def create_item(item: Item, _: None = Depends(verify_token)):  # 검증만 수행
    time.sleep(0.3)  # 응답 지연 시뮬레이션
    return {"message": f"Item {item.name} created", "price": item.price}
