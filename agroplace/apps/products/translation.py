from modeltranslation.translator import register, TranslationOptions
from .models import Products, Categories


@register(Products)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Categories)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name',)
