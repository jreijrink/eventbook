from django.contrib import admin

# Register your document here.

from .models import Tag, Url, Document

admin.site.register(Tag)
admin.site.register(Url)
admin.site.register(Document)