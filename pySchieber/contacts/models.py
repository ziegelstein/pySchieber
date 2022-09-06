from utils import base_model
from django.db import models
from characters import models as chars
from groups import models as groups


class Contact(base_model):
    character_sheet = models.ForeignKey(chars.Character_Sheet, on_delete = models.CASCADE)
    groups = models.ForeignKey(groups.Group, on_delete = models.CASCADE, related_name="members")

    def __str__(self):
        return self.username

class Influence(base_model):
    influence_value = models.SmallIntegerField(default=0, blank=False, help_text="The influence value of a person to an group, from -10 to 10")
    groups = models.ForeignKey(groups.Group, on_delete = models.CASCADE, related_name="incluences")
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE, related_name="incluences")
    InfluenceType = models.TextChoices("Owner", "Worker", "Customer", "Stakeholder")
    type = models.CharField(blank=True, choices=InfluenceType.choices)

class Nickname(base_model):
    name = models.CharField("Nickname", max_length=512)
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE, related_name="nicknames")

class Relationship(base_model):
    relationship_value = models.SmallIntegerField(default=0, blank=False, help_text="The relationship value of a person to an group, from -10 to 10")
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE, related_name="relationships")
    character = contact = models.ForeignKey(chars.Character_Sheet, on_delete = models.CASCADE, related_name="relationships")
