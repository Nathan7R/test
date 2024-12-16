from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "eat no meat for a month",
    "febuary": "walk 20 minutes a day",
    "march": "read 20 minutes a day",
    "april": "sleep less",
    "may": "eat healthy",
    "june": "eat more meat",
    "july": "message 1 person a day",
    "august": "watch less tv",
    "september": "play less games",
    "october": "code 20 min a day",
    "november": "make a friend a day",
    "december": "call 1 person a day"
}


def home(request):
    return HttpResponse("home")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("this month number is not valid!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, 
            "month_name": month.capitalize()})
    except:
        return HttpResponseNotFound("<h1>this month is not valid!</h1>")

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


    # list_months = ""
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

