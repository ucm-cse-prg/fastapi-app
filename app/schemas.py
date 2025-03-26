"""
Module for defining API request and response schemas.

This module defines Pydantic models that represent the data structures for products
used in various API endpoints, such as creating, retrieving, and updating products.
These schemas help with data validation and serialization between the client and server.
"""


# CHALLENGE:
# Remove the current Pydantic request and response schemas.
# Your task is to define schemas to validate API communication.
#
# Requirements:
# - Create a CreateProductRequest schema for POST requests.
# - Create a CreateProductResponse schema for returning a created product.
# - Create a GetProductResponse schema for returning a product.
# - Create an UpdateProductRequest and UpdateProductResponse schemas for product updates.
#
# Ensure your schemas reuse the models defined in app/models.py where appropriate.
#
# Example:


from pydantic import BaseModel
from beanie import PydanticObjectId
from app.models import Product

class CreateProductRequest(Product, BaseModel):
    pass

class CreateProductResponse(Product, BaseModel):
    id: PydanticObjectId

class GetProductResponse(CreateProductResponse):
    pass
class GetProductRequest(CreateProductRequest):
    pass
