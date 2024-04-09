from fastapi import FastAPI

#uvicorn calcserver:app --reload
app = FastAPI()

@app.get("/api/calc")
async def calc(op1  = 0, op2  = 0, op  = '+') :
    status = "error"
    if op == '+' :        
        status = "ok"
        result = op1 + op2
    elif op == '-' :
        status = "ok"
        result = op1 - op2
    elif op == '*' :
        status = "ok"
        result = op1 * op2        
    elif op == '/' :
        status = "ok"
        result = op1 / op2     

    return {"stats": status, "left operand":op1, "right operand":op2, "operation":op, "result":result}

#Defualt value 가 없으면 첫번째가 필수파라미터가 된다.
@app.get("/api/weather")
async def weather(city: str = "Bengaluru"):
    return {"status":"ok",
            "city": city, 
            "temperature": 33, 
            "unit": "C"}