from fastapi import APIRouter
from service.generate_data import create_username

router = APIRouter()

@router.post('/create')
def create_user_name():
    username = create_username()
    if username:
        return {"username":username}
    else:
        return {"status":"Unable to create user name"}