from fastapi import FastAPI

from .routes.items import router as items_rt
from .routes.users import router as users_rt

app = FastAPI()

app.include_router(router=items_rt,
                   prefix='/items',
                   )

app.include_router(router=users_rt,
                   prefix='/users'
                   )
