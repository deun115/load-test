from sqlalchemy.orm import Session
from app import models, schemas

# 사용자 추가 (INSERT)
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.UserInfo(user_id=user.user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # 새로 추가된 데이터 반환
    return db_user

# 모든 사용자 조회 (SELECT)
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# 특정 사용자 조회 (SELECT)
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
