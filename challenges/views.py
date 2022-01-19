from django.http import response
from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.


# def index(request):
#     return HttpResponse("This is monthly chllenge")


# def january(request):
#     return HttpResponse("Eat no meat for the entire month")


# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes everyday")


monthly_chllenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 minutes everyday",
    "march": "Learn Django for atleast 20 minutes everyday",
    "april": "Eat no meat for the entire month",
    "may": "Walk for atleast 20 minutes everyday",
    "june": "Learn Django for atleast 20 minutes everyday",
    "july": "Eat no meat for the entire month",
    "august": "Walk for atleast 20 minutes everyday",
    "september": "Learn Django for atleast 20 minutes everyday",
    "october": "Learn Django for atleast 20 minutes everyday",
    "november": "Eat no meat for the entire month",
    "december": None,
}

def index(request):
    months = list(monthly_chllenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_chllenge_by_number(request, month):
    months = list(monthly_chllenges.keys())
    redirect_month = None
    if month > 12:
        return HttpResponseNotFound("This number is not supported!")

    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_chllenges[month]
        print(challenge_text)
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
