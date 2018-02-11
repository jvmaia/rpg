from django.db import models


from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=255)

    player_only = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        return f"room-{self.id}"
