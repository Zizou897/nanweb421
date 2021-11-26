from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail

import re
import json
from django.views.decorators.csrf import csrf_exempt
from nannews import models

# Create your views here.
def index(request):
    accueil = True
    site_web = models.Site.objects.filter(status=True).first()
    return render(request, "index.html", locals())


def catagory(request,slug=None):
    site_web = models.Site.objects.filter(status=True).first()
    return render(request, "catagory.html", locals())


@csrf_exempt
def search(request):
    site_web = models.Site.objects.filter(status=True).first()

    if 'q' in request.GET:
        q = request.GET["q"]
        return render(request, "search.html", locals())


def about(request):
    site_web = models.Site.objects.filter(status=True).first()
    teams = models.Team.objects.filter(status = True)
    configuration = models.Config.objects.filter(status=True).first()
    return render(request, "about-us.html", locals())


def contact(request):
    site_web = models.Site.objects.filter(status=True).first()
    return render(request, "contact.html", locals())


def detail(request, idt=None):
    site_web = models.Site.objects.filter(status=True).first()
    return render(request, "single-post.html", locals())




@csrf_exempt
def checkup(request):
    success = True
    text = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')

        if email.isspace() or email == '' or name.isspace() or name == '' or message.isspace() or message == '':
            success = False
            text = 'Veuillez remplir les champs vides'
        elif re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b',email):
            success = False
            text = 'Veuillez saisir un email valide'
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", name):
            success = False
            text = 'Veuillez saisir un nom valide'
        else:
            contact,created = models.Contact.objects.get_or_create(nom=name, message=message, email=email)
            contact.save()
            if created:
                text = 'Votre message a bien été envoyé'

                send_mail(
                    name,
                    message,
                    email,
                    ['amiroudiallo03@gmail.com'], 
                    fail_silently=False,
                )
            else:
                text = 'Votre message est déjà envoyé'

    datas = {
        'success':success,
        'text':text
    }

    return JsonResponse(datas, safe=False)



    
@csrf_exempt
def registerEmail(request):
    msg, success = '', False

    if request.method == 'POST':
        email = json.loads(request.POST.get('email'))
        if email.isspace():
            msg = 'veuillez remplir ce champ avant de le soumettre !!!'
        elif re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
            msg = 'Email invalide'
        else:
            news, created = models.Newsletter.objects.get_or_create(email=email)
            news.save()
            if created:
                msg = 'email enregistrer avec success'
            else:
                msg = 'Vous etes déjà inscrit'
            success = True
    datas = {
        'success': success,
        'msg': msg
    }
    return JsonResponse(datas, safe=False)