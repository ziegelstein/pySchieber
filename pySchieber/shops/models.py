from utils import base_model
from django.db import models
from items import models as items
from shops import models as shops
from characters import models as chars


class Shop_Category(base_model):
    name = models.CharField()
    allowed_categories = models.ManyToManyField(items.Item_Category, on_delete = models.CASCADE, related_name="items")
    description = models.TextField
    category = models.CharField

class Shop_Location(base_model):
    name = models.CharField(unique=True, blank=False)
    type = models.CharField

class Shop(base_model):
    name = models.CharField()
    location = models.ForeignKey(Shop_Location, on_delete = models.CASCADE, related_name="shops")
    category = models.ForeignKey(Shop_Category, on_delete = models.CASCADE, related_name="shops")
    illegal = models.BooleanField
    owner = models.ForeignKey(chars.Character_Sheet, on_delete = models.CASCADE, related_name="shops")
    description = models.TextField