from django.db import models


class GetOrNoneManager(models.Manager):
    """ Менеджер ORM """

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class Network(models.Model):
    """Модель торговой сети"""
    title = models.CharField(max_length=150, verbose_name='Название сети')

    class Meta:
        verbose_name = "Торговая сеть"
        verbose_name_plural = "Торговые сети"

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=25)
    model = models.CharField(verbose_name='Модель продукта', max_length=100)
    release_date = models.DateField(verbose_name='Дата выхода на рынок', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Company(models.Model):
    """ Модель компаний """
    TYPES = [
        ('ЗВД', 'Завод'),
        ('ДСТ', 'Дистрибьютор'),
        ('ДЛР', 'Дилерский центр'),
        ('КРС', 'Крупная розничная сеть'),
        ('ИП', 'Индивидуальный предприниматель')
    ]
    type = models.CharField(max_length=3, verbose_name='Тип компании', choices=TYPES)
    hierarchy = models.PositiveSmallIntegerField(verbose_name='Уровень в иерархии', default=0)
    network = models.ForeignKey(Network, verbose_name="Торговая сеть", on_delete=models.CASCADE,
                                related_name="companies")
    name = models.CharField(verbose_name='Название компании', max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    country = models.CharField(verbose_name='Название страны', max_length=100)
    city = models.CharField(verbose_name='Название города', max_length=100)
    street = models.CharField(verbose_name='Название улицы', max_length=100)
    building_number = models.CharField(verbose_name='Номер дома', max_length=50)
    products = models.ManyToManyField(Product, related_name='companies')
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        related_name='traders',
        null=True,
        blank=True,
    )
    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Задолженность',
        blank=True,
        default=0
    )
    created_date = models.DateField(auto_now_add=True)

    objects = GetOrNoneManager()

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name

