from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)