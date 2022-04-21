from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("sendlist/",views.sendlist,name="sendlist"),
    path("transfer/<int:id>",views.transfer,name="transfer"),
    path("receivelist/",views.receivelist,name="receivelist"),
    path("confirm/<int:id_receive>",views.confirm,name="confirm"),
    path("success/",views.success,name="success"),
    path('history/<int:id_history>',views.history,name="history"),
]