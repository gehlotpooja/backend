from django.db import models

# Create your models here.
class LobbyDetails(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    member_size = models.SmallIntegerField(null=True,blank=True)
    winner = models.CharField(max_length=50,null=True,blank=True)
    entry_fee = models.SmallIntegerField(null=True,blank=True)
    house_charges = models.FloatField(null=True,blank=True)

    class Meta:
        db_table = 'tbl_lobby_details'

class LobbyMembers(models.Model):
    lobby = models.ForeignKey(LobbyDetails,on_delete=models.DO_NOTHING)
    member_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_lobby_members'