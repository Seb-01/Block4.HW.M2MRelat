#from django.contrib import admin
#from .models import Article

#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass


from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScopes


class ArticleScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        #self.forms
        main_scope_counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить


            #здесь делается проверка на несколько главных разделов

            print(form.cleaned_data)
            # если словарь не пустой
            if len(form.cleaned_data) and form.cleaned_data['is_main'] == True:
                main_scope_counter +=1

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if main_scope_counter > 1:
                raise ValidationError('Основным может быть только один раздел')
            if main_scope_counter == 0:
                raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopesInline(admin.TabularInline):
    model = ArticleScopes
    formset = ArticleScopesInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopesInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleScopes)
class ArticleScopesAdmin(admin.ModelAdmin):
    pass