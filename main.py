from fastapi import FastAPI
from hanlers import routers


app = FastAPI()

for router in routers:
    app.include_router(router=router)
