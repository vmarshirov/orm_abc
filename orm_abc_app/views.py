import datetime
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import CreateAbcForm
from .models import Abc

def index(request):
    return render(request, 'index.html')

def datetime_nov(request):
    datetime_now = datetime.datetime.now()
    print(datetime_now)
    context = {'key': datetime_now}
    return render(request, 'datetime_now.html', context)


def var_list_dict(request):
    var_main = 2
    print(var_main)
    list_main = [1, 2, 3, 4, 5]
    print(list_main)
    dict_main = {'x': 1, 'y': 2}
    print(dict_main)
    context = {"var_main": var_main, 'list_main': list_main, 'dict_main': dict_main}
    return render(request, 'list_dict.html', context)

class AbcFormCreate(forms.Form):
    a = forms.IntegerField(initial=1, min_value=2)
    b = forms.IntegerField(required=False)
    c = forms.IntegerField(label='c_lable')


def abc_form(request):
    abc_form = AbcFormCreate()
    print(abc_form)
    return render(request, 'abc_form.html', {"abc_form": abc_form})


def abc_get(request):
    print(request.GET)
    print(request.GET.get("a"))
    print(request.GET.get("b"))
    print(request.GET.get("c"))
    A = request.GET.get("a")
    B = request.GET.get("b")
    C = request.GET.get("c")
    return HttpResponse(f"""
    <pre>
    A = {A}
    B = {B}
    C = {C}
    </pre>
    """)



def form_create_0(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect('orm_abc_app:abc_result')
    else:
        form = CreateAbcForm()
        print('\nform_else:\n', form)
    context = {'form': form}
    print("\ncontext:\n", context)
    return render(request, 'form_create_0.html', context)


def form_create(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect('orm_abc_app:abc_result')
    else:
        form = CreateAbcForm()
        print('\nform_else:\n', form)
    context = {'form': form}
    print("\ncontext:\n", context)
    return render(request, 'form_create.html', context)

def solution(a, b, c):
    if a + b == c:
        result = " С равна сумме A и B"
    else:
        result = "С не равна сумме A и B"
    return result
def abc_result(request):
    object_list = Abc.objects.all().order_by('-id')[:2]
    print("object_list: ", object_list)
    last_object = Abc.objects.all().order_by('-id')[:1][0]
    print("object_values: ", last_object.a)
    result_obj = solution(last_object.a, last_object.b, last_object.c)

    print("object_list.values('a', 'b', 'c'):", object_list.values('a', 'b', 'c'))
    last_object = object_list.values('a', 'b', 'c')[0]
    print("last_object: ", last_object)
    print("object_0_a: ", last_object['a'])
    # list
    values_list = object_list.values_list()[0]
    print("values_list: ", values_list)
    if values_list[2] + values_list[3] == values_list[4]:
        result = " С равна сумме A и B"
    else:
        result = "С не равна сумме A и B"
    task_formulation = values_list[1]
    print('task_content: ', task_formulation)
    last_values = [values_list[2], values_list[3], values_list[4]]
    print('last_values:', last_values)
    print('result: ', result)
    context = {'task_formulation': task_formulation, 'last_object': last_object, 'result_obj':result_obj, 'last_values': last_values, 'result': result}
    return render(request, 'abc_result.html', context)


def table(request):
    # objects_list
    objects_values = Abc.objects.values()
    print('\nobjects_values:', objects_values)
    # values_list 
    objects_values_list = Abc.objects.values_list().filter(id__gte=27).order_by('-a')#[0:3]
    print('\nobjects_values_list:', objects_values_list)
    cur_objects = objects_values_list
    statics_val = [cur_objects.aggregate(Count('b')), cur_objects.aggregate(Avg('b')), cur_objects.aggregate(Min('b')),
                   cur_objects.aggregate(Max('b')), cur_objects.aggregate(StdDev('b')), cur_objects.aggregate(Sum('b'))]
    print('\nstatics_val:', statics_val)
    statics = {'statics_val': statics_val}
    # fields_name
    fields = Abc._meta.get_fields()
    print('\nfields', fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print('\nverbose_name_list:', verbose_name_list)
    print('\nname_list', name_list)
    field_names = verbose_name_list
    context = {'objects_values': objects_values, 'name_list': name_list,
               'objects_values_list': objects_values_list,  'verbose_name_list': verbose_name_list,
               'statics': statics, 'field_names': field_names}
    return render(request, 'table.html', context)
