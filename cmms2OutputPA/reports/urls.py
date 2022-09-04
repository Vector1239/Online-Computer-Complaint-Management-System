from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	 path('',views.home,name="home"),
     path("student_login/",views.slogin,name="slogin"),
     path("admin_login/",views.alogin,name="alogin"),
     path("logout/",views.logoutUser,name="logout"),
     path("userLog",views.userLogs,name="userLog"),
     path("send_otp",views.send_otp,name="send otp"),
     path("dashboard/navigation/block/",views.sdashB,name="sdashB"),
     path("dashboard/navigation/<int:pk_b>/lab/",views.sdashL,name="sdashL"),
     path("dashboard/navigation/<int:pk_b>/<int:pk_l>/room/",views.comp,name="comp"),
     path("dashboard/navigation/<int:pk_b>/<int:pk_l>/<int:pk_c>/report/",views.thing,name="thing"),
     path("dashboard/navigation/<int:pk_b>/<int:pk_l>/<int:pk_c>/areport/",views.issue,name="issue"),
     path("dashboard/navigation/<int:pk_b>/<int:pk_l>/aroom/",views.acomp,name="acomp"),
]