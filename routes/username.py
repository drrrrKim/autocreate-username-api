from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from service.generate_data import create_username

router = APIRouter()

@router.post('/create')
def create_user_name():
    username = create_username()
    if username:
        return JSONResponse(
            status_code=201,
            content={"username": username}
        )
    else:
        raise HTTPException(
            status_code=500,
            detail="Unable to create user name"
        )