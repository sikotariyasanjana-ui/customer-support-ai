async def get_products():

    cursor = products_collection.find()

    return await cursor.to_list(length=100)


async def get_complaints():

    cursor = complaints_collection.find()

    return await cursor.to_list(length=100)


async def save_feedback(feedback):

    return await feedback_collection.insert_one(
        feedback.model_dump()
    )


async def add_product(product):

    return await products_collection.insert_one(
        product.model_dump()
    )


async def create_complaint(complaint):

    return await complaints_collection.insert_one(
        complaint.model_dump()
    )