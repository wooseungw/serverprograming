from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
def root(id=5000,check=True) :
    return {"message":"hello","id":id,"check":check}

@app.get("/2")
async def root2() :
    return ["hello", 45, 78.2, True]

@app.get("/3")
async def root3() :
    return 45

@app.get("/4",response_class=HTMLResponse)
async def root4() :
    return "<h1>Hello</h1>"

@app.get("/5/{id}") 
async def root5(id = 20) :
    return {"id" : id}

@app.get("/login")
def login(userid=None,pwd=None):
    if userid == pwd:
        check = True
        return {"login":check,"userid":userid,"pwd":pwd}
    else: 
        check = False
        return {"login":check}

@app.post("/login")
def login(userid=None,pwd=None):
    if userid == pwd:
        check = True
        return {"login":check,"userid":userid,"pwd":pwd}
    else: 
        check = False
        return {"login":check}
    
# id=7, name=이순신, age=75
@app.get("/6")
async def root5(id  = 0, name = "" , weight  = 60.0)  :
    return {"id" : id, "name":name, "weight" : weight}
