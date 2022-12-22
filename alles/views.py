from django.shortcuts import render, redirect
from django.views.generic import *
from .forms import *
from .models import *
# Create your views here.`

# class Base(ListView):
#     model = Turi
#     template_name = 'base.html'

def base(request):
    turi = Turi.objects.all()
    return render(request, 'base.html', {'turi':turi})

def home(request, id):
    turii = Turi.objects.get(id=id)
    maxsulot = Maxsulot.objects.filter(turi=turii)
    turi = Turi.objects.all()
    return render(request, 'home.html', {'maxsulot': maxsulot,'turi':turi})

# def contact(request):
#     news = Fakultet.objects.all()
#     bolim = Bolim.objects.all()
#     if request.method=='POST':
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')
#     form=ContactForm()
#     data={
#         'form':form,
#     }
#     return render(request,'contact.html',{'news':news,'bolim':bolim,'form':form})

# def m_qoshish(request):
#     if request.method == 'POST':
#     form=ContactForm(request.POST)
#         if form.is_valid():
#              form.save()
#     #             return redirect('contact')
#     #     form=ContactForm()
#     return render(request, 'login.html')

def m_qoshish(request):
    return render(request, 'm_qoshish.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profil(request):
    return render(request, 'profil.html')

def profil_tahrirlash(request):
    return render(request, 'profil_tahrirlash.html')

def parol(request):
    return render(request, 'parol.html')

def parolni_tiklash(request):
    return render(request, 'parolni_tiklash.html')

def xabar(request):
    return render(request, 'xabar.html')

def buyurtmalar(request):
    return render(request, 'buyurtmalar.html')

def m_batafsil(request):
    return render(request, 'm_batafsil.html')

def m_qoshish(request):
    return render(request, 'm_qoshish.html')

def buyurtma_batafsil(request):
    return render(request, 'buyurtma_batafsil.html')

def manzil(request):
    return render(request, 'manzil.html')

def qabul_b(request):
    return render(request, 'qabul_b.html')

def tarix_b(request):
    return render(request, 'tarix_b.html')

def dastafka_y(request):
    return render(request, 'dastafka_y.html')

def dastafka_k(request):
    return render(request, 'dastafka_k.html')

def agent_y(request):
    return render(request, 'agent_y.html')

def agent_k(request):
    return render(request, 'agent_k.html')

def statistika(request):
    return render(request, 'statistika.html')