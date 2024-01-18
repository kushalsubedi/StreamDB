from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Content_Type(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Content(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ttitle = models.CharField(max_length=255)
    content_rating = models.FloatField()
    description = models.TextField()
    content_type = models.ForeignKey(Content_Type, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Thumbnail(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    thumbnail = models.ForeignKey(Thumbnail, on_delete=models.CASCADE)
    duration = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    audio_language = models.CharField(max_length=255)
    subtitle_language = models.CharField(max_length=255)
    video_rating = models.FloatField()

    def __str__(self):
        return self.content.title
