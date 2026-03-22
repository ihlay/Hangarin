from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.contrib.auth.mixins import LoginRequiredMixin

from todoapp.models import Priority, Category, Task, Note, SubTask
from todoapp.forms import PriorityForm, CategoryForm, TaskForm, NoteForm, SubTaskForm


class HomePageView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['completed_tasks'] = Task.objects.filter(status='Completed').count()
        context['pending_tasks'] = Task.objects.filter(status='Pending').count()
        context['in_progress_tasks'] = Task.objects.filter(status='In Progress').count()
        context['total_subtasks'] = SubTask.objects.count()
        context['total_notes'] = Note.objects.count()

        context['category_stats'] = (
            Category.objects.annotate(task_count=Count('task')).order_by('-task_count')
        )
        context['priority_stats'] = (
            Priority.objects.annotate(task_count=Count('task')).order_by('-task_count')
        )
        context['recent_tasks'] = Task.objects.select_related('category', 'priority').order_by('-created_at')[:5]
        return context
