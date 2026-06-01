from fastapi import APIRouter,Depends,HTTPException


person_router=APIRouter(tags=['person'],prefix='/person')


@person_router.post("/new")
async def create_new_person():
    pass 

@person_router.get("/all")
async def get_all_person():
    pass 


@person_router.get("/{id}")
async def get_person_with_id(id:int):
    pass 