from django.shortcuts import render
from django.http import JsonResponse
from .models import country
from django.db.models import Count
from django.core import serializers
# Create your views here.
# PERFORMING CRUD operations using ORM
def create(request,state,city,postal_code):
    try:
        new_country = country.objects.create(
        state=state,
        city=city,
        postal_code=postal_code
    )
        return JsonResponse({"message":"Data create succefully."})
    
    except Exception as e:
        return JsonResponse({"error":e})
        
def read(request,postal_code):
    try:
        record=country.objects.all()
        data = list(record.values())
        for rec in data:
            if rec['postal_code']==postal_code:
                return JsonResponse(rec)
    except Exception as e:
        return JsonResponse({"error":e})
    
def update(request,id,state, city, postal_code):
    try:
        record = country.objects.update_or_create(
            id=id,

            defaults={
                'state': state,
                'city': city,
                'postal_code': postal_code
            },
        )
            
        return JsonResponse({"msg":"created"})
    except Exception as e:
        return JsonResponse({"error":e})
        # if record.exists():
        #     for rec in record:
        #             rec.state=state
        #             rec.city=city
        #             rec.save()
        #     updated_records = list(record.values())
            #return JsonResponse(updated_records, safe=False)
    # except Exception as e:
    #     return JsonResponse({"error":e})
    

def delete(request,postal_code):
    try:
        record=country.objects.filter(postal_code=postal_code).delete()
        return JsonResponse({"msg":"deleted"})
    except Exception as e:
        return JsonResponse({"error":e})


def filtered_countries_view(request):
    filtered_countries = country.objects.exclude(postal_code=500)
    print(filtered_countries.values_list())
    filtered_countries_data = list(filtered_countries.values())
    print(filtered_countries_data)
    return JsonResponse(filtered_countries_data, safe=False)

def entries_no(request):
    # filtered_countries = country.objects.values('state').annotate(count_state=Count('state'))
    filtered_countries = country.objects.aggregate(Count('state'))
    # for s in filtered_countries:
    # for s in filtered_countries:
    #     print(f"State: {s['state']}, State Count: {s['count_state']}")
    return JsonResponse(filtered_countries)

def get_method(request,id):
    try:
        filtered_countries = country.objects.get(id=id)
        info_={
            'id':filtered_countries.id,
            'state':filtered_countries.state,
            'postal_code':filtered_countries.postal_code,
        }
        print(filtered_countries)
        print(info_)
        return JsonResponse(info_)
    except Exception as e:
        return JsonResponse({"error":e})
    
from django.http import JsonResponse
from .models import country

def orderby_(request):

    filtered_countries = country.objects.order_by("-id")
    
    data = []
    for country_obj in filtered_countries:
        country_data = {
            'id': country_obj.id,
            'state': country_obj.state,
            'postal_code': country_obj.postal_code
        }
        data.append(country_data)
    

    return JsonResponse(data, safe=False)
    
