from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from Todos.models import Tasks
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    todo_items = Tasks.objects.all().order_by ("-added_date")
    return render(request, 'main/index.html', {"todo_items": todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    NewItem = Tasks.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")