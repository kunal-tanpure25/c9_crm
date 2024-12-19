from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from dashboard.models import SalesData
# Create your views here.

@login_required
def dashboard(request):
    user = request.user

    sales_records = SalesData.objects.filter(user=user)

    sales_labels = [record.month for record in sales_records]
    sales_data = [float(record.amount) for record in sales_records]

    total_sales = sum(sales_data)
    leads_generated = 25
    active_projects = 5  


    recent_activities = [
        {"date": "2024-11-01", "description": "Closed a big deal"},
        {"date": "2024-11-15", "description": "Followed up with a lead"},
    ]

    return render(request, "dashboard/dashboard.html", {
        "client_name": user.username,
        "sales_labels": sales_labels,
        "sales_data": sales_data,
        "total_sales": total_sales,
        "leads_generated": leads_generated,
        "active_projects": active_projects,
        "recent_activities": recent_activities,
    })

from django.http import JsonResponse
from .models import SalesData

@login_required
def get_sales_data(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    # Fetch sales data only for the logged-in user
    sales = SalesData.objects.filter(user=request.user).order_by('id')
    sales_labels = [sale.month for sale in sales]
    sales_data = [sale.amount for sale in sales]

    return JsonResponse({
        "sales_labels": sales_labels,
        "sales_data": sales_data
    })


