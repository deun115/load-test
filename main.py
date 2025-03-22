import io
import logging
import os
import time
from uuid import uuid4, UUID
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request, Response, logger
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from dotenv import load_dotenv

import cv2
from PIL import Image

load_dotenv()  # 환경 변수 로드

app = FastAPI()
token_set = set()  # 빠른 검색을 위한 set 사용
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # OAuth2 Bearer 토큰 사용


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 요청 시간 측정용 미들웨어
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} completed in {duration:.4f}s with status {response.status_code}")
    return response


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
        
        # background_tasks.add_task(remove_token_after_delay, rand_token, 300)

        return {"access_token": str(rand_token), "token_type": "bearer"}  # OAuth2 형식의 응답
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


# 토큰 검증 함수 (OAuth2 방식)
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        uuid_token = UUID(token)  # 문자열을 UUID로 변환
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Token format")

    if uuid_token not in token_set:
        raise HTTPException(status_code=401, detail="Invalid Token")


# 현재 토큰 목록 조회
@app.get("/tokens/{access_code:str}")
async def get_tokens(access_code: str):
    """현재 유효한 토큰 목록 반환"""
    if access_code == os.getenv('ACCESS_CODE', '1234'):
        return {"tokens": [str(token) for token in token_set]}  # UUID를 문자열로 변환
    else:
        raise HTTPException(status_code=403, detail="Invalid Access Code")


@app.get("/items/{item_id}")
async def read_item(item_id: int, _: None = Depends(verify_token)):  # 검증만 수행
    time.sleep(0.2)  # 응답 지연 시뮬레이션
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.post("/items/")
async def create_item(item: Item, _: None = Depends(verify_token)):  # 검증만 수행
    time.sleep(0.3)  # 응답 지연 시뮬레이션
    return {"message": f"Item {item.name} created", "price": item.price}


# 이미지 처리
@app.post("/process_images/")
async def create_image(_: None = Depends(verify_token)):
    image = cv2.imread("inputs/dog.png")
    blurred = cv2.blur(image, (9, 9))
    blurred_pil = Image.fromarray(blurred)
    
    img_byte_arr = io.BytesIO()
    blurred_pil.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)  # 바이트 스트림의 시작점으로 이동

    return StreamingResponse(img_byte_arr, media_type="image/png")


# 파일 전송 
@app.get("/get_files/{file_name:str}")
async def get_file(file_name: str, _: None = Depends(verify_token)):
    internal_path = f"/files/{file_name}"

    return Response(
        status_code=200,
        headers={"X-Accel-Redirect": internal_path}
    )