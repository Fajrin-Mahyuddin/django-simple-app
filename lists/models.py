from django.db import models

# Create your models here.
class Todo(models.Model):
	todo_name = models.CharField(max_length=50)
	priority_level = models.DecimalField(max_digits=10, decimal_places=0)
	is_finish = models.BooleanField(default=False)
	due_date = models.DateTimeField("date published")

	def __str__(self) -> str:
		return self.todo_name
