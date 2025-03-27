"""
Module for defining database document models.

This module uses Beanie's Document base class combined with Pydantic models
to define the schema of documents stored in the MongoDB collection.
"""

# CHALLENGE:
# Remove the existing Beanie Document implementation.
# Your task is to define Beanie document models that represent your MongoDB collections.
#
# Requirements:
# - Create a Product Document that inherits from Beanie's Document and your Product Pydantic model.
# - Configure the document's collection name and any relevant settings.
#
# Example:


from beanie import Document
from app.models import Product as ProductModel

class Product(Document, ProductModel):
    class Settings:
        name = "products"

