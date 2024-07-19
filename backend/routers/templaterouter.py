from fastapi import APIRouter
from ..models.templatemodel import TemplateModel

router = APIRouter(
    prefix="/api/template",
    tags=["template"],
    responses={
        404: {"description": "Not found"},
        200: {"description": "OK"},
        400: {"description": "Bad Request"},
        500: {"description": "Internal Server Error"}
    }
)

@router.get("/")
async def get_template():
    models = {1, "Homoerectus", "USA"}
    return models
