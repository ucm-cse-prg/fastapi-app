"""
Module for defining Pydantic models for the application.

This module defines the data models for Product and Category, which are used
to validate and serialize the data passed between the API client and the server.
"""

from pydantic import BaseModel, Field, field_validator


class Category(BaseModel):
    """
    Data model representing a product category.

    Attributes:
        name (str): The name of the category. Must be 2-50 characters long and
                    match the pattern allowing alphanumeric characters, underscores, spaces, or ampersands (&).
        description (str): A brief description of the category. Maximum 200 characters.
    """

    name: str = Field(
        default_factory=str,
        title="Name",
        description="Name of the category",
        max_length=50,
        min_length=2,
        pattern=r"^[\w\s&]+$",
        examples=["Phones", "Accessories"],
    )
    description: str = Field(
        default="",
        title="Description",
        description="Description of the category",
        max_length=200,
        examples=["Mobile phones", "Smartphone watches, headphones, and chargers"],
    )


class Product(BaseModel):
    """
    Data model representing a product.

    Attributes:
        name (str): The name of the product. Must be 2-50 characters long and
                    match the pattern allowing alphanumeric characters, spaces, or dashes.
        description (str): A detailed description of the product. Maximum 200 characters.
        price (float): The price of the product. Must be greater than 0 and less than 100000.
                       Additionally, the price must end with a '0.99' fractional component.
        category (Category): The category to which the product belongs.
    """

    name: str = Field(
        default_factory=str,
        title="Name",
        description="Name of the product",
        max_length=50,
        min_length=2,
        pattern=r"^[\w\s-]+$",
        examples=["SM-G973F", "iPhone 12"],
    )
    description: str = Field(
        default="",
        title="Description",
        description="Description of the product",
        max_length=200,
        examples=["Samsung Galaxy S10", "The latest iPhone"],
    )
    price: float = Field(
        title="Price",
        description="Price of the product",
        gt=0,
        lt=100000,
        allow_inf_nan=False,
        examples=[799.99, 1299.99],
    )
    category: Category

    @field_validator("price", mode="after")
    @classmethod
    def price_ends_with_99(cls, v: float) -> float:
        """
        Validator to ensure the price ends with '0.99'.

        Args:
            v (float): The price value to validate.

        Raises:
            ValueError: If the price does not end with 0.99.

        Returns:
            float: The validated price which ends with 0.99.
        """
        # Use modulo operator with rounding to check if fractional part equals 0.99.
        if round(v % 1, 2) != 0.99:
            raise ValueError("Price must end with 0.99")
        return v
