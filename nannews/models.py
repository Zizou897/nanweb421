from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Contact(models.Model):
    nom = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom


class Newsletter(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email


class Team(models.Model):
    nom = models.CharField( max_length=250)
    prenom = models.CharField(max_length=250)
    models.FileField( upload_to="image_team")
    job = models.CharField(max_length=150)
    social = models.ForeignKey("nannews.Social",related_name="team_social", on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.nom


class Site(models.Model):
    nom_site = models.CharField(max_length=250)
    phone = models.ForeignKey("nannews.Phone", related_name="site_phone", on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    copy_ryght = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
	

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Site"

    def __str__(self):
        return self.nom_site

class Phone(models.Model):
	telephone = models.CharField(max_length=50)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Telephone"
		verbose_name_plural = "Telephones"

class Social(models.Model):
	nom = models.CharField(max_length=250)
	icon = models.CharField(max_length=250)
	link = models.URLField(max_length=200)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Social"
		verbose_name_plural = "Sociaux"
	
	def __str__(self):
		return self.nom
