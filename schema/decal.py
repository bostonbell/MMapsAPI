"""Schema definition for the decal domain object."""

from flask_restful import fields

from resources.schema import add_api_schema

decal_schema = {
    "name": "decal",
    "fields": {
        # Base Metadata
        "_id": {
            "type": fields.String,
            "required": False,
            "read_only": True,
            "description": "Server generated ID of a decal."
        },

        # Core Domain Data
        "url": {
            "type": fields.String,
            "required": True,
            "read_only": True,
            "description": "Url to given image of a decal."
        }
    },
    "example": {
        "_id": "5aa9e7734700a016fcc12ced",
        "url": "http://www.azure.com/lol"
    }
}

add_api_schema(decal_schema)