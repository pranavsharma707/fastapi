from fastapi import FastAPI
import model
from databases import engine
from routers import blog,user,authentication


app=FastAPI()

model.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)








