from fastapi import FastAPI

app = FastAPI()

@app.get("/api/calc")
async def calc(op1 = 1, op2 = 0, op : str = '+'):
    status = "error"
    op1 = int(op1)
    op2 = int(op2)
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
    return {"stats": status, "left operand":op1, "right operand":op2,"operation":op,"result":result}

