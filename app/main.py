from fastapi import FastAPI

from .routes.items import router as items_rt
from .routes.users import router as users_rt
from .routes.tokens import router as token_rt

app = FastAPI()

app.include_router(router=items_rt,
                   prefix='/items',
                   )

app.include_router(router=users_rt,
                   prefix='/users'
                   )

app.include_router(router=token_rt,
                   prefix='/tokens'
                   )
