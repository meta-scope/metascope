# views.py
from django.shortcuts import render
from . import api_utils

def home(request):
    return render(request, 'home.html')

def results(request):
    contract_address = request.GET['contract_address']
    token_id = request.GET['token_id']
    blockchain = request.GET['blockchain']
    data = api_utils.process_metadata(contract_address, token_id, blockchain)
    return render(request, 'results.html', {'data': data})
