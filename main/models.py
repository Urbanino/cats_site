from django.db import models
from django.shortcuts import reverse

class Cat(models.Model):
    """Model definition for Cat."""
    name = models.CharField(max_length = 100, 
                                    verbose_name = 'Имя')
    birthday = models.DateField(verbose_name = 'Дата рождения', blank=True, null=True)
    photo = models.ImageField(verbose_name = 'Фото')
    description = models.TextField(max_length = 250, 
                                    verbose_name = 'Описание', blank=True, null=True)

    parent1 = models.ForeignKey(to = "Cat", on_delete = models.DO_NOTHING, related_name= 'Mom',  verbose_name = 'Мама', blank=True, null=True)
    parent2 = models.ForeignKey(to = "Cat", on_delete = models.DO_NOTHING, related_name= 'Dad',  verbose_name = 'Папа', blank=True, null=True )

    sale = models.BooleanField(blank=True, null=True,  verbose_name = 'На продажу?')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Cat."""

        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'

    def __str__(self):
        """Unicode representation of Cat."""
        return self.name

    def get_absolute_url(self):
        return reverse("cat_detail_url", kwargs={"cat_id": self.pk})

class Cat_Photo(models.Model):
    """Model definition for Cat_Photo."""
    image = models.ImageField(verbose_name = 'Фото')
    fk_cat = models.ForeignKey(Cat, on_delete=models.CASCADE, verbose_name = 'Кот')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Cats_Photo."""

        verbose_name = 'Фото котов'
        verbose_name_plural = 'Фото котов'

    def __str__(self):
        """Unicode representation of Cats_Photo."""
        return self.fk_cat.name


# Create your models here.
