from schemas.news import NewsDetailsModel, NewsModel
from schemas.users import User
from utils import news as post_utils
from utils.dependecies import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/posts", response_model=NewsDetailsModel, status_code=201)
async def create_post(post: NewsModel, current_user: User = Depends(get_current_user)):
    print("POOOOST", post)
    post = await post_utils.create_post(post, current_user)
    return post


@router.get("/posts")
async def get_posts(page: int = 1):
    #total_cout = await post_utils.get_posts_count()
    posts = await post_utils.get_posts(page)
    #return {"total_count": total_cout, "results": posts}
    # Преобразуем каждый элемент в словарь, преобразуя datetime в строку
    posts_dicts = []
    for post in posts:
        post_dict = dict(post)
        post_dict["created_at"] = post_dict["created_at"].isoformat()  # Преобразование datetime в строку
        posts_dicts.append(post_dict)
    return posts_dicts


@router.get("/posts/{post_id}", response_model=NewsDetailsModel)
async def get_post(post_id: int):
    return await post_utils.get_post(post_id)


@router.put("/posts/{post_id}", response_model=NewsDetailsModel)
async def update_post(
    post_id: int, post_data: NewsModel, current_user=Depends(get_current_user)
):
    post = await post_utils.get_post(post_id)
    if post["user_id"] != current_user["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to modify this post",
        )

    await post_utils.update_post(post_id=post_id, post=post_data)
    return await post_utils.get_post(post_id)