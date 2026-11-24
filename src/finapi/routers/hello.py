from fastapi import APIRouter

hellortr = APIRouter(prefix="/hello", tags=["hello test routers"])


@hellortr.get("")
async def hello_friend():
    return {"msg": "Hello friend!"}
