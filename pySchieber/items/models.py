from utils import base_model
from django.db import models
from characters import models as chars
from shops import models as shops


class Item_Category(base_model):
    name = models.CharField(unique=True)
    description = models.TextField

class Base_Item(base_model):
    name = models.CharField()
    base_value = models.PositiveIntegerField
    description = models.TextField
    rarity = models.PositiveSmallIntegerField
    category = models.ForeignKey(Item_Category, on_delete = models.CASCADE, related_name="items")

class Character_Item(base_model):
    groups = models.ForeignKey(chars.Character_Sheet, on_delete = models.CASCADE, related_name="items")
    illegal = models.BooleanField
    stolen = models.BooleanField
    mod_value = models.PositiveIntegerField

class Store_Item(base_model):
    groups = models.ForeignKey(shops.shop, on_delete = models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField
    selling_price = models.PositiveIntegerField
    rarity_modifier = models.PositiveSmallIntegerField
    notes = models.TextField

