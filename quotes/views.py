from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        
        url = 'https://apicalls.io/api/v1/markets/stock/quotes'
        params = {'ticker': ticker,}
        headers = {'Authorization': 'Bearer 573|6YpfvAfKkzwBGewnAgZG14WjpS819TeHTsAvTMgA'}
        
        api_request = requests.request('GET', url, headers=headers, params=params)

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "ERROR!!!"

        return render(request, 'home.html', {'api': api })
    
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..." })
    


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect('add_stock')
        
    else:
        ticker = Stock.objects.all()
        output = []

        for ticker_item in ticker:

            url = 'https://apicalls.io/api/v1/markets/stock/quotes'
            params = {'ticker': str(ticker_item),}
            headers = {'Authorization': 'Bearer 573|6YpfvAfKkzwBGewnAgZG14WjpS819TeHTsAvTMgA'}
            
            api_request = requests.request('GET', url, headers=headers, params=params)

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "ERROR!!!"

        return render(request, 'add_stock.html', {'ticker':ticker, 'output':output})



def delete_stock(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted"))
    return redirect('add_stock')

  
       

  

# Create your views here.
  #lx_5UdqEAi5lzIdpukTWj19EaEWuWjnr
    #573|6YpfvAfKkzwBGewnAgZG14WjpS819TeHTsAvTMgA