

# Register your models here.
from django.contrib import admin
from .models import Task  # Импортируем вашу модель


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Поля, которые будут видны в списке
    list_display = ('title', 'completed', 'created_at')

    # Поля, по которым можно фильтровать (появятся справа)
    list_filter = ('completed', 'created_at')

    # Поля, по которым работает поиск (сверху)
    search_fields = ('title', 'description')

    # Возможность редактировать поле completed прямо в списке, не заходя внутрь задачи
    list_editable = ('completed',)
