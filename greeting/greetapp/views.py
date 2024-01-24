# Q3/views.py

from django.shortcuts import render

def get_greeting(request):
    if request.method == 'POST':
        time = request.POST.get('time', '')
        greeting = calculate_greeting(time)
        return render(request, 'greetapp/greet_with_time.html', {'greeting': greeting})

    else:
        return render(request, 'greetapp/greet_with_time.html')

def calculate_greeting(time_str):
    time = int(time_str)
    if 0 <= time <= 23:
        if 0<= time < 12:
            return "Good Morning"
        elif 12 <= time < 17:
            return "Good Afternoon"
        elif 17 <= time < 20:
            return "Good Evening"
        else:
            return "Good Night"
       
