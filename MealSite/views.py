from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView, UpdateView
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Tag, Meal, MealRating
from .forms import MealForm


class IndexView(ListView):
    model = Meal
    template_name = "MealSite/index.html"
    context_object_name = "meal_list"

    def get_queryset(self):
        meal_list = self.model.objects.all()
        q = self.request.GET.get('q') if self.request.GET.get('q') is not None else ''
        if q == 'rating':
            meal_list = meal_list.annotate(avg_rating=Avg("mealrating__rating")).order_by('-avg_rating')
        elif q == 'date':
            meal_list = meal_list.order_by('-dateAdded')
        else:
            meal_list = meal_list.order_by("countryOfOrigin")
        return meal_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_list"] = Tag.objects.all()
        return context


class TagView(ListView):
    model = Meal
    template_name = 'MealSite/index.html'
    context_object_name = 'meal_list'

    def get_queryset(self):
        tag = Tag.objects.get(name=self.kwargs['tag'])
        meal_list = self.model.objects.filter(tag=tag)
        return meal_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.filter(name=self.kwargs['tag'])
        return context


class MealDetailView(LoginRequiredMixin ,DetailView, CreateView):
    model = MealRating
    fields = ['meal', 'rating']
    template_name = 'MealSite/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal'] = Meal.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meal:detail', kwargs={'pk': self.object.meal.id})


class MealCreateView(LoginRequiredMixin, FormView):
    template_name = 'MealSite/create.html'
    model = Meal
    form_class = MealForm
    success_url = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        self.success_url = reverse_lazy('meal:index')
        return super().form_valid(form)


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'MealSite/delete.html'
    success_url = reverse_lazy('meal:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'MealSite/update.html'
    fields = ['name', 'imageUrl', 'countryOfOrigin', 'tag', 'description']

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_success_url(self):
        return reverse('meal:detail', kwargs={'pk': self.object.id})