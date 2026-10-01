from fastapi import FastAPI
from backend.routes.students import routes

app = FastAPI()

app.include_router(routes)



