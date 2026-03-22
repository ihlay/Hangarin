from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from todoapp.models import Priority, Category, Task, Note, SubTask


class Command(BaseCommand):
    help = 'Populate initial data for Hangarin To-Do App'

    def handle(self, *args, **kwargs):
        self.create_priorities()
        self.create_categories()
        self.create_tasks(30)
        self.create_notes(20)
        self.create_subtasks(25)

    def create_priorities(self):
        names = ['High', 'Medium', 'Low', 'Critical', 'Optional']
        for name in names:
            Priority.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Priorities created: High, Medium, Low, Critical, Optional'))

    def create_categories(self):
        names = ['Work', 'School', 'Personal', 'Finance', 'Projects']
        for name in names:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Categories created: Work, School, Personal, Finance, Projects'))

    def create_tasks(self, count):
        fake = Faker()
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                category=fake.random_element(elements=categories) if categories else None,
                priority=fake.random_element(elements=priorities) if priorities else None,
            )
            self.stdout.write(self.style.SUCCESS('Task created successfully.'))

    def create_notes(self, count):
        fake = Faker()
        tasks = list(Task.objects.all())
        if not tasks:
            self.stdout.write(self.style.WARNING('No tasks found. Skipping notes.'))
            return

        for _ in range(count):
            Note.objects.create(
                task=fake.random_element(elements=tasks),
                content=fake.paragraph(nb_sentences=3),
            )
            self.stdout.write(self.style.SUCCESS('Note created successfully.'))

    def create_subtasks(self, count):
        fake = Faker()
        tasks = list(Task.objects.all())
        if not tasks:
            self.stdout.write(self.style.WARNING('No tasks found. Skipping subtasks.'))
            return

        for _ in range(count):
            SubTask.objects.create(
                parent_task=fake.random_element(elements=tasks),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
            )
            self.stdout.write(self.style.SUCCESS('SubTask created successfully.'))