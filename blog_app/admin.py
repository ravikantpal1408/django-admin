from django.contrib import admin
from .models import Blog, Comment, Category, Place
from django.utils import timezone

from django.db.models import Count

from django_summernote.admin import SummernoteModelAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from leaflet.admin import LeafletGeoAdmin
from import_export.admin import ImportExportModelAdmin


from main.resources import CommentResource






# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ('comment_text', 'is_active')
    extra = 0
    classes = ('collapse',)


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

    list_display = ('title', 'author', 'list_date', 'is_active', 'days_since_creations', 'no_of_comments')
    # li    st_editable = ('is_active', )
    ordering = ('title', '-list_date')
    search_fields = ('title', 'author',)
    list_filter = ('is_active', ('list_date', DateTimeRangeFilter))
    prepopulated_fields = { 'slug' : ('title',)}
    actions = ('set_blogs_to_published',)
    date_hierarchy = 'list_date'
    inlines = (CommentInline,)
    # fields = (('title', 'slug'), 'author', 'content')
    fieldsets = (
        (None,{
            'fields' : (('title', 'slug'), 'author', 'content'),
        }),
        ('Advanced Options', {
            'fields' : ('is_active', 'categories'),
            'description' : 'Option to configure Blogs',
            'classes' : ('collapse',) 
        })
    )

    list_per_page = 25

    filter_horizontal = ('categories',)


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comments_count=Count('comments'))
        return queryset 

    
    def no_of_comments(self, blog):
        return blog.comments_count
    no_of_comments.admin_order_field = 'comments_count'
    # no_of_comments.short_description = 'Total Comment(s)'



    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('title', '-list_date')
        return ('title',)


    def set_blogs_to_published(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, 'Selected Bog is Un-Published')
    set_blogs_to_published.short_description = 'Un-True Selected Blog'


    def days_since_creations(self, Blog):
        diff = timezone.now() - Blog.list_date
        return diff.days
    days_since_creations.short_description = 'Days Active'




class CommentAdmin(ImportExportModelAdmin):
    list_display = ('comment_text', 'created_date', 'is_active' , 'blog')
    # list_display_links = ('comment_text',)
    # list_editable = ('comment_text', 'is_active',)
    list_per_page = 10
    list_filter = (        
            ('blog', RelatedDropdownFilter),
        )
    resource_class = CommentResource
    list_select_related = ('blog',)# or True
    raw_id_fields = ('blog',)




admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Place, LeafletGeoAdmin)