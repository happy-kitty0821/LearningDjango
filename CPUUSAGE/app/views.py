import psutil
from django.http import JsonResponse

def sysinfo(request):
    cpu_percent = psutil.cpu_percent(interval=0.500)
    ram_percent = psutil.virtual_memory().percent
    print(f"cpu usage{cpu_percent}")
    return JsonResponse({'cpu_percent': cpu_percent, 'ram_percent': ram_percent})


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
