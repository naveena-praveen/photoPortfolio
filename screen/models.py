from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db import models
from django.urls import reverse

class Work(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Work_details(models.Model):
    work = models.ForeignKey(Work, related_name='details', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='work_images')
    description = models.TextField()

    class Meta:
        ordering = ('work',)
        verbose_name = 'Work Detail'
        verbose_name_plural = 'Work Details'

    def get_url(self):
        return reverse('details', args=[self.work.slug, self.id])

    def __str__(self):
        return f"{self.work.name} - {self.id}"



class Art(models.Model):
    image = models.ImageField(upload_to='work_images')
    description = models.TextField(blank=True, null=True)  

    class Meta:
        verbose_name = 'art'
        verbose_name_plural = 'arts'

    def __str__(self):
        if self.description:
            return self.description[:20]  
        return "No description"

    def get_url(self):
        return reverse('art_detail', args=[self.id])

class LoveAndWar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    side_image = models.ImageField(upload_to='work_images')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LoveAndWarImage(models.Model):
    love_and_war = models.ForeignKey(LoveAndWar, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='work_images')

    def __str__(self):
        return f"Image for {self.love_and_war.title}"
    
class Itswhatido(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    side_image = models.ImageField(upload_to='work_images')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'its what i do'
        verbose_name_plural = 'its what i do'

    def __str__(self):
        return self.title


class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Exhibition'
        verbose_name_plural = 'Exhibitions'

    def __str__(self):
        return self.title
    
class Awards(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    title2= models.CharField(max_length=200,null=True)
    title2description=models.TextField(null=True)
    title3=models.CharField(max_length=200,null=True)
    title3description=models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Awards and Education'
        verbose_name_plural = 'Awards and Educations'

    def __str__(self):
        return self.title
    

class Bio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Biography'
        verbose_name_plural = 'Biography'

    def __str__(self):
        return self.title