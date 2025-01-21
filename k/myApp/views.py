from django.shortcuts import render, redirect, get_object_or_404
from .models import UserData
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import requests         
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from myApp.models import UserData
import json

UNIVERSAL_API_KEY = settings.UNIVERSAL_API_KEY
UNIVERSAL_USER_EMAIL = settings.UNIVERSAL_USER_EMAIL


def get_countries(request):
        url = "https://api.first.org/data/v1/countries"
        countriesRequestApi = requests.get(url)
        country_data = json.loads(countriesRequestApi.content)['data']
        countries = [{'name': country["country"]} for country in country_data.values()]
        return countries

       
def registation(request):
    print("Registation view called")
    countries = get_countries(request)  # Fetch countries


    
    if request.method == 'POST':
        name = request.POST.get('name')
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        gender = request.POST.get('gender')
        country = request.POST.get('country')
   
        password = request.POST.get("password")
        password_strength = calculate_password_strength(password)
        confirm_password = request.POST.get("confirm_password")
        image = request.FILES.get("image")
        checkbox = request.POST.get('checkbox')


        # Collect errors in a dictionary
        errors = {}
        success={}

        # Field Validations
        if not name:
            errors['name_error'] = 'Please fill your full name.'
        if not user_name:
            errors['user_name_error'] = 'Please fill User Name.'
        if not email:
            errors['mail_error'] = 'Please fill E-mail.'
        if not gender:
            errors['gender_error'] = 'Please Choose Your Gender.'
        if country == 'Select Country':
            errors['country_error'] = 'Please select a country.'
        if not password:
            errors['password_error'] = 'Please fill Password.'
        if password != confirm_password:
            errors['confirm_password_error'] = 'Passwords do not match.'
        if not image:
            errors['image_error'] = 'Please select an image.'
        if not checkbox:
            errors['checkbox_error'] = 'Please agree to the terms and conditions.'

        # Password Validation
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                errors['password_error'] = e.messages[0]

        # Check if username or email already exists
        if UserData.objects.filter(user_name=user_name).exists():
            errors['user_error'] = 'Username is already taken.'
        if UserData.objects.filter(email=email).exists():
            errors['email_already_taken_error'] = 'Email is already registered.'

        # Return form with errors if any exist
        if errors:
            return render(request, 'website/registation.html', {**errors, 'password_strength': password_strength, 'countries': countries})

        # Save user data if no errors
        user_data = UserData(name=name, user_name=user_name, email=email, gender=gender,country=country,password=make_password(password), password_strength=password_strength,image=image)
        user_data.save()

        

        # Redirect after successful registration to clear form
        messages.success(request, 'Registration successful!')
        return redirect('registation')
   

    return render(request, 'website/registation.html', {'countries': countries})





def calculate_password_strength(password):
    # Basic strength check (you can make it more complex)
    if len(password) < 6:
        return 1
    elif len(password) < 8:
        return 3
    elif len(password) < 10:
        return 4
    else:
        return 6  # Max strength for long passwords



def homePage(request):
    return render(request, 'website/registation.html')


def view(request):
    user_data = UserData.objects.all()
    return render(request, 'website/view.html', {'user_data': user_data})


def delete(request, id):
    UserData.objects.filter(id=id).delete()
    return redirect('view')


# def edit(request, id):
#     user = get_object_or_404(UserData,id=id)

#     if request.method == 'POST':
#         user.user_name = request.POST.get("user_name")
#         user.email = request.POST.get("email")
#         password = request.POST.get("password")

#         # Update password if provided
        

#         if not user.user_name:
#             return render(request, 'website/edit.html', {'name_edit_error': 'Please fill user name.'})
#         if not user.email :
#             return render(request, 'website/edit.html', {'mail_edit_error': 'Please fill email.'})
#         if not password :
#             return render(request, 'website/edit.html', {'password_edit_error': 'Please fill password.'})

#         if UserData.objects.filter(user_name=user.user_name).exclude(id=id).exists():
#             return render(request, 'website/edit.html',{'user': user, 'error': 'Username is already taken.'})
        
#         if UserData.objects.filter(email=user.email).exclude(id=id).exists():
#             return render(request, 'website/edit.html', {'user': user, 'error': 'Email is already registered.'})
        
#         user.user_name = user.user_name
#         user.email = user.email

#         if password:
#             user.password = make_password(password)

#         user.save()
#         return redirect('view')

#     return render(request, 'website/edit.html', {'user': user})

def edit(request, id):
    user = get_object_or_404(UserData, id=id)
    errors = {}

    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        image = request.FILES.get("image")

        # Validate input fields
        if not user_name:
            errors['name_edit_error'] = 'Please fill User Name.'
        if not email:
            errors['mail_edit_error'] = 'Please fill E-mail.'
        
        if password != confirm_password:
            errors['confirm_password_edit_error'] = 'Passwords do not match.'
        

        # Check for uniqueness of username and email
        if UserData.objects.filter(user_name=user_name).exists() and user_name != user.user_name:
            errors['user_edit_error'] = 'Username is already taken.'
        if UserData.objects.filter(email=email).exists() and email != user.email:
            errors['mail_edit_error'] = 'Email is already registered.'

        # Validate password if provided
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                errors['password_edit_error'] = e.messages[0]

        # If no errors, update user data
        if not errors:
            user.user_name = user_name
            user.email = email
            if image:
                user.image = image
            if password:
                user.password = make_password(password)
            user.save()
            return redirect('view')  # or whatever URL you need

        # Render form with errors
        return render(request, 'website/edit.html', {'user': user, 'errors': errors})

    # Render the form with the current user data
    return render(request, 'website/edit.html', {'user': user})

def finaldata(request):
    return render(request, 'website/finaldata.html')

def login(request):
    user_data = UserData.objects.all()
    if request.method == 'POST':
        user_name_email = request.POST.get("user_name")
        password = request.POST.get("password")

        if not user_name_email or not password:
            return render(request, 'website/loginform.html', {
                'error': 'Please fill all fields.', 
            })

        try:
            user = UserData.objects.filter(user_name=user_name_email).first() or\
                UserData.objects.filter(email=user_name_email).first()
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('view')
            else:
                raise UserData.DoesNotExist
        except UserData.DoesNotExist:
            return render(request, 'website/loginform.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'website/loginform.html', {'user_data': user_data})
