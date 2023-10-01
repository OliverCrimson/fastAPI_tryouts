from fastapi import FastAPI
from routes.items import router as rt

app = FastAPI()

app.include_router(router=rt,
                   prefix='/items',
                   )
