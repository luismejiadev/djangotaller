from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    readonly_fields = ['votes', 'stats_votes']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question', 'votes']


class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ['id', 'question_text', 'pub_date']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
