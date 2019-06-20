"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.urls import path
from django.http import HttpResponse
from views import index, about

urlpatterns = [
    path('', index),
    path('about', about),
]