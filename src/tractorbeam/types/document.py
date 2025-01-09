# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["Document"]


class Document(BaseModel):
    id: str
    """The ID of the document"""

    created_at: str
    """The date and time when the document was created in RFC 3339 format"""

    file_bytes: int
    """The size of the document in bytes"""

    file_type: str
    """The file type of the document"""

    name: str
    """The name of the document"""

    owner: str
    """The owner of the document"""
