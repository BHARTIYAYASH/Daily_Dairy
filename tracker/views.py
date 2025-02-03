from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.defaulttags import register
from calendar import monthrange
from datetime import date
from django.db.models import Sum
from .models import DailyConsumption
from .forms import DailyConsumptionForm
from django.views.decorators.csrf import csrf_exempt
import calendar

# Price of 1L milk, 1KG curd, 1L buttermilk (Modify as needed)
PRICES = {'Milk': 71, 'Curd': 40, 'Buttermilk': 40}

@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key))

def home(request):
    form = DailyConsumptionForm()

    if request.method == 'POST':
        form = DailyConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    # Get all consumption data for the current month
    month_data = DailyConsumption.objects.filter(
        date__month=date.today().month
    ).order_by('-date')  # Sort by date descending
    
    # Calculate totals and costs
    total_milk = month_data.filter(item="Milk").aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_curd = month_data.filter(item="Curd").aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_buttermilk = month_data.filter(item="Buttermilk").aggregate(Sum('quantity'))['quantity__sum'] or 0

    # Calculate individual costs
    total_milk_cost = total_milk * PRICES['Milk']
    total_curd_cost = total_curd * PRICES['Curd']
    total_buttermilk_cost = total_buttermilk * PRICES['Buttermilk']
    total_cost = total_milk_cost + total_curd_cost + total_buttermilk_cost

    # Get current month's name and days
    today = date.today()
    _, days_in_month = monthrange(today.year, today.month)
    current_month = calendar.month_name[today.month]

    # Create grid data structure
    date_quantity_pairs = []
    dates = list(range(1, days_in_month + 1))
    
    # Split dates into chunks of 6
    for i in range(0, len(dates), 6):
        chunk = dates[i:i+6]
        # Pad with empty strings if needed to maintain grid structure
        while len(chunk) < 6:
            chunk.append('')
        date_quantity_pairs.append({'dates': chunk})

    # Create dictionary of milk quantities by date
    milk_entries = month_data.filter(item="Milk")
    milk_by_date = {str(entry.date.day): entry.quantity for entry in milk_entries}

    context = {
        'form': form,
        'month_data': month_data,
        'total_milk': total_milk,
        'total_curd': total_curd,
        'total_buttermilk': total_buttermilk,
        'total_milk_cost': total_milk_cost,
        'total_curd_cost': total_curd_cost,
        'total_buttermilk_cost': total_buttermilk_cost,
        'total_cost': total_cost,
        'days_in_month': range(1, days_in_month + 1),
        'date_quantity_pairs': date_quantity_pairs,
        'milk_by_date': milk_by_date,
        'current_month': current_month,
    }
    
    return render(request, 'tracker/home.html', context)

def add_entry(request):
    if request.method == 'POST':
        form = DailyConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change 'home' to your actual home page view
    else:
        form = DailyConsumptionForm()

    return render(request, 'add_entry.html', {'form': form})

def edit_entry(request, entry_id):
    entry = get_object_or_404(DailyConsumption, id=entry_id)
    if request.method == 'POST':
        form = DailyConsumptionForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DailyConsumptionForm(instance=entry)

    return render(request, 'tracker/edit_entry.html', {'form': form, 'entry': entry})

@csrf_exempt
def delete_entry(request, entry_id):
    if request.method == 'POST':
        try:
            entry = get_object_or_404(DailyConsumption, id=entry_id)
            entry.delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)