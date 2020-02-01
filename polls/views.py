from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import uuid,hashlib
import os
from mysite import settings

def get_unique_str():
    uuid_str = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()

def index(req):
    if req.method == 'GET':
        return render(req,'mybook.html')
    else:
        name = req.POST.get('name')
        myfile = req.FILES.get('icon')
        filename = get_unique_str()+'.'+myfile.name.split('.')[-1]

        # 文件路径
        filepath = os.path.join(settings.MEDIA_ROOT,filename)
        f = open(filepath,'wb')
        for i in myfile.chunks():
            f.write(i)
        f.close()
        return HttpResponse('OK')

def good(req):
    if req.method == 'POST':
        iFile = req.FILES.get('inputFile')
        iAlgorithm = req.POST.get('inputAlgorithm')
        return HttpResponse("get file name is " + iFile.name + ", algorithm is " + iAlgorithm);
