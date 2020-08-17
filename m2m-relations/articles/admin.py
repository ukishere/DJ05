from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags, Tagging


class TaggingInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags_count = 0
        for form in self.forms:
            if form.cleaned_data['main_tag']:
                main_tags_count += 1
            if main_tags_count > 1:
                raise ValidationError('Может быть только один главный тэг')
            elif main_tags_count < 1:
                raise ValidationError('Укажите основной тэг')
        return super().clean()

class TaggingInline(admin.TabularInline):
    model = Tagging
    formset = TaggingInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TaggingInline
    ]

class TagsAdmin(admin.ModelAdmin):
    pass

class TaggingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tags, TagsAdmin)