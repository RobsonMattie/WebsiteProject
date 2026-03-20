from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def custom400(request, exception):
    return render(request, 'Error Pages/400.html', status=400)

def custom403(request, exception):
    return render(request, 'Error Pages/403.html', status=403)

def custom404(request, exception):
    return render(request, 'Error Pages/404.html', status=404)

def custom500(request):
    return render(request, 'Error Pages/500.html', status=500)

def custom503(request, exception):
    return render(request, 'Error Pages/503.html', status=503)