from django_filters import FilterSet
from .models import Post
from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput


class NewsFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='some_data',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
# В Meta классе мы должны указать Django модель,
# в которой будем фильтровать записи.
        model = Post

# В fields мы описываем по каким полям модели
# будет производиться фильтрация.
        fields = {
            'categories': ['exact'],
            'title': ['icontains'],




        }


