from django.http import HttpResponse, Http404
import time

from time import strftime

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sceneImgUpload(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            path = "static/images/upload/" + time.strftime("%Y%m%d%H%M%S",time.localtime())
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")  
            for chunk in f.chunks():
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception, e:
            print e
        res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"
        return HttpResponse(res)
    else:
        raise Http404()