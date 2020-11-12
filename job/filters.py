import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    desciption = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields ='__all__'
        exclude=['published_at','image','salary','Vacancy','owner','slug']