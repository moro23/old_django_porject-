from django.test import TestCase

from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='a body here')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expect_object_name = f'{todo.title}'
        self.assertEquals(expect_object_name, 'first todo')


    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expect_object_name = f'{todo.body}'
        self.assertEquals(expect_object_name, 'a body here')