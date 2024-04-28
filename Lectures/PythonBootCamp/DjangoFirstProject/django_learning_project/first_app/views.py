from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

# redirect = yonlendirmek 
# enn düzgün hali
# 1) dict'ten keyler alındı ve liste haline getirildi.
# 2) reverse komutu kullanıldı(isimden fonksiyona gidildi) ve parametre unutulmadı
# 3) HttpResponseRedirect kullanıldı
# 4) try-except ile beraber HttpResponseNotFound("Not Found! Please look for another course.") kullanıldı

def course_number_view(request, num1):
    course_list = list(course_dictionary.keys())
    try:
        course = course_list[num1]
        page_to_go = reverse("kurs", args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not Found! Please look for another course.")
    