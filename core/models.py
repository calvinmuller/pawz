from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe


class Status(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    address = models.TextField()
    telephone = models.TextField()
    email = models.EmailField()
    logo = models.ImageField(upload_to='organisations')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    can_donate = models.BooleanField()
    featured = models.BooleanField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organisation, self).save(*args, **kwargs)



class OrganisationImage(models.Model):
    property = models.ForeignKey(Organisation, related_name='images',  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='organisations')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.image)


#
 # `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 #  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 #  `organisation_id` int(10) unsigned NOT NULL,
 #  `created_at` timestamp NULL DEFAULT NULL,
 #  `updated_at` timestamp NULL DEFAULT NULL,
 #  `picture` text COLLATE utf8mb4_unicode_ci NOT NULL,
 #  `colour` int(10) unsigned NOT NULL,
 #  `breed` int(10) unsigned NOT NULL,
 #  `breed_other` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 #  `likes` text COLLATE utf8mb4_unicode_ci,
 #  `date_of_birth` date DEFAULT NULL,
 #  `found_at` date DEFAULT NULL,
 #  `adopted_at` date DEFAULT NULL,
 #  `can_donate` tinyint(1) NOT NULL DEFAULT '1',
 #  `can_adopt` tinyint(1) NOT NULL DEFAULT '1',
 #  `favorite_toy` text COLLATE utf8mb4_unicode_ci,
 #  `favorite_food` text COLLATE utf8mb4_unicode_ci,


class Paw(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    organisation = models.ForeignKey('Organisation', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='paw')
    colour = models.ForeignKey('Colour', on_delete=models.CASCADE)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)

    breed_other = models.CharField(max_length=255, blank=True)

    can_donate = models.BooleanField(default=False)
    can_adopt = models.BooleanField(default=False)

    favourite_toy = models.TextField(blank=True)
    favourite_food = models.TextField(blank=True)

    date_of_birth = models.DateField(blank=True, null=True)
    found_at = models.DateField(auto_now=True, blank=True, null=True)
    adopted_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {}".format(self.name, self.breed)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Paw, self).save(*args, **kwargs)


class PawImage(models.Model):
    property = models.ForeignKey(Paw, related_name='images',  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='paws')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.image)


class Colour(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='colours', blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Breed(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='colours', blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
