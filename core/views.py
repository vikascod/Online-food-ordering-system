from django.shortcuts import render, redirect
from core.models import Food, Category
from core.forms import FoodForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    foods = None
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        foods = Food.objects.filter(category=categoryID)
    else:
        foods = Food.objects.all()
    context = {'foods':foods, 'categories':categories}
    return render(request, 'core/home.html', context)

def order(request):
    if request.method == "POST":
        client = razorpay.Client(auth=("rzp_test_DXAxqdmpgyJ6Na", "ZX0sYPLhHo0pXIUZNtJU0Wpx"))
        payment = client.order.create({ "amount": 50000, "currency": "INR", "payment_capture": "1" })
    orders = Food.objects.all()
    return render(request, 'core/order_confirm.html', {'orders':orders})

@csrf_exempt
def success(request):
    return render(request, 'core/success.html')


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = SignupForm()
    return render(request, 'core/signup.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

