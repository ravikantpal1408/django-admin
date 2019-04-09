from import_export import resources
from blog_app.models import Comment



class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        