from django.db import models
from mptt import models as mptt_models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return "{}".format(self.name)


class Profile(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='Роль', null=True)


class Level(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Structure(mptt_models.MPTTModel):
    name = models.CharField(max_length=100)
    parent = mptt_models.TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    position = models.IntegerField(null=True, blank=True)
    structure_level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.name

    def get_descendant_structures_users(self):
        structures = self.get_descendants()
        users = Profile.objects.filter(structureuser__structure__in=structures)
        return users


class StructureUser(models.Model):
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.structure.name + ' - ' + self.user.username

