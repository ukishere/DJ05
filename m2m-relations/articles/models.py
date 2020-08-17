from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(
        'Tags',
        through='Tagging'
    )

    class Meta:
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tags(models.Model):
    TAGS_CHOICES = [
        ('Здоровье', 'Здоровье'),
        ('Наука', 'Наука'),
        ('Город', 'Город')
    ]

    tag = models.TextField(
        choices = TAGS_CHOICES
    )

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag

class Tagging(models.Model):

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    tag = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE
    )

    main_tag = models.BooleanField()

    class Meta:
        unique_together = (('article','tag'),)
        db_table = 'articles_to_tags'

    def is_main(self):
        return self.main_tag