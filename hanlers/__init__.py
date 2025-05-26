from .tasks import router as tasks_router
from .ping_db import router as ping_router

routers = [tasks_router, ping_router]
