from inspect import Attribute
from utils import base_model
from django.db import models
from groups import models as groups
from contacts import models as cont

class Base_Attribute(base_model):
    AttributeType = models.TextChoices("body", "agility", "reaction", "strength", "willpower", "logic", "intuition", "charisma", "edge", "magic", "essence", "initiative", "ressonance")
    attribute = models.CharField(blank=True, choices=AttributeType.choices)
    description = models.CharField



class Character_Attribute(base_model):
    attribute = models.ForeignKey(Base_Attribute, on_delete = models.CASCADE)
    value = models.PositiveSmallIntegerField
    modifier = models.PositiveSmallIntegerField
    notes = models.CharField

class Base_Skill(base_model):
    primary_attribute = models.ForeignKey(Character_Attribute, on_delete = models.CASCADE, related_name="primary_skills")
    secondary_attribute = models.ForeignKey(Character_Attribute, on_delete = models.CASCADE, related_name="primary_skills")

class Character_Skill(base_model):
    attribute = models.ForeignKey(Base_Skill, on_delete = models.CASCADE)
    value = models.PositiveSmallIntegerField
    modifier = models.PositiveSmallIntegerField
    notes = models.CharField

class Character_Sheet(base_model):
    name = models.CharField("Name of the character", max_length=1024)
    attributes = models.ForeignKey(Character_Attribute, on_delete = models.CASCADE)
    skills = models.ForeignKey(Character_Skill, on_delete = models.CASCADE)
    groups = models.ForeignKey(groups.Group, on_delete = models.CASCADE, related_name="members")

    def __str__(self):
        return self.username


class Licence(base_model):
    LicenseType = models.TextChoices("Small Arms", "Heavy Arms", "Cyberdeck", "Drivers Licence", "Military Equipment", "Worker License")
    type = models.CharField(blank=True, choices=LicenseType.choices)
    notes = models.CharField("Details about the License")

class Identities(base_model):
    name = models.CharField("Name of the identity", max_length=1024)
    valid = models.BooleanField
    fake_identity = models.BooleanField
    quality = models.PositiveSmallIntegerField("Quality of the forged identity")
    licences = models.ForeignKey(Licence, on_delete = models.CASCADE, related_name="incluences")
    character = models.ForeignKey(Character_Sheet, on_delete = models.CASCADE, related_name="incluences")

