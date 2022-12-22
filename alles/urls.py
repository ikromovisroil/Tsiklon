from django.urls import path
from .views import *
urlpatterns = [
    path('statistika', statistika, name='statistika'),
    path('agent_k', agent_k, name='agent_k'),
    path('agent_y', agent_y, name='agent_y'),
    path('dastafka_k', dastafka_k, name='dastafka_k'),
    path('dastafka_y', dastafka_y, name='dastafka_y'),
    path('tarix_b', tarix_b, name='tarix_b'),
    path('qabul_b', qabul_b, name='qabul_b'),
    path('manzil', manzil, name='manzil'),
    path('buyurtma_batafsil', buyurtma_batafsil, name='buyurtma_batafsil'),
    path('m_qoshish', m_qoshish, name='m_qoshish'),
    path('m_batafsil', m_batafsil, name='m_batafsil'),
    path('buyurtmalar', buyurtmalar, name='buyurtmalar'),
    path('xabar', xabar, name='xabar'),
    path('parolni_tiklash', parolni_tiklash, name='parolni_tiklash'),
    path('parol', parol, name='parol'),
    path('profil_tahrirlash', profil_tahrirlash, name='profil_tahrirlash'),
    path('profil/', profil, name='profil'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),

    # path('add/', m_qoshish, name='m_qoshish'),
    # path('add/addrecord/', m_qoshishi, name='m_qoshishi'),

    path('<int:id>', home, name='home'),
    path('', base, name='base'),
]