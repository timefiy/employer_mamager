from django.db import models


# Create your models here.


class Department(models.Model):
    """部门表"""
    # id = models.BigAutoField(verbose_name='部门id', primary_key=True)
    dep_name = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.dep_name


class Employer(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="员工姓名", max_length=16)
    password = models.CharField(verbose_name='员工密码', max_length=64)
    age = models.IntegerField(verbose_name='员工年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    '''前者指定的整数的范围，后者限制了小数的范围'''
    create_time = models.DateTimeField(verbose_name='入职时间')
    # ForeignKey 是一种字段类型，用于创建两个模型之间的一对多
    """
    to：一个字符串，指定要关联的模型的名称。
    to_field：可选参数，指定要链接到的字段名称。默认为 "id"，即主模型的主键。如果你想要链接到其他字段，可以使用这个参数。
    on_delete：指定当关联对象被删除时应该如何处理。models.CASCADE 表示级联删除，即当主模型的对象被删除时，所有关联的从模型对象也会被删除。
    """
    dep = models.ForeignKey(to="Department", to_field='id', on_delete=models.CASCADE)
    # 添加约束，赋值时要用元组
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='员工性别', choices=gender_choices)
