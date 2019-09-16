from django.contrib import admin

from .models import Planet, Rookie, Sith, Questions, BlackHandTest, Answers

# Register your models here.
admin.site.register(Planet)
admin.site.register(Rookie)
admin.site.register(Sith)
admin.site.register(Questions)
admin.site.register(BlackHandTest)
admin.site.register(Answers)