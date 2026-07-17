from fastapi import APIRouter

from database.models import Product
from database.crud import (
    add_product,
    get_products
)

router = APIRouter()


@router.post("/add")
async def create_product(product: Product):

    result = await add_product(product)

    return {
        "message": "Product Added Successfully",
        "id": str(result.inserted_id)
    }


@router.get("/")
async def all_products():

    products = await get_products()

    for product in products:
        product["_id"] = str(product["_id"])

    return products