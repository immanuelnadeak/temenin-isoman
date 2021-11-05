<<<<<<< HEAD
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Result)
admin.site.register(Quiz)


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
=======
from django.contrib import admin
from .models import *

admin.site.register(Result)
admin.site.register(Quiz)


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
>>>>>>> 99d81d9a1038e3c401a758a44d449b85248bed7d
