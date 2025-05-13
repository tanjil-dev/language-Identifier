from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages


import json
import joblib
import os
import logging

logger = logging.getLogger(__name__)


# Define the path to the 'data' folder
data_folder = os.path.join(settings.BASE_DIR, 'data')

# Load the model and vectorizer
model_path = os.path.join(data_folder, 'language_identifier.pkl')
vectorizer_path = os.path.join(data_folder, 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Or wherever you want to redirect after login
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def custom_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('custom_login')  # Redirect to login after successful signup
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'index.html')


def predict_language(request):
    # Set prediction limit based on authentication status
    if request.user.is_authenticated:
        prediction_limit = None  # Unlimited predictions for logged-in users
    else:
        prediction_limit = 10  # Limit to 10 predictions for non-logged-in users

    # Get the current prediction count from session
    current_count = request.session.get('prediction_count', 0)

    # Check if the user has exceeded the prediction limit
    if prediction_limit is not None and current_count >= prediction_limit:
        return JsonResponse({'error': 'Prediction limit reached. Please log in for unlimited predictions.'}, status=400)

    # Increment prediction count in session
    request.session['prediction_count'] = current_count + 1

    # Proceed with prediction logic if there is text in the request
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            # Vectorize the input text
            sample_vec = vectorizer.transform([text])
            # Predict the language
            prediction = model.predict(sample_vec)[0]
            confidence = round(model.predict_proba(sample_vec).max(), 2)
            return JsonResponse(
                {'language': prediction, 'confidence': confidence})

        return JsonResponse({'error': 'No text provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)
            full_name = data.get('fullName')
            email = data.get('email')
            message = data.get('comment')

            # Ensure that all required fields are present
            if not full_name or not email or not message:
                return JsonResponse({'success': False, 'error': 'Missing required fields'}, status=400)

            # Create a new Contact record in the database
            contact = Contact(full_name=full_name, email=email, message=message)
            contact.save()

            return JsonResponse({'success': True})

        except Exception as e:
            # Log the error for debugging purposes
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')