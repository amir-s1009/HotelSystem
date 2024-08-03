from . import models
from .models import Customer, Reservation, Room, manager
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.http import require_http_methods
import datetime

def test(request):
    #print(Customer.objects.all())
    #print(Reservation.objects.all())
    #print(Room.objects.all())
    #for user in Customer.objects.all():
    #   print(user.reservation_set.all())

    #manager.objects.create(name="", family="", username="admin", password="admin")
    return HttpResponse(status=200)

@require_http_methods(["GET"])
def logout(request):
    return redirect("loginPage")

@require_http_methods(["GET"])
def signupPage(request):
    return render(request, "main/signup.html", {})

@require_http_methods(["POST"])
def signup(request):
    if(not Customer.objects.filter(username = request.POST["username"])):
        if(request.POST["password"] and
            request.POST["name"] and
            request.POST["family"] and
            request.POST["mobile"] and
            request.POST["nationalId"] and
            request.POST["email"]
        ):
            if(len(request.POST["mobile"]) == 11 and
                len(request.POST["nationalId"]) == 10
            ):
                Customer.objects.create(
                    username=request.POST["username"],
                    password=request.POST["password"],
                    name=request.POST["name"],
                    family = request.POST["family"],
                    mobile = request.POST["mobile"],
                    nationalId = request.POST["nationalId"],
                    email = request.POST["email"]
                )
                messages.success(request, "ثبت نام شما با موفقیت انجام یافت", extra_tags="s")
                return redirect("loginPage")
            else:
                messages.error(request, "شماره موبایل یا کد ملی غیر مجاز میباشد", extra_tags="f")
                return redirect(signupPage)
        else:
            messages.error(request, "اطلاعات وارد شده غیر مجاز میباشد", extra_tags="f")
            return redirect(signupPage)
    else:
        messages.error(request, "این نام کاربری موجود است", extra_tags="f")
        return redirect(signupPage)

@require_http_methods(["GET"])
def loginPage(request):
    return render(request, "main/login.html", {})

@require_http_methods(["POST"])
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    userType = request.POST["userType"]
    if(userType == "0"):
        try:
            customer = Customer.objects.get(username=username, password=password)
            return render(request, "main/customer-dashboard.html", {"user":customer})
        except Customer.DoesNotExist:
            messages.error(request, "لطفا اطلاعات را درست وارد نمایید", extra_tags="f")
            return redirect("loginPage")
    elif(userType == "1"):
        try:
            mang = manager.objects.get(username=username, password=password)
            return render(request, "main/manager-dashboard.html", {"admin":mang})
        except manager.DoesNotExist:
            messages.error(request, "لطفا اطلاعات را درست وارد نمایید", extra_tags="f")
            return redirect("loginPage")
    else:
        messages.error(request, "نوع کاربری را مشخص فرمایید", extra_tags="f")
        return redirect("loginPage")
        
@require_http_methods(["GET"])
@xframe_options_exempt
def customerInfoPage(request, username, password):
    return render(request, "main/customer-info.html", {"user":Customer.objects.get(username=username, password=password)})

@require_http_methods(["POST"])
def updateCustomerInfo(request):
    try:
        user = Customer.objects.get(username=request.POST["username"], password=request.POST["password"])
        user.username = request.POST['newUsername']
        user.password = request.POST['newPassword']
        user.name = request.POST['name']
        user.family = request.POST['family']
        user.mobile = request.POST['mobile']
        user.nationalId = request.POST['nationalId']
        user.email = request.POST['email']
        user.save()

        messages.success(request, "تغییرات با موفقیت اعمال شد", extra_tags="s")
        return redirect("customerInfo", username=user.username, password=user.password)
    except Customer.DoesNotExist:
        messages.error(request, "خطایی رخ داد", extra_tags="f")
        return redirect("customerInfo", username=user.username, password=user.password)


@require_http_methods(["GET"])
@xframe_options_exempt
def managerRoomsPage(request, username, password):
    if(manager.objects.get(username=username, password=password)):
        return render(request, "main/rooms.html", {"rooms":Room.objects.all(), "admin":{"username":username, "password":password}})

@require_http_methods(["POST"])
def addRoom(request, username, password):
    if manager.objects.get(username=username, password=password):
        Room.objects.create(
            no=int(request.POST["no"]),
            capacity=int(request.POST["capacity"]),
            beds=int(request.POST["beds"]),
            ecoclass=int(request.POST["ecoclass"]),
            isIdle=True,
        )
        messages.success(request, "اتاق جدید به شماره "+request.POST["no"]+" افزوده شد", extra_tags="s")
        return redirect("rooms", username=username, password=password)

        
@require_http_methods(["GET"])
def deleteRoom(request, no, username, password):
    try:
        if manager.objects.get(username=username, password=password):
            room = Room.objects.get(no=no)
            room.delete()
            messages.success(request, "اتاق با موفقیت حذف گردید", extra_tags="s")
            return redirect("rooms", username=username, password=password)
    except Room.DoesNotExist:
        messages.error(request, "اتاق یافت نشد", "f")
        return redirect("rooms", username=username, password=password)

@require_http_methods(["GET"])
@xframe_options_exempt
def reservations(request, username, password):
    if manager.objects.get(username=username, password=password):
        return render(request, "main/manageReservation.html", {"reservations":Reservation.objects.all(), "admin":{"username":username, "password":password}})

@require_http_methods(["GET"])
@xframe_options_exempt
def cutomerViewRooms(request, username, password):
    return render(request, "main/customer-reserve.html", {"rooms":[], "user":Customer.objects.get(username=username, password=password)})


@require_http_methods(["POST"])
@xframe_options_exempt
def cutomerFilterRooms(request, username, password):
    #date format: yyyy-mm-dd
    #time format: hh:mm
    sdate = request.POST["startDate"]
    stime = request.POST["startTime"]
    fDate = request.POST["endDate"]
    fTime = request.POST["endTime"]
    reservations = list(Reservation.objects.filter(
        endDate__gt=datetime.date(int(sdate[0:3]), int(sdate[5:7]), int(sdate[8:10])),
        endTime__gt=datetime.time(int(stime[0:2]), int(stime[3:5]))
    ))
    reservations = reservations+list(
        Reservation.objects.filter(
            startDate__gt=datetime.date(int(fDate[0:3]), int(fDate[5:7]), int(fDate[8:10])),
            startTime__gt=datetime.time(int(fTime[0:2]), int(fTime[3:5]))
        )
    )   
    not_needed_rooms = []
    for reservation in reservations:
        if reservation.room not in not_needed_rooms:
            not_needed_rooms.append(reservation.room.no)
    print(reservations)
    needed_rooms = []
    allRooms = Room.objects.all()
    for room in allRooms:
        if room.no not in not_needed_rooms:
            needed_rooms.append(room)
    return render(request, "main/customer-reserve.html",
        {
        "rooms":needed_rooms,
        "user":Customer.objects.get(username=username, password=password),
        "datetime":{"sd":sdate, "st":stime, "ed":fDate, "et":fTime}
        })

@require_http_methods(["GET"])
@xframe_options_exempt
def customerViewReservations(request, username, password):
    data = Reservation.objects.filter(customer__username=username, customer__password=password)
    return render(request, "main/customer-reservations.html", {"reserves":data})

@require_http_methods(["GET"])
def customerReservation(request, roomId, startDate, startTime, endDate, endTime, username, password):
    targetRoom = Room.objects.get(pk=roomId)
    targetCustomer = Customer.objects.get(username=username, password=password)
    reserve = Reservation(
        startDate = datetime.date(int(startDate[0:3]), int(startDate[5:7]), int(startDate[8:10])),
        startTime = datetime.time(int(startTime[0:2]), int(startTime[4:6])),
        endDate = datetime.date(int(endDate[0:3]), int(endDate[5:7]), int(endDate[8:10])),
        endTime = datetime.time(int(endTime[0:2]), int(endTime[4:6])),
        isActive = False,
        score = None,
        room = targetRoom,
        customer = targetCustomer
    )
    reserve.save()
    messages.success(request, "رزرو شما با موفقیت به شماره "+str(reserve.id)+" ثبت شد", extra_tags="s")
    return redirect("customer-reservations", username=username, password=password)

@require_http_methods(["GET"])
def deleteReservation(request, id, username, password):
    reserve = Reservation.objects.get(pk=id)
    reserve.isActive = False
    reserve.room.isIdle = True
    reserve.room.save()
    reserve.save()
    messages.success(request, "رزرو با موفقیت ابطال شد", extra_tags="s")
    return redirect("reservations", username=username, password=password)

@require_http_methods(["GET"])
def acceptReservation(request, id, username, password):
    reserve = Reservation.objects.get(pk=id)
    reserve.isActive = True
    reserve.room.isIdle = False
    reserve.room.save()
    reserve.save()
    messages.success(request, "رزرو با موفقیت تایید شد", extra_tags="s")
    return redirect("reservations", username=username, password=password)

@require_http_methods(["POST"])
def scoreReservation(request, id, username, password):
    try:
        reserve = Reservation.objects.get(customer__username=username, customer__password=password, id=id)
        reserve.score = int(request.POST["rate"])
        reserve.save()
        messages.success(request, "امتیاز شما ثبت گردید، با تشکر  از همکاری شما")
        return redirect("customer-reservations", username=username, password=password)
    except:
        messages.error(request, "خطا در امتیازدهی رخ داد")
        return redirect("customer-reservations", username=username, password=password)