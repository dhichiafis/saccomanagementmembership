from fastapi import FastAPI
import uvicorn 
from routes.person import person_router

app=FastAPI()
app.include_router(person_router)



@app.get('/')
async def home():
    return {"message":"this si teh user person identification"}


