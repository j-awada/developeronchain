from django.shortcuts import render
from .models import SubscriberEmail
from django.core.validators import validate_email


def home(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'general/home.html')


def learning_rust_primer(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/learning_rust_primer.html')


def rust_lifetimes(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/rust_lifetimes.html')


def programming_languages(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/programming_languages.html')


def solana_and_quic(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/solana_and_quic.html')


def rustconf_2024_montreal(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/rustconf_2024_montreal.html')


def eurorust_2025_paris(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/eurorust_2025_paris.html')


def map_methods_in_rust(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/map_methods_in_rust.html')


## Unpublished

def exploring_crypto_wallets(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/exploring_crypto_wallets.html')


def cult_mentality_in_web3(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/cult_mentality_in_web3.html')

def blockchain_layers(request):
	if request.method == 'POST':
		try:
			subscriber_email = request.POST['subscriber_email']
			validate_email(subscriber_email)
			if SubscriberEmail.objects.filter(subscriber_email=subscriber_email).exists():
				return render(request, 'general/subscribed.html', {'subscribed_message': 'You are already subscribed! :)'})
			subscribe_int = SubscriberEmail.objects.create(subscriber_email=subscriber_email)
			subscribe_int.save()
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Thanks for subscribing! :)'})
		except:
			return render(request, 'general/subscribed.html', {'subscribed_message': 'Hmm, something went wrong.'})
	return render(request, 'blog/blockchain_layers.html')