from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Course, Category

from django import forms
from ckeditor_uploader.widgets \
    import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'


fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_Date', 'updated_Date', 'active']
    search_fields = ['id', 'name']
    list_filter = ['created_Date', 'name']
    readonly_fields = ['my_image']

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img src='/static/{course.image.name}' width='200'/>")


admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
