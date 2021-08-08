from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)

    def __str__(self):
        return self.title

class PaidCourse(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    seats = models.IntegerField(blank=False, null=False)
    time = models.CharField(max_length=100, blank=False, null=False)
    money = models.IntegerField(blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

class Jamoamiz(models.Model):
    ism_familiyasi = models.CharField(max_length=100, blank=False, null=False)
    rasmi = models.ImageField(upload_to="images/", blank=False, null=False)
    lavozimi = models.CharField(max_length=100, blank=False, null=False)
    telefon_raqami = models.CharField(max_length=100, blank=False, null=False)
    telegram_manzili = models.CharField(max_length=100, blank=False, null=False)
    instagram_manzili = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.ism_familiyasi

class Fikrlar(models.Model):
    fikri = models.TextField(blank=False, null=False)
    ism_familiyasi = models.CharField(max_length=100, blank=False, null=False)
    rasmi = models.ImageField(upload_to="images/", blank=False, null=False)
    lavozimi = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.ism_familiyasi

class Manzil(models.Model):
    malumot = models.TextField(blank=False, null=False)
    joyi = models.CharField(max_length=300, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    telefon_raqami = models.CharField(max_length=100, blank=False, null=False)
    telegram_manzili = models.CharField(max_length=100, blank=False, null=False)
    instagram_manzili = models.CharField(max_length=100, blank=False, null=False)
    youtube_manzili = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.joyi


