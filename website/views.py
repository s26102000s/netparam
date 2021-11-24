from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# from paytm.Checksum import generate_checksum, verify_checksum
from .models import course, team, service, product, Transaction, client, Contact
from .form import newslatter, contact
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template

# Create your views here.



@cache_control()
def home(request):

    clients = client.objects.filter()
    print(clients)

    return render(request, 'home.html', {"clients":clients})

@cache_control()
def et(request):
    return render(request, 'et.html')

@cache_control()
def es(request):
    return render(request, 'es.html')

@cache_control()
def rs(request):
    return render(request, 'rs.html')
    

@cache_control()
def courses(request):

    courses = course.objects.all()

    return render(request, 'courses.html', {'courses':courses})

def courseinfo(request, name):

    Course = course.objects.get(name=name)
    
    return render(request, 'courseinfo.html', {'course':Course})

@cache_control()
def services(request):
    services = service.objects.all().order_by('name')
    return render(request, 'services.html', {'services':services})

def service_detail(request, id):

    Service =  service.objects.get(id=id)

    return render(request, 'servicedetail.html', {'service':Service})

def teams(request):

    Course = course.objects.get(name='Artificial Intelligence')

    return render(request, 'team.html', {'course':Course})

@cache_control()
def about(request):
    contacts=contact()
    
    members = team.objects.all().order_by('name')
    if request.method=="POST":
        contacts = contact(request.POST)
        context={'members':members,'contacts':contacts}
        if contacts.is_valid():
            contacts.save()
            email=request.POST["email"]
            name=request.POST["name"]
            recipent_email=(email,)
            email_from=settings.EMAIL_HOST_USER
            try:
                context['msg']='We Will Let You Soon'
                subject="we will let you soon"
                ctx={
                    'name':name
                }
                message = get_template('mail_Contact.html').render(ctx)
                send_mail(subject, message,email_from, recipent_email)
            except:
                context['msg']='We Will Let You Soon'
            contacts=contact()
            return render(request, 'about.html',context)
        else:
            contacts = contact()
            return render(request, 'about.html', {'members':members,'contacts':contacts})
    contacts=contact()
    return render(request, 'about.html', {'members':members,'contacts':contacts})

def career(request):

    
    return render(request, 'career.html')



# def initiate_payment(request):
#     if request.method == "GET":
#         return render(request, 'pay.html')
#     try:
#         username = request.POST['username']
#         password = request.POST['password']
#         amount = int(request.POST['amount'])
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             raise ValueError
#         auth_login(request=request, user=user)
#     except:
#         return render(request, 'pay.html', context={'error': 'Wrong Account Details or amount'})

#     transaction = Transaction.objects.create(made_by=user, amount=amount)
#     transaction.save()
#     merchant_key = settings.PAYTM_SECRET_KEY

#     params = (
#         ('MID', settings.PAYTM_MERCHANT_ID),
#         ('ORDER_ID', str(transaction.order_id)),
#         ('CUST_ID', str(transaction.made_by.email)),
#         ('TXN_AMOUNT', str(transaction.amount)),
#         ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
#         ('WEBSITE', settings.PAYTM_WEBSITE),
#         # ('EMAIL', request.user.email),
#         # ('MOBILE_N0', '9911223388'),
#         ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
#         ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
#         # ('PAYMENT_MODE_ONLY', 'NO'),
#     )

#     paytm_params = dict(params)
#     checksum = generate_checksum(paytm_params, merchant_key)

#     transaction.checksum = checksum
#     transaction.save()

#     paytm_params['CHECKSUMHASH'] = checksum
#     print('SENT: ', checksum)
#     return render(request, 'redirect.html', context=paytm_params)


# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':
#         received_data = dict(request.POST)
#         paytm_params = {}
#         paytm_checksum = received_data['CHECKSUMHASH'][0]
#         for key, value in received_data.items():
#             if key == 'CHECKSUMHASH':
#                 paytm_checksum = value[0]
#             else:
#                 paytm_params[key] = str(value[0])
#         # Verify checksum
#         is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
#         if is_valid_checksum:
#             received_data['message'] = "Checksum Matched"
#         else:
#             received_data['message'] = "Checksum Mismatched"
#             return render(request, 'callback.html', context=received_data)
#         return render(request, 'callback.html', context=received_data)
