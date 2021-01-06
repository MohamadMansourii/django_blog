from django.contrib import admin
from .models import Article, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position','title','slug','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
	prepopulated_fields = {"slug" : ('title',)}


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug','jpublish','status', 'category_to_str')
	list_filter = ('publish','status')
	search_fields = ('title', 'desc')
	prepopulated_fields = {"slug" : ('title',)}
	ordering = ['status','publish']	

	def category_to_str(str, obj):
		return "، ".join([category.title for category in obj.category_published()])

	category_to_str.short_description = "دسته بندی"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
