from django.shortcuts import render

# from .forms import SignUpForm

from django.http import HttpResponseRedirect

from .forms import NameForm
from .forms import NewResource

from .models import AddResource

# Create your views here.
def home(request):

	resources = AddResource.objects.order_by('timestamp')

	name = "Welcome Anonymus"
	if request.user.is_authenticated():
		name = "Welcome %s" %(request.user)

	# Form
	if request.method == "POST":
		print request.POST


	context = {
		"resources": resources,
	}


	return render(request, "home.html", context)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
  			instance	=	form.save(commit = False)
		 	instance.save()
			return	HttpResponseRedirect('/')
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return	HttpResponseRedirect('/')

def add_resource(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewResource(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
  			instance	=	form.save(commit = False)
		 	instance.save()
			return	HttpResponseRedirect('/')
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewResource()

    return	HttpResponseRedirect('/')	
