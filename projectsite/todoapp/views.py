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



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().select_related('category', 'priority').order_by('-created_at')

        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)

        priority_id = self.request.GET.get('priority')
        if priority_id:
            qs = qs.filter(priority__id=priority_id)

        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(category__id=category_id)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['priorities'] = Priority.objects.all()
        context['categories'] = Category.objects.all()
        context['status_choices'] = Task.STATUS_CHOICES
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')



class SubTaskListView(LoginRequiredMixin, ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().select_related('parent_task')

        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(parent_task__title__icontains=query)
            )

        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)

        return qs

    def get_ordering(self):
        return 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = SubTask.STATUS_CHOICES
        return context


class SubTaskCreateView(LoginRequiredMixin, CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')


class SubTaskUpdateView(LoginRequiredMixin, UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')


class SubTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')