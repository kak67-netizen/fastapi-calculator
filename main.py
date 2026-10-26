"""FastAPI web application for the calculator."""

import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app import operations

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI Calculator")
templates = Jinja2Templates(
    directory=Path(__file__).parent / "templates"
)


class Numbers(BaseModel):
    """Two numbers submitted to a calculator endpoint."""

    a: float
    b: float


@app.get("/")
async def home(request: Request):
    """Show the calculator webpage."""
    logger.info("Calculator page opened")
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


def calculate(operation_name: str, function, numbers: Numbers):
    """Run one arithmetic function and log the result or error."""
    try:
        result = function(numbers.a, numbers.b)
    except ValueError as error:
        logger.warning(
            "%s failed for a=%s and b=%s: %s",
            operation_name,
            numbers.a,
            numbers.b,
            error,
        )
        raise HTTPException(status_code=400, detail=str(error)) from error

    logger.info(
        "%s: %s and %s produced %s",
        operation_name,
        numbers.a,
        numbers.b,
        result,
    )
    return {"result": result}


@app.post("/add")
async def add_numbers(numbers: Numbers):
    return calculate("add", operations.add, numbers)


@app.post("/subtract")
async def subtract_numbers(numbers: Numbers):
    return calculate("subtract", operations.subtract, numbers)


@app.post("/multiply")
async def multiply_numbers(numbers: Numbers):
    return calculate("multiply", operations.multiply, numbers)


@app.post("/divide")
async def divide_numbers(numbers: Numbers):
    return calculate("divide", operations.divide, numbers)