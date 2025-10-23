from fastapi import FastAPI


app = FastAPI() 

@app.post("/name/")

def read_name(name: str):
    return {"message": f"Hello, {name}!"}



@app.get("/")

def read_root(): 
    return {"message": "Hello, World!  "}


