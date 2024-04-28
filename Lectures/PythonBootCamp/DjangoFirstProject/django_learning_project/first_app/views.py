from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

# dynamic routing
course_dictionary = {
    "python" : "Python Course Page",
    "java" : "Java Course Page",
    "kotlin" : "Kotlin Course Page",
    "swift" : "Swift Course Page"
}

def index(request):
    return HttpResponse("This is first Django project, first index")

def courses(request, item):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not Found! Please look for another course.")
        #raise Http404("Not Found! Please look for another course.")
    # bu kodun çalışması için settings'e gitmeliyiz.
    # DEBUG = False yap
    # ALLOWED_HOSTS = ["127.0.0.1"] yap
    #return HttpResponse(course_dictionary.get(item, "Not Found!"))

def multiply_view(request, num1, num2): # briefly we can take parameter from user and add to url
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")

def course_number_view(request, num1):
    if num1 == 10:
        return HttpResponseRedirect("kotlin")