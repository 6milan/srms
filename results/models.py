from django.db import models
from subjects.models import StudentClass
from students.models import Student
from django.urls import reverse
from django.contrib.postgres.fields import JSONField

from django.db import migrations, models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):
    dependencies = [('testapp', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff', JSONField()),
            ],
        ),
    ]


# Create your models here.

class DeclareResult(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    select_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = JSONField(blank=True)

    def get_absolute_url(self):
        return reverse('results:declare_result')

    def __str__(self):
        return "%s Section-%s" % (self.select_class.class_name, self.select_class.section)
