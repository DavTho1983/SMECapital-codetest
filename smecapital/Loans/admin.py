from django.contrib import admin
from .models import Loans


@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    def _allow_edit(self, request, obj=None):
        if not obj:
            return True
        return not (request.user.is_staff or request.user.is_superuser)

    def has_change_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_delete_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    list_display = (
        "borrower",
        "approved",
        "start_date",
    )
    ordering = ["start_date"]