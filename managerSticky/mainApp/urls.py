"""Main app Urls"""


from django.urls import path
from . import views


app_name = 'mainApp'
urlpatterns = [
    path('', views.index, name='index'),

    path('note/<uuid:sticky_id>/', views.all_view_sticky, name='all'),

    path('my_sticky/<slug:user_name>/', views.my_sticky, name='my_sticky'),

    path('my_sticky/<slug:user_name>/<uuid:sticky_id>/',
         views.view_sticky, name='sticky'),

    path('my_sticky/<slug:user_name>/create',
         views.create_sticky, name='create_sticky'),

    path('my_sticky/edit/<slug:user_name>/<uuid:sticky_id>/',
         views.edit_sticky, name='edit_sticky'),

    path('my_sticky/delete/<slug:user_name>/<uuid:sticky_id>/',
         views.delete_sticky, name='delete_sticky'),

    path('my_sticky/favorite/<slug:user_name>/<uuid:sticky_id>/',
         views.favorite_sticky, name='favorite_sticky'),

    path('my_sticky/public/<slug:user_name>/<uuid:sticky_id>/',
         views.public_sticky, name='public_sticky'),

    path('sign_in/', views.RegistrationView.as_view(), name='sign_in'),

    path('page404', views.page404, name='404'),

    path('filter/<int:pk>', views.filter, name='filter')
]
