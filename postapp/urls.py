from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView, PostDetailView



urlpatterns = [
    url(r'^$', PostListView.as_view(), name='index'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    url(r'^post-detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post-comments/(\d+)/$', views.post_comments, name='post-comment')
]