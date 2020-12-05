from django.http import JsonResponse
from django.shortcuts import render

from .models import Cube


def index(request):
    cub1 = Cube.objects.get_or_create(pk='1')[0]
    cub1.value = 0
    cub1.save()

    cub2 = Cube.objects.get_or_create(pk='2')[0]
    cub2.value = 0
    cub2.save()
    return render(request, 'home.html', context={"cub1": cub1, "cub2": cub2})


def add(request):
    val = request.GET["val"]
    cub = request.GET["cub"]
    cub = Cube.objects.get(pk=cub)
    cub.value = cub.value + int(val)
    cub.save()
    return JsonResponse({"val": cub.value})
