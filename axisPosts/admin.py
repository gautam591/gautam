from django.contrib import admin
from .models import Post,postComments,postReactions,commentReactions
from .models import apply,booking
# Register your models here.

class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'postTitle','content')
    list_filter = ()
    search_fields = ['postTitle', 'content','country']
    #prepopulated_fields = {'postSlug': ('postAuthor','postTitle')}

class CommentViewAdmin(admin.ModelAdmin):
    list_display = ('id','postId', 'parentId','commentAuthor', 'comment','popularity','updatedOn')
    #list_filter = ("axisStatus","createdOn",'updatedOn','category')
    #search_fields = ['postTitle', 'content','postAuthor']
    #prepopulated_fields = {'postSlug': ('postTitle',)}

class ReactionsViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'postId', 'userName','reaction')
    #list_filter = ("axisStatus","createdOn",'updatedOn','category')
    #search_fields = ['postTitle', 'content','postAuthor']
    #prepopulated_fields = {'postSlug': ('postTitle',)}

class CmtReactionsViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentId', 'userName','reaction')
    #list_filter = ("axisStatus","createdOn",'updatedOn','category')
    #search_fields = ['postTitle', 'content','postAuthor']
    #prepopulated_fields = {'postSlug': ('postTitle',)}

admin.site.register(Post, PostViewAdmin)
admin.site.register(apply)
admin.site.register(booking)
admin.site.register(postComments, CommentViewAdmin)
admin.site.register(postReactions, ReactionsViewAdmin)
admin.site.register(commentReactions, CmtReactionsViewAdmin)
