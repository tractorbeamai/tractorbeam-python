# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["APIToken"]


class APIToken(BaseModel):
    id: str
    """The ID of the API token. Starts with prefix `token_`."""

    created_at: str
    """
    The date and time when the API token was created in
    [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format.
    """

    name: str
    """The human-readable name of the API token."""

    owner: str
    """The owner of the API token, either an organization or a user."""

    token_prefix: str
    """The 8-character prefix of the token itself."""
