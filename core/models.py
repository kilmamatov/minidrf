from django.db import models


class Address(models.Model):
    city = models.CharField('Город', max_length=100)
    street = models.CharField('Улица', max_length=100)
    house_number = models.CharField('Дом', max_length=20)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house_number}'


class University(models.Model):
    name = models.CharField('Название', max_length=100)
    address = models.OneToOneField(Address, verbose_name='Адрес', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вуз'
        verbose_name_plural = 'Вузы'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Название', max_length=100)
    staff_count = models.IntegerField('Количетсво сотрудников', )

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    def __str__(self):
        return self.name


class Professor(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100)
    birth_year = models.DateField('Дата рождения', )
    department = models.ForeignKey(Department, verbose_name='Кафедра', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профессор'
        verbose_name_plural = 'Профессора'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

