from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .Filter import NewsFilter
from .forms import NewsForm, ArticleForm
from django.urls import reverse_lazy

class NewFilter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список новостей
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context




class News(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'rating_pt'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    paginate_by = 10 # вот так мы можем указать количество записей на странице



    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — new.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class CreateNews(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'NewsCreate.html'
    def form_valid(self, form):
        new = form.save(commit=False)
        new.change = 'NW'
        return super().form_valid(form)

class EditNews(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'NewsEdit.html'
    def form_valid(self, form):
        data = form.save(commit=False)
        data.some_data = datetime.utcnow()
        return super().form_valid(form)

class DeleteNews(DeleteView):
    model = Post
    template_name = 'NewsDelete.html'
    success_url = reverse_lazy('News')
    context_object_name = 'newdel'

class CreateArticle(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'ArticleCreate.html'
    def form_valid(self, form):
        article = form.save(commit=False)
        article.change = 'AR'
        return super().form_valid(form)

class EditArticle(UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'ArticleEdit.html'
    def form_valid(self, form):
        data = form.save(commit=False)
        data.some_data = datetime.utcnow()
        return super().form_valid(form)

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'ArticleDelete.html'
    success_url = reverse_lazy('News')