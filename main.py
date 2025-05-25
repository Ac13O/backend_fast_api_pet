from fastapi import FastAPI

from hanlers import router

app = FastAPI()
app.include_router(router=router)
