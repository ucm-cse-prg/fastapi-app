import logging

from fastapi import status
from beanie import PydanticObjectId
from app.documents import Product

logger = logging.getLogger("uvicorn.error")


class APIException(Exception):
    """
    Base exception class for API-related errors.

    This exception is raised when an API error occurs. It includes an HTTP status code
    and a descriptive error message.
    """

    def __init__(self, code: int, detail: str):
        # HTTP status code that indicates the type of error.
        self.code = code
        # A descriptive error message.
        self.detail = detail
        logger.warning(self.detail)

    def __str__(self) -> str:
        # Return the error message when the exception is printed.
        return self.detail


class InternalServerError(APIException):
    """
    Exception raised for internal server errors (HTTP 500).

    Inherits from APIException and automatically assigns a 500 HTTP status code.
    """

    def __init__(self, detail: str):
        # Initialize with HTTP 500 status code and a generic internal server error message.
        super().__init__(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        )


# CHALLENGE:
# Implement custom exceptions to handle different types of API errors.
#
# Define functions like create_product, get_product, update_product, delete_product with appropriate signatures.
#
# Example:
#
class ProductNotFound(APIException):
    def __init__(self, product_id: PydanticObjectId):
        super().__init__(
            code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )
