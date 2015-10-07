from django.contrib import admin

# Register your document here.

from .models import Token, Url, Document

admin.site.register(Token)
admin.site.register(Url)
admin.site.register(Document)