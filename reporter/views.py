from django.shortcuts import render


def client_sampling(request, client_id):
    return render(request, 'reporter/client_sampling.html', {'client_id': client_id})
