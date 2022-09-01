from django.contrib import admin
from products.admin import BasketAdminInline

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
