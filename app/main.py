from fastapi import FastAPI
from .routes.items import router as rt
from .models import core
from .models.database import engine


core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=rt,
                   prefix='/items',
                   )

app.include_router(router=rt,
                   prefix='/users'
                   )
