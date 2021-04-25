from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UploadFileForm
from .models import ModelFile, ModelArticle, ModelArticleFile
import zipfile
import hashlib
import datetime


# класс для обертки файлов zip 
# TODO: не придумал куда его убрать
class CustomFile:
    

    def __init__(self, name, file):
        self.name = name
        self.file = file.read(name)


    def read(self):
        return self.file


# для отображения формы из index.html
def index(request):
    form = UploadFileForm()
    return render(request, 'main/index.html',{'form':form})


# для загрузки файла и формы
def upload_file(request):

    # обрабатываем post запрос 
    if request.method == 'POST':
        if(request.FILES):


            # загрузка файла
            upload_file = []


            # один файл - один запрос
            # в случае передачи архива приходить больше файлов
            # оборачиваем файл из request в массив
            files = [request.FILES.get('file')]

            # провека в название .zip
            if '.zip' in files[0].name[-4:]:
                # разархивируем zip
                with zipfile.ZipFile(files[0]) as zip_ref:
                    data = []
                    # создать массив с файлами из архива
                    for ref in zip_ref.namelist():
                        data.append(CustomFile(ref, zip_ref))
                    del files
                    # пересоздаем files для записи в модель
                    files = []
                    for d in data:
                        # пропускаем папки
                        if len(d.file) == 0:
                            continue
                        
                        files.append(d)


            # записываем файлы
            for file in files:
                hash = hashlib.md5((file.name + str(datetime.datetime.now().timestamp())).encode('utf-8'))
                model_file = ModelFile(
                    name = file.name,
                    bin_file = file.read(), 
                    token = hash.hexdigest())
                model_file.save()
                # записываем все хэши файлов для ModelArticle
                upload_file.append(model_file.token)

            return JsonResponse({'result':{
                'success':True,
                'data':upload_file
            }})
            pass
        else:
            # загрузка дополнительной информации
            # создаем запись с текстом
            article = ModelArticle(text=request.POST['about'])
            article.save()

            # получаем id, только что добавленной записи
            article_id = article.id

            # список token файлов 
            files = request.POST.getlist('files[]')
            model_file = []
            for f in files:
                # получаем записи файлов по token
                _f = ModelFile.objects.get(token=f)
                model_file.append(_f)

            # создаем запись для связи файла и записи с информацией 
            for f in model_file:
                article_file = ModelArticleFile(article=article, file=f)
                article_file.save()


            # переходим на главную страницу
            return redirect('/')
        
    return JsonResponse({'result':'error'})


# логи загрузок
def log(request):
    # получаем сортирование записи по дате, если даже без файлов
    artciles = ModelArticle.objects.order_by('-date_create')
    for artcile in artciles:
        # получаем файлы к это записи
        artcile_file = ModelArticleFile.objects.filter(article=artcile)
        artcile.file = artcile_file

    return render(request, 'main/log.html',{'data':artciles})