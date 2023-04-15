from django.db import models


class MenuGroup(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Группа меню'

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название',
    )
    slug = models.CharField(max_length=256, verbose_name='Slug')
    first_level = models.BooleanField('Главный', null=True, blank=True)
    parent = models.ForeignKey(
        'Menu',
        on_delete=models.SET_NULL,
        related_name='menu_parent',
        null=True,
        blank=True
    )
    childes = models.ManyToManyField(
        'Menu',
        related_name='menu_childes',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        'MenuGroup',
        on_delete=models.SET_NULL,
        related_name='menu_group',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-group',)

    def __str__(self):
        return self.name
