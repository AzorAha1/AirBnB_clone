#!/usr/bin/python3
"""this is a class(blueprint) for place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class place that inherits from BaseModel
    public class attributes
    - city_id
    - user_id
    - name
    - description
    - number_rooms
    - number_bathrooms
    - max_guest
    - price_by_night
    - latitude
    - longitude
    - amenity_ids
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = ''
