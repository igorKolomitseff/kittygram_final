from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название достижения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name[:50]


class Cat(models.Model):
    name = models.CharField(max_length=16, verbose_name='Кличка кота')
    color = models.CharField(max_length=16, verbose_name='Цвет кота')
    birth_year = models.IntegerField(verbose_name='Год рождения кота')
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE,
        verbose_name='Владелец кота'
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat',
        verbose_name='Достижения кота'
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None,
        verbose_name='Изображение кота'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'кот'
        verbose_name_plural = 'Коты'

    def __str__(self):
        return (
            f'Кот {self.name}, {self.color}, '
            f'год рождения: {self.birth_year}'
        )


class AchievementCat(models.Model):
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        verbose_name='Достижение кота'
    )
    cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE,
        verbose_name='Кот'
    )

    class Meta:
        verbose_name = 'достижение кота'
        verbose_name_plural = 'Достижения кота'

    def __str__(self):
        return f'{self.achievement.name} - {self.cat.name}'
