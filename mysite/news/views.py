from django.shortcuts import render
from django.http import HttpResponse


def index(reques):
    return HttpResponse('Hello world')


def test(reques):
    return HttpResponse('Тестовая страница')