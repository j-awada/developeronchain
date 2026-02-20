from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('exploring_crypto_wallets', views.exploring_crypto_wallets, name='exploring_crypto_wallets'),
	path('cult_mentality_in_web3', views.cult_mentality_in_web3, name='cult_mentality_in_web3'),
	path('blockchain_layers', views.blockchain_layers, name='blockchain_layers'),
	path('learning_rust_primer', views.learning_rust_primer, name='learning_rust_primer'),
	path('rust_lifetimes', views.rust_lifetimes, name='rust_lifetimes'),
	path('programming_languages', views.programming_languages, name='programming_languages'),
	path('solana_and_quic', views.solana_and_quic, name='solana_and_quic'),
	path('rustconf_2024_montreal', views.rustconf_2024_montreal, name='rustconf_2024_montreal'),
	path('eurorust_2025_paris', views.eurorust_2025_paris, name='eurorust_2025_paris'),
	path('map_methods_in_rust', views.map_methods_in_rust, name='map_methods_in_rust'),
]