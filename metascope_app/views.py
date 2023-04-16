from django.shortcuts import render
from . import api_utils

def index(request):
    return render(request, 'index.html')

def results(request):
    if request.method == 'POST':
        contract_address = request.POST.get('contract_address')
        token_id = request.POST.get('token_id')
        blockchain = request.POST.get('blockchain')
        data = api_utils.process_metadata(contract_address, token_id, blockchain)
    return render(request, 'results.html', {'data': data})