from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, PredictionForm
import os
import pickle
from django.conf import settings


file_ = os.path.join(settings.BASE_DIR, 'users/linear_reg_model.pkl')
with open(file_, 'rb') as f:
# with open('linear_reg_model.pkl', 'rb') as f:

    linear_reg_model = pickle.load(f)

# linear_reg_model.predict(data[['x']])


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			# Flash message
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})


def home(request):
	if request.method == 'POST':
		form = PredictionForm(request.POST)
		if form.is_valid():
			# form.save()
			petal_length = form.cleaned_data.get('petal_length')
			# prediction = -0.3554602938119322 + petal_length*0.41507865012819617
			prediction = linear_reg_model.predict([[petal_length]])[0]

			# Flash message
			messages.success(request, f'The Petal Widh prediction for the given petal Length {petal_length}  is {prediction}')
			return redirect('home-page')
	else:
		form = PredictionForm()
		prediction = None
		petal_length = None


	return render(request, 'users/home.html', {'form': form, 'petal_length': petal_length, 'prediction': prediction})