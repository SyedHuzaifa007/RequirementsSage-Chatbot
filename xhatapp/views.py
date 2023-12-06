from django.shortcuts import render
from xhatapp.models import SaveQueries
from xhatapp.Config import BravoSis
from xhatapp.form import usserform
# from datetime import datetime 
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.models import AnonymousUser
from .models import SelectedItems

# Create your views here.


###################### -login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest
from django.http import JsonResponse


# initializing 
wow = BravoSis()
# wow.ai(query)

# Client for telegram
# LeosBot = Client(name="XhatGpt",api_id=wow.api_id,api_hash=wow.api_hash)

def index(request):
    return render(request, 'xhatapp/index.html')

def about(request):
    return render(request, 'xhatapp/about.html')

@login_required
def query(request):
    nice = ""
    result = "....."
    
    if request.method == 'POST':
        user_input = request.POST.get('queryinput') + "of E-commerce store only"
        
        # Check if the user input is within the defined scope for E-commerce
        if is_within_scope(user_input):
            result = wow.ai(user_input)
            
            # Save the query to the database
            ss = SaveQueries(question=user_input, returnquery=result, query_time=timezone.now())
            ss.save()
        else:
            return JsonResponse({'error': 'Input is out of scope for E-commerce requirements. Please provide a relevant query.'}, status=400)

    return render(request, 'xhatapp/index.html', {'query': nice, 'resul': result})

def is_within_scope(user_input):
    # Implement your logic to check if the user input is within the defined scope for E-commerce
    # You may validate the input against certain keywords, phrases, or predefined criteria related to E-commerce requirements
    # Replace this placeholder logic with your actual scope validation logic
    # Return True if within scope, else return False
    # Example placeholder logic:
    e_commerce_keywords = ['functional requirements', 'non functional requirements', 'business requirements', 'low level requirements', 'high level requirements', 'software requirements']
    for keyword in e_commerce_keywords:
        if ("e-commerce" or "E-commerce" or "e commerce" or "E commerce" or "E com" or "online store" or "Online Store" or "Online Shopping" or "online shopping") and keyword.lower() in user_input.lower():
            return True
    return False

def create(request):
    acc_created = False

    if request.method == 'POST':
        usr_form = usserform(data=request.POST)

        if usr_form.is_valid():
            user = usr_form.save()
            user.set_password(user.password)
            user.save()

            acc_created = True
        else:
            print(usr_form.errors)
    
    else:
        usr_form = usserform()

    return render(request, 'xhatapp/createacc.html',{"acc_form":usr_form,"created":acc_created})


def login_usr(request):
    if request.method == 'POST':
        usrname = request.POST.get('Username')
        passwrd = request.POST.get('passsw')
        print(usrname,passwrd)

        user = authenticate(username=usrname, password=passwrd)

        if user:
            if user.is_active:
                login(request, user)
                print("checkked")
                return HttpResponseRedirect(reverse('xhat'))
          
            else:
                print("Account not usable...")
                return HttpResponse("Account not usable...")
        else:
            print(f"""
                somone tried to login!!!
                username : {usrname}
                password : {passwrd}
                """)
            return HttpResponse("OOpppzz Invalid Login Details....")
    else:
        return render(request, 'xhatapp/login.html')
    
@login_required
def usr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('indexpage'))

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

def forgot(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            return render(request, 'password_reset_done.html', {})
    else:
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})   
def forgotdone(request):
    return render(request,"login.html")


def chatbot_view(request):
    fetched_data = ["Requirement 1", "Requirement 2", "Requirement 3"]  # Sample fetched data

    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')

        if isinstance(request.user, AnonymousUser):
            # For anonymous users - Handle accordingly (e.g., associate data with sessions)
            for item in selected_items:
                SelectedItems.objects.create(selected_item=item)
        else:
            user = request.user
            for item in selected_items:
                SelectedItems.objects.create(user=user, selected_item=item)

    return render(request, 'xhatapp/chatbot.html', {'fetched_data': fetched_data})

def export_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="selected_items.pdf"'

    selected_items = SelectedItems.objects.filter(user=request.user) if request.user.is_authenticated else SelectedItems.objects.none()

    try:
        pdf = canvas.Canvas(response)
        pdf.drawString(100, 800, 'Selected Items:')
        y = 780

        for item in selected_items:
            pdf.drawString(120, y, item.selected_item)
            y -= 20

        pdf.showPage()
        pdf.save()
        return response
    except Exception as e:
        print(f"An error occurred while generating PDF: {e}")
        return HttpResponse(status=500)  # Return an error response if PDF generation fails


