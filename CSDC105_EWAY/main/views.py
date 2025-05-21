from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EBikeRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import EBikeRegistration
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

@staff_member_required
def admin_registrations(request):
    status = request.GET.get('status')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    search = request.GET.get('search')

    registrations = EBikeRegistration.objects.all()

    if status:
        registrations = registrations.filter(status__iexact=status)
    if date_from:
        registrations = registrations.filter(purchase_date__gte=date_from)
    if date_to:
        registrations = registrations.filter(purchase_date__lte=date_to)
    if search:
        registrations = registrations.filter(
            Q(full_name__icontains=search) |
            Q(ebike_model__icontains=search) |
            Q(ebike_brand__icontains=search)
        )

    return render(request, 'admin-registrations.html', {'registrations': registrations})

def admin_logout(request):
    logout(request)
    return redirect('signin')

def create_account(request):
    print("Create account view called with method:", request.method)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Form data:", request.POST)
        if form.is_valid():
            print("Form is valid, saving user.")
            form.save()
            return redirect('signin')
        else:
            print("Form errors:", form.errors)
            return render(request, 'create_account.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_account.html', {'form': form})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.role == role:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('home_page_with_account')
            else:
                return render(request, 'signin.html', {'error': 'User role mismatch.'})
        else:
            return render(request, 'signin.html', {'error': 'Invalid email or password.'})
    return render(request, 'signin.html')

def user_registration(request):
    print(f"Request method: {request.method}")
    print(f"User: {request.user}")

    if request.method == 'POST':
        form = EBikeRegistrationForm(request.POST)
        print("Form data:", request.POST)

        if form.is_valid():
            print("Form is valid")
            ebike = form.save(commit=False)
            ebike.owner = request.user
            ebike.save()
            messages.success(request, 'E-Bike registered successfully!')
            return redirect('user_registration')
        else:
            print("Form errors:", form.errors)
    else:
        form = EBikeRegistrationForm()

    return render(request, 'registration.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.role == role:
                login(request, user)
                if role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('home_page_with_account')
            else:
                return render(request, 'signin.html', {'error': 'Invalid role for this account.'})
        else:
            return render(request, 'signin.html', {'error': 'Invalid email or password.'})
    return render(request, 'signin.html')

# Static pages / generic views
def homepage(request):
    return render(request, 'home_page.html')

def homepage_with_account(request):
    return render(request, 'home_page_with_account.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def signin(request):
    return render(request, 'signin.html')

def user_registration(request):
    return render(request, 'user_registration.html')

def registration(request):
    return render(request, 'registration.html')

def showcase_with_account(request):
    return render(request, 'showcase_with_account.html')

def regulations(request):
    return render(request, 'regulations.html')

def maintenance_main(request):
    return render(request, 'maintenance_main.html')

def maintenance_battery(request):
    return render(request, 'maintenance_battery.html')

def maintenance_services(request):
    return render(request, 'maintenance_services.html')

def maintenance_tire(request):
    return render(request, 'maintenance_tire.html')

# Admin-related views
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_content(request):
    return render(request, 'admin-content.html')

def admin_log_out(request):
    return render(request, 'admin-logout.html')
