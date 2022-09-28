from django.urls import path
# Импортируем созданное нами представление
from .views import News, NewsDetail, NewFilter, CreateNews, EditNews, DeleteNews, CreateArticle, EditArticle, DeleteArticle


urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', News.as_view(), name='News'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>/', NewsDetail.as_view()),
    path('search/', NewFilter.as_view(), name='search'),
    path('create/', CreateNews.as_view(), name='Create_New'),
    path('<int:pk>/edit/', EditNews.as_view(), name='Edit_New'),
    path('<int:pk>/delete/', DeleteNews.as_view(), name='Delete_New'),
    path('articles/create/', CreateArticle.as_view(), name='Create_Article'),
    path('articles/<int:pk>/edit/', EditArticle.as_view(), name='Edit_Article'),
    path('articles/<int:pk>/delete/', DeleteArticle.as_view(), name='Delete_Article'),
]