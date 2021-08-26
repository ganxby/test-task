from django.contrib import admin
from .models import (
    User,
    Address,
    Geo,
    Company,
    Post
)

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(Company)
admin.site.register(Post)