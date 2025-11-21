"""
Root router
"""
from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/")
async def home():
    """Root endpoint"""
    return "SoulTrip backend está funcionando correctamente"

