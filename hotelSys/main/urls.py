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
    path('room/all/', views.managerRoomsPage, name="rooms"),
    path('room/customerview/<str:username>/<str:password>', views.cutomerViewRooms, name="customer-rooms"),
    path('room/customerfilter/<str:startDate>/<str:endDate>', views.cutomerFilterRooms, name="customer-filter-rooms", kwargs={"username":"amir1382", "password":"1382"}),
    path('room/delete/<int:no>/', views.deleteRoom, name="deleteRoom"),
    path('reservation/all/', views.reservations, name="reservations"),
    path('reservation/request/<int:roomId>/<str:username>/<str:password>', views.customerReservation, name="customer-reserve"),
    path('reservation/delete/<int:id>/', views.deleteReservation, name="deleteReservation"),
    path('reservation/accept/<int:id>/', views.acceptReservation, name="acceptReservation"),
    path('test/', views.test)
]
