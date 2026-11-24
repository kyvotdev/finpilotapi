# from fastapi import Depends, HTTPException
# from authx import TokenPayload
#
# from finapi.auth.config import auth
#
#
# async def get_current_user(
#     payload: TokenPayload = Depends(auth.access_token_required),
#     repository: UserRepository = Depends(),
# ):
#     user = await repository.get_by_id(int(payload.sub))
#
#     if user is None:
#         raise HTTPException(
#             status_code=401,
#             detail="User not found",
#         )
#
#     if not user.is_active:
#         raise HTTPException(
#             status_code=403,
#             detail="User is inactive",
#         )
#
#     return user
