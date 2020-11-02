from django.db import models
#from django.db.models.enums import TextChoices

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField('Scope', through='ArticleScopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

#выбор разделов
# class Section(models.TextChoices):
#     CULTURE = "CULTURE", "Культура"
#     CITY = "CITY", "Город"
#     HEALTH="HEALTH","Здоровье"
#     SCIENCE="SCIENCE","Наука"
#     INTERRELATION="INTERRELATION","Международные отношения"


SCOPE_CHOICES = [
    ('CULTURE', 'Культура'),
    ('CITY', 'Город'),
    ('HEALTH', 'Здоровье'),
    ('SCIENCE', 'Наука'),
    ('INTERRELATION', 'Международные отношения'),
    ('SPACE', 'Космос'),
]

class Scope(models.Model):
    # выбор разделов
    # class Section(models.TextChoices):
    #     CULTURE = "CULTURE", "Культура"
    #     CITY = "CITY", "Город"
    #     HEALTH = "HEALTH", "Здоровье"
    #     SCIENCE = "SCIENCE", "Наука"
    #     INTERRELATION = "INTERRELATION", "Международные отношения"

    # title = models.TextField(
    #     blank=True,
    #     default='',
    #     choices=Section.choices, verbose_name='Раздел')

    title = models.CharField(max_length=50, choices=SCOPE_CHOICES, verbose_name='Раздел статьи')
    #mtm = models.ManyToManyField('Article', through='ArticleScopes')
    #title=models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Раздел статьи'
        verbose_name_plural = 'Разделы статей'

    def __str__(self):
        return self.title

class ArticleScopes(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    scope = models.ForeignKey('Scope', on_delete=models.CASCADE)
    # нужно значение по умолчанию обязательно!
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    def __str__(self):
        return f'{self.article} -> {self.scope}'

    class Meta:
        verbose_name = 'Раздел и статья'
        verbose_name_plural = 'Разделы и статьи'