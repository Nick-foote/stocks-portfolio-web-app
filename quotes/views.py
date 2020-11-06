from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
from .models import Stock
from .forms import StockForm



api_key = '#####'		# Insert own Public Key from IEX.com


def home(request):
	if request.method == 'POST':
		ticker = request.POST["ticker"]
		api_request = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={api_key}')
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'ERROR'

		return render(request, 'home.html', {'api': api})
	
	else:
		return render(request, 'home.html', {'ticker': 'Enter a Ticker Symbol above to retrieve stock information'})


def about(request):
	return render(request, 'about.html', {})


def stocks(request):
	if request.method == 'POST':
		form = StockForm(request.POST or None)
		
		if form.is_valid():
			form.save()
			sym = request.POST.get('ticker')

			messages.success(request, (f'{sym} Stock has been added'))
			return redirect('stocks')

	else:
		ticker = Stock.objects.all()
		api_stocks = []

		for sym in ticker:
			api_request = requests.get(f'https://cloud.iexapis.com/stable/stock/{str(sym)}/quote?token={api_key}')

			try:
				api = json.loads(api_request.content)
				api_stocks.append(api)
			except Exception as e:
				api = 'ERROR'

		return render(request, 'stocks.html', {'ticker': ticker, 'api_stocks': api_stocks})


def delete(request, symbol):

	"""Will find all stock tickers whether capitalised or lower case"""

	item = Stock.objects.get(ticker__iexact=symbol)
	item.delete()
	messages.success(request, (f"{item} Stock has been removed"))
	return redirect('stocks')



def dashboard(request):
	return render(request, 'dashboard.html', {})