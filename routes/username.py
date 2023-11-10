from fastapi import APIRouter
from service.generate_data import create_name, create_adjectives

router = APIRouter()

@router.get('/create')
async def create_user_name():
    first_adjectives = await create_adjectives()
    second_name = await create_name()
    username = first_adjectives + " " + second_name
    return {"username":username}
