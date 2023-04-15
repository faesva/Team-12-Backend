from fastapi import FastAPI
from fastapi.params import Depends
from typing import List
from starlette.responses import RedirectResponse
import models, schemas
from Config import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/movies/',response_model=List[schemas.Movie])
def get_movies(db:Session=Depends(get_db)):
    movies = db.query(models.Movie).all()
    return movies

@app.post('/movies/',response_model=schemas.Movie)
def create_movie(input:schemas.Movie,db:Session=Depends(get_db)):
    movie = models.Movie(user_id=input.user_id, category_id=input.category_id, title=input.title, sipnosis = input.sipnosis, director = input.director, release_date = input.release_date)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

@app.get('/users/',response_model=List[schemas.User])
def get_users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post('/users/',response_model=schemas.User)
def create_user(input:schemas.User,db:Session=Depends(get_db)):
    user = models.User(is_admin=False,username=input.username,name=input.name,email=input.email,password=input.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.put('/users/{id}',response_model=schemas.User)
def update_user(id:int,input:schemas.UserUpdate,db:Session=Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    user.name=input.name
    user.password=input.password
    db.commit()
    db.refresh(user)
    return user

@app.delete('/users/{id}',response_model=schemas.Response)
def delete_user(id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter_by(id=id).first()
    db.delete(user)
    db.commit()
    res = schemas.Response(message="¡User deleted!")
    return res
