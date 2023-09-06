from django.urls import path

from therapy.views import index, rules, Coaches, service, prices, actions_page, category_page, post

urlpatterns = [
    path('', index, name='home'),
    path('rules/', rules, name='rules'),
    path('coach_list/', Coaches.as_view(), name='coaches'),
    path('prices/', prices, name='prices'),
    path('actions/', actions_page, name='actions'),
    path('service/<slug:slug>', service, name='service'),
    path('category/<slug:slug>', category_page, name='category_page'),
    path('posts/<slug:slug>', post, name='post_page'),
]
