from django.contrib import admin

# Register your models here.
from phones.models import Phone

class PhoneAdmin(admin.ModelAdmin):
    pass

#Создаем интерфейсы для создания/удаления и редактирования сущностей
admin.site.register(Phone,PhoneAdmin)
