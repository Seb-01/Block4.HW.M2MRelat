from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleScopes


def articles_list(request):
    template = 'articles/news.html'

    art=Article.objects.order_by('-published_at').prefetch_related('scopes')
    #art=ArticleScopes.objects.prefetch_related('article')
    #art = Article.objects.prefetch_related('scopes')

    #проверка
    # print(art)
    # for one_art in art:
    #     print(one_art)
    #     print(one_art.title, one_art.text)
    #     #rasdel=one_art.scope_set.all()
    #     #print(rasdel)
    #     #for r in rasdel:
    #     #    print(r.title)
    #
    #     sc=one_art.articlescopes_set.all()
    #     print(sc)
    #     for one_sc in sc:
    #         print(one_sc.scope.title)
    #         print(one_sc.is_main)


    #print(art.text)

    # for val in art:
    #     print(val.is_main)
    #     print(val.article.title)
    #     print(val.article.text)
    #     print(val.article.published_at)
    #     sc=val.article.scopes.all()
    #
    #     print(sc)
    #
    #     for razdel in sc:
    #         print(razdel.title)

    context = {'object_list': art}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    #ordering = '-published_at'

    return render(request, template, context)
