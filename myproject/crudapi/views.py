from django.http import JsonResponse

my_list=[]
my_dict={}
# GET operation


def get_data(request,name):
    print("get_data called")
    for rec in my_list:
        if rec['name']==name:
            return JsonResponse(rec)
    # else:
    #     return JsonResponse({"error":"404 not found"})
#POST operation
def post_data(request,name,roll_no):
    print(name)
    print("post_data called")
    my_dict={
        "name":name,
        "roll_no":roll_no
    }
    my_list.append(my_dict)
    return JsonResponse(my_dict, safe=False)
#PUT operation
def put_data(request,name,new_name):
    print("put_data called")
    for rec in my_list:
        if rec['name']==name:
            rec['name']=new_name
    return JsonResponse(rec)
#DELETE operation
def delete_data(request,roll_no):
    print("delete_data called")
    for rec in my_list:
        print(roll_no,rec)
        if rec['roll_no']==roll_no:
            my_list.remove(rec)
    return JsonResponse({"msg":"User deleted Sucessfully"})