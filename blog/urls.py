from django.urls import path

from . import views

app_name = 'blog'  #Definiu app_name para podermos referenciar as urls

urlpatterns = [ #Lista de padrões URL
    path('', views.PostListView.as_view(), name='list'), # as_view() recebe a solicitação web
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail')
]