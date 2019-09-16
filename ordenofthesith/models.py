from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Planet(models.Model):
    """ Задается модель для планеты """
    name = models.CharField(max_length=80, verbose_name='Название планеты')

    class Meta:
        verbose_name_plural = 'Планеты'
        verbose_name = 'Планета'
    
    def __str__(self):
        return self.name

class Sith(models.Model):
    """ Модель для ситха """
    name = models.CharField(max_length=80, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')

    class Meta:
        verbose_name_plural = 'Ситхи'
        verbose_name = 'Ситх'

    def __str__(self):
        return self.name

class Rookie(models.Model):
    """ Создаем модель для рекрута, поле ситх принимает пустое значение """
    name = models.CharField(max_length=80, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта')
    sith = models.ForeignKey(Sith, null=True, on_delete=models.CASCADE, verbose_name='Ситх')

    class Meta:
        verbose_name_plural = 'Рекруты'
        verbose_name = 'Рекрут'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Переходим по заданному url, передавая словарь с данными для формы """
        return reverse('ordenofthesith:blackHandTest', kwargs={'rookie_id': self.id, 'planet_id': self.planet_id})

class Questions(models.Model):
    """ Модель для вопросов """
    content = models.CharField(max_length=240, verbose_name='Вопрос')

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'

    def __str__(self):
        return self.content[:50]

class BlackHandTest(models.Model):
    """ Модель тестового испытания черной руки """
    planet = models.OneToOneField(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    questions = models.ManyToManyField(Questions, verbose_name='Вопросы')

    class Meta:
        verbose_name_plural = 'Тест Черной руки'
        verbose_name = 'Тест Черной руки'

    def __str__(self):
        return f'Тест с планеты {str(self.planet)}'

class Answers(models.Model):
    """ Модель для ответов """
    rookie = models.ForeignKey(Rookie, on_delete=models.CASCADE, verbose_name='Рекрут')
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name='Вопрос')
    content = models.NullBooleanField(verbose_name='Ответ')

    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'

    def __str__(self):
        return f'Ответ на вопрос "{self.questions}" от {self.rookie}'