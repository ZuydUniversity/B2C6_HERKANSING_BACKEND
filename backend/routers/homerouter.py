from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={404: {"description": "Not found"}, 200: {"description": "OK"}, 400: {"description": "Bad Request"}, 500: {"description": "Internal Server Error"}}
)

@router.get("/")
async def homeurl():
    return {"message": "API is working!"}

