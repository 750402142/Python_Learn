from django.db import models

# Create your models here.

class Student(models.Model):
    sex_choice = (
        (0,'女'),
        (1,'男'),
        (2,'保密'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    age = models.SmallIntegerField(verbose_name='年龄')
    sex = models.SmallIntegerField(choices = sex_choice)

    # 在这里如果创建之后想要添加新的列表,在执行就可以同步过去,需要有默认值
    classmate = models.CharField(db_column="class", max_length=5, db_index=True, verbose_name="班级")
    class Meta:
        db_table = 'db_student'
    def __str__(self):
        return self.name
