import datetime
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template


def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
    dic = {
        'current_date':current_date,
        'title':'wuxiaolei'
    }
    #t = get_template('current_datetime.html')
    #html = t.render({'current_date':now})
    #return HttpResponse(html)
    #render_to_response:渲染模板并自动调用HttpResponse
    #return render_to_response('mypage.html',locals())
    #locals()：自动调用局部变量拼装成的字典，上面语句中locals()={‘current_date':datetime.datetime.now()}
    return render_to_response('child/current_datetime.html',dic)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

    html = "<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)