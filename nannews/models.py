from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Base(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Contact(Base):
    nom = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom


class Newsletter(Base):
    email = models.EmailField()

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email


class Team(Base):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    image = models.FileField(upload_to="image_team")
    job = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.nom


class Site(Base):
    nom_site = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    image = models.FileField(upload_to="image_site")
    copy_ryght = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Site"

    def __str__(self):
        return self.nom_site


class Phone(Base):

    telephone = models.CharField(max_length=50)
    site = models.ForeignKey(
        "nannews.Site", related_name="site_phone", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Telephone"
        verbose_name_plural = "Telephones"


class Social(Base):
    nom = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Sociaux"

    def __str__(self):
        return self.nom


class SocialUser(Base):
    link = models.URLField(max_length=200)
    social = models.ForeignKey(
        "nannews.Social",related_name="team_social", on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        "nannews.Team", related_name="team_social", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Social_User"
        verbose_name_plural = "Social_Users"

    def __str__(self):
        return self.link


class Config(Base):
    nom_history = models.CharField(max_length=150)
    history = models.TextField()
    titre_description = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return self.nom_history
