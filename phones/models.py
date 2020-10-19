from django.db import models
from django.template.defaultfilters import slugify


# каждая таблица - это класс. Поля таблицы - тоже классы с суффиксом Field
class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # создаем модель Phone
    # с полями id, name, price, image, release_date, lte_exists и slug.
    # Поле id - должно быть основным ключом модели.
    name = models.CharField(max_length=40, unique=True)
    price=models.FloatField()
    # ссылка на файл
    image=models.TextField()
    release_date=models.DateField()
    lte_exists=models.BooleanField()
    # Значение поля slug будет устанавливаться слагифицированным значением поля name
    slug=models.SlugField(max_length=250)

    # возврат понятного отображения заголовка в панель администрирования
    def __str__(self):
        return f'{self.id} - {self.name}'

    # здесь переопределяем save - цель оформить slug (ЧПУ)
    def save(self, *args, **kwargs):
        # фишка в том, чтобы сгенерировать слаг только один раз при создании нового объекта:
        if not self.id:
            # Newly created object, so set slug
            # устанавливается слагифицированное значение поля name
            self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)
