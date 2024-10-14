from django.shortcuts import render
from app1.models import Employee
from . import forms

# Create your views here.
def renderIndex(request):
    empleados = Employee.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'app1/empleados.html', data)


def userRegistrationView(request):
    form = forms.UserRegistrationForm()

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form es Válido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Email: ", form.cleaned_data['email'])
            print("Fono: ", form.cleaned_data['fono'])

    data = {'form' : form}
    return render(request, 'app1/userRegistration.html', data)