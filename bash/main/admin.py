from django.contrib import admin
from .models import ModelFile, ModelArticle, ModelArticleFile

# Register your models here.


admin.site.register(ModelFile)
admin.site.register(ModelArticle)
admin.site.register(ModelArticleFile)