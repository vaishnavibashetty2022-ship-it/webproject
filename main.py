
from fastapi import FastAPI

app = FastAPI()

numbers = [10, 20, 30, 40, 50]


# 1. GET - Display all numbers
@app.get("/")
def home():
    return {"numbers": numbers}


# 2. GET - Display the sum
@app.get("/sum")
def total():
    return {"sum": sum(numbers)}


# 3. GET - Display the length
@app.get("/length")
def length():
    return {"length": len(numbers)}


# 4. POST - Add a number
@app.post("/add/{num}")
def add(num: int):
    numbers.append(num)
    return {"numbers": numbers}


# 5. PUT - Update a number at an index
@app.put("/update/{index}/{num}")
def update(index: int, num: int):
    if 0 <= index < len(numbers):
        numbers[index] = num
        return {"numbers": numbers}
    return {"error": "Invalid index"}


# 6. DELETE - Remove a number by index
@app.delete("/delete/{index}")
def delete(index: int):
    if 0 <= index < len(numbers):
        numbers.pop(index)
        return {"numbers": numbers}
    return {"error": "Invalid index"}


# 7. GET - Sort the numbers
@app.get("/sort")
def sort_numbers():
    return {"sorted_numbers": sorted(numbers)}


# 8. GET - Find the largest number
@app.get("/max")
def maximum():
    if len(numbers) > 0:
        return {"maximum": max(numbers)}
    return {"error": "List is empty"}


# 9. GET - Find the smallest number
@app.get("/min")
def minimum():
    if len(numbers) > 0:
        return {"minimum": min(numbers)}
    return {"error": "List is empty"}
