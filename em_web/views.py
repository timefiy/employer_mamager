from django import forms
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse

from em_web.models import Employer
from em_web.models import Department


def dep_list(request):
    # 从数据库中获取数据
    all_dep_data = Department.objects.all().order_by('id')
    return render(request, 'dep_list.html', {'dep_queryset': all_dep_data})


def emp_list(request):
    search_data = request.GET.get("search")

    if search_data:
        # 使用 Q 对象构建过滤条件
        emp_data = Employer.objects.filter(Q(name__icontains=search_data))
    else:
        emp_data = Employer.objects.all()

    page_str = request.GET.get("page")
    if page_str:
        page = int(page_str)
    else:
        page = 1
    page_max_item = 2
    start = (page - 1) * page_max_item
    end = page * page_max_item
    emp_data = emp_data[start:end]

    for emp in emp_data:
        emp.create_time = emp.create_time.strftime("%Y-%m-%d")
        emp.gender = emp.get_gender_display()

    return render(request, "emp_list.html", {"emp_queryset": emp_data, "search_data": search_data, "page": page})


def dep_add(request):
    if request.method == "GET":
        return render(request, 'dep_add.html')
    elif request.method == 'POST':
        get_post = request.POST
        dep_name = get_post.get("dep_name")

        from em_web.models import Department
        Department.objects.create(dep_name=dep_name)
        if Department.objects.filter(dep_name=dep_name):
            return redirect('http://127.0.0.1:8000/dep_list/')
        else:
            return HttpResponse("提交失败")


class EmpAddForm(forms.ModelForm):
    name = forms.CharField(min_length=3, label="员工姓名")

    class Meta:
        model = Employer
        fields = ["name", "password", "age", "account", "create_time", "gender", "dep"]
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "age": forms.NumberInput(attrs={"class": "form-control"}),
        #     "account": forms.NumberInput(attrs={"class": "form-control"}),
        #     "create_time": forms.TimeInput(attrs={"class": "form-control"})
        # }

        def __int__(self, *args, **kwargs):
            super().__int__(*args, **kwargs)
            for name, field in self.fields.items():
                # "class": "form-control" "placeholder": field.labels
                field.widgets.attrs = {}


def emp_add(request):
    """员工新建"""
    if request.method == 'POST':
        emp_add_form = EmpAddForm(data=request.POST)
        if emp_add_form.is_valid():
            # 如果数据合法
            emp_add_form.save()
            return redirect("/emp_list/")
        else:
            return render(request, "emp_add.html", {"form": emp_add_form})
    emp_add_form = EmpAddForm()
    return render(request, "emp_add.html", {"form": emp_add_form})


def dep_del(request):
    if request.method == 'GET':
        del_id = request.GET.get('del_id')

    Department.objects.filter(id=int(del_id)).delete()

    return redirect('http://127.0.0.1:8000/dep_list/')


def emp_del(request):
    if request.method == 'GET':
        emp_del_id = request.GET.get("emp_del_id")

    Employer.objects.filter(id=int(emp_del_id)).delete()
    return redirect("http://127.0.0.1:8000/emp_list/")


def dep_update(request):
    if request.method == 'GET':
        update_dep_id = request.GET.get("update_id")
        default_dep_name = Department.objects.filter(id=int(update_dep_id)).first()
        return render(request, 'dep_update.html', {"default_dep": default_dep_name})
    elif request.method == "POST":
        new_dep_id = request.POST.get("new_dep_id")
        new_dep_name = request.POST.get('new_dep_name')
        Department.objects.filter(id=int(new_dep_id)).update(dep_name=new_dep_name)
        return redirect('/dep_list/')
