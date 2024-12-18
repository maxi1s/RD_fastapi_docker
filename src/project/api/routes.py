from fastapi import APIRouter, HTTPException, status

from project.schemas.user import UserSchema, UserCreateUpdateSchema
from project.schemas.healthcheck import HealthCheckSchema
from project.core.exceptions import UserNotFound, UserAlreadyExists, FlowerAlreadyExists
from project.schemas.flowers import FlowerSchema, FlowerCreateSchema
from project.api.depends import database, user_repo, flowers_repo


router = APIRouter()
@router.get("/flowers", response_model=list[FlowerSchema], status_code=status.HTTP_200_OK)
async def get_flowers() -> list[FlowerSchema]:
        async with database.session() as session:
            all_flowers = await flowers_repo.get_all_flowers(session=session)

        return all_flowers
#Криво но уже работае.
@router.post("/add_flower", response_model=FlowerSchema, status_code=status.HTTP_201_CREATED)
async def add_flower(flower_data: FlowerCreateSchema,) -> FlowerSchema:
        try:
            async with database.session() as session:
                new_flower = await flowers_repo.create_flower(session=session, flower_data=flower_data)
        except FlowerAlreadyExists as error:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

        return new_flower


@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=status.HTTP_200_OK)
async def check_health() -> HealthCheckSchema:
    async with database.session() as session:
        db_is_ok = await user_repo.check_connection(session=session)

    return HealthCheckSchema(
        db_is_ok=db_is_ok,
    )


@router.get("/all_users", response_model=list[UserSchema], status_code=status.HTTP_200_OK)
async def get_all_users() -> list[UserSchema]:
    async with database.session() as session:
        all_users = await user_repo.get_all_users(session=session)

    return all_users


@router.get("/user/{user_id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: int,
) -> UserSchema:
    try:
        async with database.session() as session:
            user = await user_repo.get_user_by_id(session=session, user_id=user_id)
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return user


@router.post("/add_user", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def add_user(
    user_dto: UserCreateUpdateSchema,
) -> UserSchema:
    try:
        async with database.session() as session:
            new_user = await user_repo.create_user(session=session, user=user_dto)
    except UserAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_user


@router.put(
    "/update_user/{user_id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def update_user(
    user_id: int,
    user_dto: UserCreateUpdateSchema,
) -> UserSchema:
    try:
        async with database.session() as session:
            updated_user = await user_repo.update_user(
                session=session,
                user_id=user_id,
                user=user_dto,
            )
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_user


@router.delete("/delete_user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
) -> None:
    try:
        async with database.session() as session:
            user = await user_repo.delete_user(session=session, user_id=user_id)
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return user
