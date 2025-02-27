from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
        BookContributor, Review)


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')
    @admin.display(
        ordering='isbn',
        description='ISBN-13',
        empty_value='-/-'
    )
    def isbn13(self, obj):
        return "{}-{}-{}-{}-{}".format(
            obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13]
        )


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content',
                  {'fields': ('content', 'rating')}))
    # list_display = ('book', 'rating')
    # list_filter = ('rating',)
    # search_fields = ('content', 'book__title')

class BookContributorAdmin(admin.ModelAdmin):
    list_display = ('book', 'contributor', 'role')
    list_filter = ('role',)
    search_fields = ('book__title', 'contributor__last_names')

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Review, ReviewAdmin)