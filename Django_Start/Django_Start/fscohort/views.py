from django.shortcuts import render

# HttpResponse is used to 
# pass the information  
# back to view 
from django.http import HttpResponse

# Defining a function which 
# will receive request and 
# perform task depending  
# upon function definition 
def index(request):

    # This will return Hello, world. This is fscohort index page.
    # string as HttpResponse 
    return HttpResponse("Hello, world. This is fscohort index page.")

