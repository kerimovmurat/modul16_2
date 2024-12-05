from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

@app.get("/")
async def start_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async  def userid_page(user_id:Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='55')]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_page(username:str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                     age:int = Path(ge=18, le=120, description='Enter age', example='77')) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
