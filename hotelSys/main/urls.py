from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signupPage, name="signupPage"),
    path('signup/createUser', views.signup, name="createUser"),
    path('login/', views.loginPage, name="loginPage"),
    path('login/validate', views.login, name="validateUser"),
    path('customer/info/<str:username>/<str:password>', views.customerInfoPage, name="customerInfo"),
    path('customer/info/update', views.updateCustomerInfo, name="updateCustomerInfo"),
    path('customer/reservations/<str:username>/<str:password>', views.customerViewReservations, name="customer-reservations"),
    path('customer/reservations/<str:username>/<str:password>/<int:id>', views.scoreReservation, name="scoreReservation"),
    path('room/all/<str:username>/<str:password>', views.managerRoomsPage, name="rooms"),
    path('room/customerview/<str:username>/<str:password>', views.cutomerViewRooms, name="customer-rooms"),
    path('room/customerfilter/<str:username>/<str:password>', views.cutomerFilterRooms, name="customer-filter-rooms"),
    path('room/delete/<int:no>/<str:username>/<str:password>', views.deleteRoom, name="deleteRoom"),
    path('room/add/<str:username>/<str:password>', views.addRoom, name="addRoom"),
    path('reservation/all/<str:username>/<str:password>', views.reservations, name="reservations"),
    path('reservation/request/<int:roomId>/<str:startDate>/<str:startTime>/<str:endDate>/<str:endTime>/<str:username>/<str:password>', views.customerReservation, name="customer-reserve"),
    path('reservation/delete/<int:id>/<str:username>/<str:password>', views.deleteReservation, name="deleteReservation"),
    path('reservation/accept/<int:id>/<str:username>/<str:password>', views.acceptReservation, name="acceptReservation"),
    path('test/', views.test)
]
