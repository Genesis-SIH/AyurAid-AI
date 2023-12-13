from django.shortcuts import render
from .models import data_collection
from django.http import JsonResponse, HttpResponse
from bson.objectid import ObjectId
from django.http import JsonResponse
from bson.objectid import ObjectId


def index(request):
    return HttpResponse("App is running!!!")


#add

def add_data(request):
    try:
        data = {"data": "hello"} #data = {"data": request.POST.get("data", "")}
        result = data_collection.insert_one(data)
        if result.inserted_id:
            return JsonResponse({"message": "New data added successfully", "id": str(result.inserted_id)})
        else:
            return JsonResponse({"error": "Failed to add data"}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)




#show

def get_all_data(request):
    if request.method == 'GET':
        datas = list(data_collection.find())
        for data in datas:
            data["_id"] = str(data["_id"])
        return JsonResponse({"data": datas})
    else:
        return HttpResponse("Method Not Allowed", status=405)



#find

def get_data_by_id(request, data_id):
    try:
        _id = ObjectId(data_id)
        data = data_collection.find_one({"_id": _id})

        if data:
            data["_id"] = str(data["_id"])
            return JsonResponse({"data": data})
        else:
            return JsonResponse({"error": "Data not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    

#update

def update_person_by_id(request, data_id):
    try:
        _id = ObjectId(data_id)
        overide = {"byee": "hello"}

        all_updates = {
            "$set": {
                "new_field": True,
                "data": overide,
            },
        }

        print(f"ID: {_id}")
        print(f"Updates: {all_updates}")
        data_collection.update_one({"_id": _id}, all_updates)

        return JsonResponse({"message": "Data updated successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

#delete

def delete_by_id(request, data_id):
    try:
        _id = ObjectId(data_id)

        result = data_collection.delete_one({"_id": _id})

        if result.deleted_count > 0:
            return JsonResponse({"message": "Data deleted successfully"})
        else:
            return JsonResponse({"error": "Data not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


