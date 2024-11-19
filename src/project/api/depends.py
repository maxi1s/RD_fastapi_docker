from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.infrastructure.postgres.repository.flowers_repo import FlowerRepository


user_repo = UserRepository()
flowers_repo = FlowerRepository()
database = PostgresDatabase()
