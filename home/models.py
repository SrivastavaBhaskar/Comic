from django.db import models
from django.utils.text import slugify

# Create your models here.
def comic_directory_path(instance, comic):
    comic_ext = comic.split('.')[-1]
    slug_name = slugify(instance.name)
    return f'{slug_name}/display_image.{comic_ext}' 

class Comic(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=comic_directory_path, blank=True)
    description = models.TextField(max_length=500)
    rating = models.FloatField(default=0.0)
    total_reviews = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=150, blank=True)
    chapter_number = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

def chapter_directory_path(instance, page):
    chapter = Chapter.objects.get(id=instance.chapter.id)
    comic = chapter.comic
    new_file_name = f'{instance.page_number}'
    slug_name = slugify(comic.name)
    page_ext = page.split('.')[-1]
    return f'{slug_name}/{chapter.id}/{new_file_name}.{page_ext}'

class Page(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='pages')
    image = models.ImageField(upload_to=chapter_directory_path)
    page_number = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
