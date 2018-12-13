from django.db import models


class Compress(models.Model):
    image =models.ImageField(upload_to='images')
class CompressedImage(models.Model):
    new_compressed_image=models.ImageField(upload_to='generated_images')
