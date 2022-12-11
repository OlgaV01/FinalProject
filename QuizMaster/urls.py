from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/',views.login, name="login"),
    path('create/', views.create_study_set, name="studySet"),
    path('update/<int:name_id>', views.update, name="update_set"),
    path('delete/<int:name_id>', views.delete, name="delete_set"),
    path('index/', views.index, name="index"),
    path('add/<int:name_id>', views.add, name="add_term"),

]
