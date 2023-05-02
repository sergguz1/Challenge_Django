from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Tell always the truth",
    "february": None,
    "march": "Assume the other person knows something you do not",
    "april": "Do not avoid something frightening if it stands in your way -- and do not do unnecessarily dangerous things",
    "may": "Be precise in your speech",
    "june": "Dress like the person you want to be",
    "july": "Compare yourself to who you were yesterday, not to who someone else is today",
    "august": "Work as hard as you possibly can on at least one thing and see what happens",
    "september": "Do not do things that you hate",
    "october": "Provide a warm and secure home",
    "november": "Object to stupid rules",
    "december": "Buy clothes that are slightly better than you can afford"
}

# Create your views here.

# def january(request):
#     return HttpResponse("Tell always the truth")

# def february(request):
#     return HttpResponse("Walk for at least 20 mins every day")

#month has to be of the same word as the word inside the brackets in the urls.py from challenges
# def monthly_challenges(request, month):
#     challenge_text = None
#     match month:
#         case "january": return HttpResponse("Tell always the truth")
#         case "february": return HttpResponse("Walk for at least 20 mins every day")
#         case "march": return HttpResponse("Assume the other person knows something you do not")
#         case "april": return HttpResponse("Do not avoid something frightening if it stands in your way -- and do not do unnecessarily dangerous things")
#         case "may": return HttpResponse("Be precise in your speech")
#         case "june": return HttpResponse("Dress like the person you want to be")
#         case "july": return HttpResponse("Compare yourself to who you were yesterday, not to who someone else is today")
#         case "august": return HttpResponse("Work as hard as you possibly can on at least one thing and see what happens")
#         case "september": return HttpResponse("Do not do things that you hate")
#         case "october": return HttpResponse("Provide a warm and secure home")
#         case "november": return HttpResponse("Object to stupid rules")
#         case "december": return HttpResponse("Buy clothes that are slightly better than you can afford")
#         case default: return HttpResponseNotFound("There is no other month, this is not supported")

# Used for the basic home page path, the one with path empty
# Commented out because the following does not have an html view built
# def index(request):
#     list_items = ""
#     months = list(monthly_challenges.keys())

#     for month in months:
#         capitlized_month = month.capitalize()
#         month_path = reverse("month-string", args= [month])
#         list_items += f"<li><a href=\"{month_path}\">{capitlized_month}</li>"
    
#     response_data = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_data)

# The following is the same from above but including an html index view
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is invalid")

    redirect_month = months[month - 1]
    reditect_path = reverse("month-string", args= [redirect_month])
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(reditect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html",{
            "month_text": challenge_text,
            "month_key": month.capitalize()
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404() # This needs the Debug setting set to False, but if it's false, the server will not work
    