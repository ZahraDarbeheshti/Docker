from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'dob', 'created_at')
    list_filter = ('dob',)
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)

    def get_readonly_fields(self, request, obj=None):
        """Ensure readonly_fields are dynamic based on the object state."""
        if obj:  # If editing an existing object
            return self.readonly_fields
        return ()
