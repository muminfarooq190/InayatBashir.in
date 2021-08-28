from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'
urlpatterns = [
    path('', views.ListTopBlogs.as_view(), name='top_blog_list'),
    path('blogs/list/', views.ListAllBlogs.as_view(), name='all_blog_list'),
    path('blogs/list/<int:pk>/', views.DetailBlog.as_view(), name='detail_blog'),
    path('me/',views.AboutMe.as_view(), name='me')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
