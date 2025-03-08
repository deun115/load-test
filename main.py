import os
import time
from uuid import uuid4, UUID
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()  # 환경 변수 로드

app = FastAPI()
token_set = set()  # 빠른 검색을 위한 set 사용
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # OAuth2 Bearer 토큰 사용


# 요청 데이터 모델
class Item(BaseModel):
    name: str
    price: float


def remove_token_after_delay(token: str, delay: int = 300):
    """지정된 시간 후 토큰 삭제 (기본 5분)"""
    time.sleep(delay)
    token_set.discard(token)


@app.post('/login/')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), background_tasks: BackgroundTasks = None):
    username = os.getenv('USERNAME', 'admin123')
    password = os.getenv('PASSWORD', 'admin123')

    if form_data.username == username and form_data.password == password:
        rand_token = uuid4()
        token_set.add(rand_token)
        
        background_tasks.add_task(remove_token_after_delay, rand_token, 300)

        return {"access_token": str(rand_token), "token_type": "bearer"}  # OAuth2 형식의 응답
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


# 현재 토큰 목록 조회
@app.get("/tokens/")
async def get_tokens():
    """현재 유효한 토큰 목록 반환"""
    return {"tokens": [str(token) for token in token_set]}  # UUID를 문자열로 변환


# 토큰 검증 함수 (OAuth2 방식)
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        uuid_token = UUID(token)  # 문자열을 UUID로 변환
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Token format")

    if uuid_token not in token_set:
        raise HTTPException(status_code=401, detail="Invalid Token")


@app.get("/items/{item_id}")
async def read_item(item_id: int, _: None = Depends(verify_token)):  # 검증만 수행
    time.sleep(0.2)  # 응답 지연 시뮬레이션
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.post("/items/")
async def create_item(item: Item, _: None = Depends(verify_token)):  # 검증만 수행
    time.sleep(0.3)  # 응답 지연 시뮬레이션
    return {"message": f"Item {item.name} created", "price": item.price}
