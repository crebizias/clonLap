from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요, 설문사이트 첫 화면입니다.")

