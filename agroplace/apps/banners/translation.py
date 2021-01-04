from modeltranslation.translator import register, TranslationOptions
from .models import MainBanners


@register(MainBanners)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title',)

