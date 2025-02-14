from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Department,Roles
from .forms import DepartmentForm,RegisterForm,Rolesform
from django.shortcuts import render, redirect,get_object_or_404




def register(request):
    if request.method == 'POST':
        reg=RegisterForm(request.POST)
        if reg.is_valid():
            reg.save()
            messages.success(request,'Registration Successfully !!')
            return redirect('login')
        else:
            messages.error(request, 'Please fill Valid Details !')
    else:
        reg=RegisterForm()
    return render(request,'register.html',{'reg':reg})





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, 'Login successful. Welcome to the Dashboard!')
                return redirect('dashboard')  
            else:
                messages.success(request, 'Login successful. Welcome to the Dashboard!')
                return redirect('user_dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')






def home(request):
    return render(request,'home.html')





@login_required
def logout_view(request):
    logout(request)
    return redirect('home')





@login_required
def dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Access restricted to administrators.')
        return redirect('login')
    departments = Department.objects.filter(status=True)
    return render(request, 'admin_dashboard.html', {'departments': departments})




@login_required
def user_dashboard(request): 
    return render(request, 'user_dashboard.html')




@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully!')
            return redirect('add_department')
        else:
            messages.error(request, 'There was an error adding the department.')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})





@login_required
def delete_department(request, id):
    department = get_object_or_404(Department, pk=id)
    if request.method == 'POST':
        department.status = False
        department.save()
        messages.success(request, f'Department "{department.Dept_Name}" deactivated successfully.')
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'department': department})




@login_required
def update_department(request, id):
    department = get_object_or_404(Department, pk=id)
    form = DepartmentForm(request.POST or None, instance=department)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Department "{department.Dept_Name}" updated successfully.')
        return redirect('dashboard')
    return render(request, 'update.html', {'form': form})



def roles(request):
    role = Roles.objects.filter(status=True)

    if request.method == 'POST':
        fm = Rolesform(request.POST)
        if fm.is_valid():
            dn=fm.cleaned_data['role_name']
            dd=fm.cleaned_data['role_description']
            reg = Roles(role_name=dn,role_description=dd)
            reg.save()
            fm = Rolesform()  
    else:
        role = Roles.objects.filter(status=True)
        fm = Rolesform()   
        
    return render(request, 'roles.html',{'form':fm, 'role':role})


def deleterole(request, id):
    deleterole = Roles.objects.get(id=id)
    print('got', deleterole)
    deleterole.status = False
    deleterole.save()
    print() 
    fm = Rolesform()   
    return redirect('roles')
 

def updaterole(request, id):
    # Safely get the department object or return a 404 if not found
    role = get_object_or_404(Roles, id=id)
    
    if request.method == "POST":
        form = Rolesform(request.POST, request.FILES, instance=role)
        if form.is_valid():
            form.save()
            return redirect('roles')
        else:
            # Return the form with errors to the template
            return render(request, "updaterole.html", {"form": form})
    else:
        # Initialize the form with the existing product instance
        form = Rolesform(instance=role)
        return render(request, "updaterole.html", {"form": form})