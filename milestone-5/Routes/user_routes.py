"""Routes for user operations.

This module defines user endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
from Controllers.user_controller import UserController
from Schemas.api_schemas import CreateUserRequest, UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(request: CreateUserRequest, db: Session = Depends(get_db)):
    """Create a new user.
    
    Args:
        request: CreateUserRequest with user_name.
        db: Database session (injected).
        
    Returns:
        UserResponse with user_id and user_name.
    """
    controller = UserController(db)
    return controller.create_user(request.user_name)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    """Get a user by ID.
    
    Args:
        user_id: The user's UUID.
        db: Database session (injected).
        
    Returns:
        UserResponse with user_id and user_name.
        
    Raises:
        HTTPException: If user not found.
    """
    controller = UserController(db)
    user = controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
