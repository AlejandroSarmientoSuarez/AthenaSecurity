from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", summary="Health check")
async def health_check():
    """Health check endpoint."""

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
    }