from django.contrib import admin

# Register your models here.

from .models import ( 
                        Subject,Topic,Learn,
                        )

class AdminLearns(admin.ModelAdmin):
    fieldsets = (
        ("Lession", {
            "fields": ['topic','lession_type','lession'],
        }),
    )

admin.site.register(Learn,admin_class=AdminLearns)

class AdminTopic(admin.ModelAdmin):
    fieldsets = (
        ("Topic", {
            "fields": ['subject','topic_name'],
        }),
    )


admin.site.register(Topic,admin_class=AdminTopic)
    
class AdminSubject(admin.ModelAdmin):
    fieldsets = (
        ("Subject Name", {
            "fields": ['name'],
        }),
    )
    
admin.site.register(Subject,admin_class=AdminSubject)