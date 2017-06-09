from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import *
from mapper.models import MapperNGO
from anganwadi.models import *
# Create your views here.

def index(request):

    if request.method=="POST":

        print(request.POST)

        name = request.POST['name']
        category = request.POST['category']
        desc = request.POST['desc']
        location = request.POST['location']
        category_obj = Category.objects.get(name = category)
        complaint_user = CustUser.objects.get(user=request.user)
        complaint=Complaint(complaint_user=complaint_user,name_child=name,category=category_obj,desc=desc, location=location)

        complaint.save()

        return render(request,"complaint/complaintform.html",{"message":"Complaint registered successfully"})
    else:
        context={}
        if request.user.is_authenticated:
            cust_user = CustUser.objects.get(user = request.user)

            if cust_user.get_user_type_display() == "Normal":
                categories = Category.objects.all()
                context = {
                    "categories": categories
                }
                return render(request, "complaint/complaintform.html", context)

            elif cust_user.get_user_type_display() == "Volunteer" :
                complaints = Complaint.objects.filter(status="URV")

            elif cust_user.get_user_type_display() == "State Coordinator" :
                complaints = Complaint.objects.filter(status="URSC")

            elif cust_user.get_user_type_display() == "Category Coordinator" :
                complaints = Complaint.objects.filter(status="URCC")

            elif cust_user.get_user_type_display() == "Category Coordinator":
                complaints = Complaint.objects.filter(status="URA")

            context = {
                "complaints": complaints,
            }
            return render(request,"complaint/dashboard.html",context)
        else:
            categories = Category.objects.all()
            context={
                "categories": categories
            }
            return render(request,"user/signup.html",context)


def update_complaint(request):

    context={}
    print("in here")
    if request.method=="POST":
        name = request.POST['name']
        value = request.POST['value']
        complaint = Complaint.objects.get(id=int(value))
        print(complaint)
        if name == "Approved-cancel" or name=="Approval-cancel":
            complaint.status = "RJ"
        else:
            status = complaint.status
            if status == "URV":
                complaint.status="URSC"
            elif status == "URSC":
                complaint.status = "URCC"
            elif status == "URCC":
                complaint_cat = complaint.category
                ngos = MapperNGO.objects.filter(category = complaint_cat)

                for ngo in ngos:
                    if ngo.ngo_name == "anganwadi":
                        transfer = AnganwadiComplaint(complaint_user = request.user.username, location = complaint.location, name_child = complaint.name_child, desc = complaint.desc, status = "PD")
                        transfer.save()

                complaint.status = "URA"
            elif status == "URA":
                complaint.status = "AP"

        complaint.save()
    return render(request,"complaint/index.html",context)

