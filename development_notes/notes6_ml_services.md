## Creating ML Services
We will using **home-page** url for serving the machine learning model

### Save the ML Model
Here we will use linear regresssion model from the 8th session of the **Skill Upgrade** 

#### Saving the model
	import pickle


	with open('linear_reg_model.pkl','wb') as f:
	    pickle.dump(reg, f)

#### Load the model
	with open('linear_reg_model.pkl', 'rb') as f:
	    model_loaded = pickle.load(f)

	model_loaded.predict(data[['x']])

### Place the ML Model (linear model) in the project directory
Here, we will palce *linear_reg_model.pkl* in the *users/* directory

### Form for input
Add the following code to the *users/froms.py*

	class PredictionForm(forms.Form):
		petal_length = forms.FloatField()

		class Meta:
			fields = ['petal_length']


### View for ML Service in the home page
Add the following code to the *users/views.py*

	import os
	import pickle
	from django.conf import settings


	file_ = os.path.join(settings.BASE_DIR, 'users/linear_reg_model.pkl')
	with open(file_, 'rb') as f:
	    linear_reg_model = pickle.load(f)

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

### Add UI for the ML service
Add the following code to the *users/templates/users/home.html*

	{% extends "users/base.html" %}
	{% load crispy_forms_tags %}

	{% block page_name %}
		<a style="font-size: 13px;" class="navbar-brand mr-4" href=""><span>&laquo;</span>&nbsp&nbsp&nbsp&nbsp {{page_name}}</a>
	{% endblock %}

	{% block content %}
		<h1>HOME PAGE</h1>
		<div class="content-section">
			<form method="POST">
				{% csrf_token %}
				<fieldset class="form-group">
					{{ form|crispy }}
				</fieldset>
				<div class="form-group">
					<button class="btn btn-outline-info" type="submit">Predict</button>
				</div>
			</form>
		</div>


	{% endblock content %}

Now you can run the development server and go to the home page, enter the float number and predict, see what will happening.
