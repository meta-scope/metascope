from django.shortcuts import render
from .api_utils import run_metadata

def index(request):
    return render(request, 'index.html')

def results(request):

    contract_address = request.GET.get('contract_address')
    token_id = request.GET.get('token_id')
    blockchain = request.GET.get('blockchain')

    data = run_metadata(contract_address, token_id, blockchain)
    return render(request, 'results.html', {'data': data})