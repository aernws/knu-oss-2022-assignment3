from fastapi import FastAPI

app1 = FastAPI()
numbers = {}
sum = 0
sumofsqr = 0
count = 0
average = 0
stddev = 0


@app1.post("?new=")
async def addnumber(newnumber: int):
    message = "Error"
    if newnumber is int:
        message = "OK"
        sum = sum + newnumber
        sumofsqr = sumofsqr + newnumber * newnumber
        count = count + 1
        avarage = sum / count
        stddev = sumofsqr / count - average * average
    return{"result": message}
    

@app1.get("/average")
async def getaverage():
    message = "No numbers in the array"
    if count >= 1:
        message = average
    return {"result": message}

@app1.get("/sum")
async def getsum():
    message = "No numbers in the array"
    if count >= 1:
        message = sum
    return {"result": message}

@app1.get("/stddev")
async def getstddev():
    message = "No numbers in the array"
    if count >= 1:
        message = stddev
    return {"result": message}