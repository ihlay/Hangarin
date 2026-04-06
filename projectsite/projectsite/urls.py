from django.contrib import admin
from django.urls import path, include
from todoapp.views import (
    HomePageView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', HomePageView.as_view(), name='home'),

    path('task_list', TaskListView.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),

    path('subtask_list', SubTaskListView.as_view(), name='subtask-list'),
    path('subtask_list/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<pk>', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),

    path('note_list', NoteListView.as_view(), name='note-list'),
    path('note_list/add', NoteCreateView.as_view(), name='note-add'),
    path('note_list/<pk>', NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),

    path('category_list', CategoryListView.as_view(), name='category-list'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),

    path('priority_list', PriorityListView.as_view(), name='priority-list'),
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),

    path('accounts/', include('allauth.urls')),
]
