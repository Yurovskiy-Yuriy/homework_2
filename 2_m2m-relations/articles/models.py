from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    tags = models.ManyToManyField(
        Tag,
        through='Scope',
        through_fields=('article', 'tag'),
        related_name='articles',
        verbose_name='Разделы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Связь статьи и раздела'
        verbose_name_plural = 'Связи статьи и разделов'
        # Чтобы избежать дублирования связей
        unique_together = [['article', 'tag']]
        ordering = ['-is_main', 'tag__name']  # Сначала основные, потом по алфавиту

    def __str__(self):
        return f'{self.article.title} - {self.tag.name}'