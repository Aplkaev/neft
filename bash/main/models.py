from django.db import models
# Create your models here.


class ModelArticle(models.Model):
    text = models.TextField()
    date_create = models.DateTimeField(auto_now=True)



class ModelFile(models.Model):
    name = models.TextField()
    token = models.TextField()
    bin_file = models.BinaryField()
    date_create = models.DateTimeField(auto_now=True)



class ModelArticleFile(models.Model):
    article = models.ForeignKey(ModelArticle, on_delete=models.CASCADE)
    file = models.ForeignKey(ModelFile, on_delete=models.CASCADE)
    