from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Sauce)
admin.site.register(models.Topping)
admin.site.register(models.Cake)



#admin.site.register(models.Author)
# class BooksInstanceInline(admin.TabularInline):
#     model = models.BookInstance
# @admin.register(models.Book) # this the same as: admin.site.register(models.Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]
# @admin.register(models.Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# @admin.register(models.BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back')
#         }),
#     )
    