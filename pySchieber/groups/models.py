from utils import base_model
from django.db import models
from contacts import models as cont
from characters import models as chars


class Group(base_model):
    name = models.CharField("Name of the organization", max_length=512)
    member_count = models.PositiveIntegerField()
    liquid_nuyen = models.CharField()
    illegal = models.BooleanField(default=True)
    owner = models.ForeignKey(chars.Character_Sheet)
    GroupType = models.TextChoices("Gang", "Secret Organisation", "Corp", "AAA-Corp")
    type = models.CharField(blank=True, choices=GroupType.choices)


    def __str__(self):
        return self.username

class Assets(base_model):
    influence_value = models.SmallIntegerField(default=0, blank=False, help_text="The influence value of a person to an group, from -10 to 10")
    groups = models.ForeignKey(Group, on_delete = models.CASCADE, related_name="incluences")
    contact = models.ForeignKey(cont.Contact, on_delete = models.CASCADE, related_name="incluences")
    InfluenceType = models.TextChoices("Owner", "Worker", "Customer", "Stakeholder")
    type = models.CharField(blank=True, choices=InfluenceType.choices)

class Nickname(base_model):
    name = models.CharField("Nickname", max_length=512)
    contact = models.ForeignKey(cont.Contact, on_delete = models.CASCADE, related_name="incluences")