"""
This module implements a FastAPI application for Accepting matrix as request 
and finding maximal rectangle areas.
"""
from time import time
from fastapi import FastAPI, Request
from pydantic import BaseModel
from uvicorn import run
from find_area import Max_Rect
from logger import logger
from db import DB

app = FastAPI()
db_obj = DB()
logger.info("App will run on http://127.0.0.1:8000")
db_info = []

class MatrixInput(BaseModel):
    'Class for getting the matrix in this datatype'
    matrix: list[list[int]]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    '''
    Middleware to add process time header to responses and log information to database.

    Parameters:
    request (Request): The incoming request.
    call_next (function): The next handler in the middleware chain.

    Returns:
    response: The response with added process time header.
    '''
    start_time = time()
    response = await call_next(request) # wait for response
    process_time = time() - start_time # calculate the time after response
    response.headers["X-Process-Time"] = str(process_time)
    res = f"Response returned. Processing time was {time()}"
    db_info.append(res)
    db_obj.insert_(res=db_info[0], req=db_info[2], turn_time=str(process_time), result=db_info[1])
    logger.info("inserted into DB")
    return response

@app.post("/execute/")
async def process_matrix(matrix: MatrixInput):
    '''
    Endpoint to process the input matrix and find the maximal rectangle area.

    Parameters:
    matrix (MatrixInput): The input matrix.

    Returns:
    dict: Dictionary containing the result of the execution.
    '''

    req = f'''Request received with input matrix 
    Rows {len(matrix.matrix)} 
    Cols {len(matrix.matrix[0])} 
    at time {time()}
    '''
    db_info.append(req)
    logger.info(req + f"Input Matrix : {matrix}")
    max_rect = Max_Rect()
    max_rect.execute(matrix=matrix.matrix)
    result = max_rect.get_result()
    db_info.append(result)
    return {"result": result}

if __name__ == "__main__":
    run(app, port=8000)
