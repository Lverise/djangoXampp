from django.shortcuts import render
from app1.models import Employee
# Create your views here.
def renderIndex(request):
    empleados = Employee.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'app1/empleados.html', data)

