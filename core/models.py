from django.db import models


class GalleryImg(models.Model):

    image = models.ImageField()


    def __str__(self):
        return str(self.pk)


class Comments(models.Model):
    img     = models.ForeignKey(GalleryImg, on_delete=models.CASCADE)
    comment = models.TextField(max_length=50)
    date    = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

