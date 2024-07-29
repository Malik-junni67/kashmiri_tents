from django.urls import path
from tents import views
from django.conf import settings
from django.conf.urls.static import static
from .views import tent_detail_view


urlpatterns = [
    path('', views.home, name="home"),
    path('tents', views.tents_view, name="tents"),
    path('add_tent', views.add_tent, name="add_tent"),
    path('tents/<int:pk>/', tent_detail_view, name='tent_detail'),
    path('tents/<int:pk>/edit/', views.tent_edit, name='tent_edit'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    
    # path('profile/update/', profile_update, name='profile_update'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)