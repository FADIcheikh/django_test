from django.conf.urls import url,include



from . import views


urlpatterns = [
    url('',
        include([
        url('index', views.index, name='Index'),
        url('login', views.login,name='login_form'),
        url('details/', views.utilisateur_details,name='details_form'),
        url('details/<slug:username>/<slug:password>/', views.utilisateur_details,name='details_form'),
        url('inscription', views.inscription, name='inscription_form'),
        url('404', views.utilisateur_not_found, name='utilisateur_not_found'),
        ])),
]