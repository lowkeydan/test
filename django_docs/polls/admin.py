from django.contrib import admin
from .models import Question, Choice, Person, Person2, Group, Membership
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QueAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_data', 'author',)
    #list_display_links = ('id', 'question_text')
    ordering = ('pub_data', )
    list_filter = ['pub_data']
    search_fields = ['question_text']
    date_hierarchy = 'pub_data'
    list_editable = ['question_text']
    fieldsets = [

        ('问题选项', {'fields': ('pub_data', 'question_text', 'author', 'email'), 'classes': (
            'collapse')}),
    ]
    inlines = [ChoiceInline]



admin.site.register(Question, QueAdmin)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Person2)
admin.site.register(Membership)