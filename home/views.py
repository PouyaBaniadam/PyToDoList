from django.shortcuts import render, redirect, get_object_or_404

from home.forms import TaskForm
from home.models import Task


def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all().order_by("date").filter(user=request.user)
        form = TaskForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                task = form.cleaned_data['task']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                user = request.user

                Task.objects.create(user=user, task=task, date=date, time=time)
                return redirect("home:home")

        return render(request, template_name="home/index.html", context={"tasks": tasks, "form": form})

    else:
        return render(request, template_name="home/index.html")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    next_parameter = request.GET['next']

    task.delete()

    if next_parameter:
        return redirect(next_parameter)

    return redirect("home:home")


def completed_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    next_parameter = request.GET['next']

    task.status = "completed"
    task.save()

    if next_parameter:
        return redirect(next_parameter)

    return redirect("home:home")


def undo_completed_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    next_parameter = request.GET['next']

    task.status = "pending"
    task.save()

    if next_parameter:
        return redirect(next_parameter)

    return redirect("home:home")


def filter_tasks(request, status):
    form = TaskForm(request.POST or None)
    filtered_tasks = Task.objects.filter(status=status, user=request.user).order_by("date")

    if request.method == "POST":

        next_parameter = request.path

        if form.is_valid():
            task = form.cleaned_data['task']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            user = request.user

            Task.objects.create(user=user, task=task, date=date, time=time)

            if next_parameter:
                return redirect(next_parameter)

            return redirect("home:home")

    if status == 'all':
        return redirect('home:home')

    if status == "all":
        what_is_active = "all"

    if status == "pending":
        what_is_active = "pending"

    if status == "completed":
        what_is_active = "completed"

    return render(request, template_name="home/index.html",
                  context={"tasks": filtered_tasks, 'form': form, "what_is_active": what_is_active})
