from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    video=models.FileField(upload_to='videos/')
    img=models.ImageField(upload_to='pics/thumbnails',null=True,blank=True)

    def __str__(self):
        return self.title

    def delete(self,*args,**kargs):
        self.video.delete()
        self.img.delete()
        super().delete(*args,**kargs)