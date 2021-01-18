from django.contrib import admin

# Register your models here.
from .models import (ProgrammingLanguage,ProgramSolutions,Comment,Question,)



class AdminSolution(admin.ModelAdmin):
    fieldsets = (
        ("Solution",{
            "fields":['program_question',"solution_code"]
        }),
    )

admin.site.register(ProgramSolutions,AdminSolution)

class AdminQuestion(admin.ModelAdmin):
    fieldsets = (
        ('Question', {
            "fields": ['programming_language','question_text'],
        }),
    )

admin.site.register(Question,AdminQuestion)


class AdminProgrammes(admin.ModelAdmin):
    fieldsets = (
        ("Language", {
            "fields": 
                ['language_name']
        }),
    )

admin.site.register(ProgrammingLanguage,AdminProgrammes)



class AdminComment(admin.ModelAdmin):
    fieldsets = (
        ('Comment', {
            "fields": ['program_solution','comment_text'],
        }),
    )
    
admin.site.register(Comment,admin_class=AdminComment)