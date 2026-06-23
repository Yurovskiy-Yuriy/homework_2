from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

# проверка на наличие основогого раздела
class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        
        main_count = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_main'):
                    main_count += 1
        
        if main_count == 0:
            raise ValidationError('Должен быть выбран один основной раздел')
        elif main_count > 1:
            raise ValidationError('Основной раздел может быть только один')
        
        return self.cleaned_data


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1
    fields = ['tag', 'is_main']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'published_at']
    list_filter = ['published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
