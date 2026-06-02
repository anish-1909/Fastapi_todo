from fastapi import APIRouter

from ..models.user import User
from ..models.user import LoginRequest

from ..services.auth_service import AuthService

router = APIRouter()

@router.post("/register")
def register(user: User):

    return AuthService.register(
        user.username,
        user.password
    )


@router.post("/login")
def login(user: LoginRequest):

    return AuthService.login(
        user.username,
        user.password
    )