from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('commonuserregistration/', views.commonuserregistration, name="commonuserregistration"),
    path('userregistrationconfirmation/', views.userregistrationconfirmation, name="userregistrationconfirmation"),
    path('coachregistration/', views.coachregistration, name="coachregistration"),
    path('coachregistrationconfirmation/', views.coachregistrationconfirmation, name="coachregistrationconfirmation"),
    path('institutionregistration/', views.institutionregistration, name="institutionregistration"),
    path('shopsregistration/', views.shopsregistration, name="shopsregistration"),
    path('clubregistration/', views.clubregistration, name="clubregistration"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('usernametaken/', views.usernametaken, name="usernametaken"),
    path('paymentsuccess/',views.paymentsuccess, name="paymentsuccess"),
    path('paymentsuccesstwo/',views.paymentsuccesstwo, name="paymentsuccesstwo"),
    path('successfullyplacedorder/',views.successfullyplacedorder, name="successfullyplacedorder"),
    

    #commonuser section
    path('cuserviewscoach/', views.cuserviewscoach, name="cuserviewscoach"),
    path('cuserviewsinstituitions/', views.cuserviewsinstituitions, name="cuserviewsinstituitions"),
    path('cuserviewsshops/', views.cuserviewsshops, name="cuserviewsshops"),
    path('cuserviewsclubs/', views.cuserviewsclubs, name="cuserviewsclubs"),
    path('commonuserprofile/', views.commonuserprofile, name="commonuserprofile"),
    path('commonuseredit/', views.commonuseredit, name="commonuseredit"),
    path('updatecommonuser/<int:id>',views.updatecommonuser,name='updatecommonuser'),
    path('updatecommonuser/commonuseredt/<int:id>',views.commonuseredt,name='commonuseredt'),
    path('instituitionprofileviewforothers',views.instituitionprofileviewforothers, name="instituitionprofileviewforothers"),
    path('instituitionprofileviewforother/<int:id>',views.instituitionprofileviewforother, name="instituitionprofileviewforother"),
    path('instituitionprofileviewforother/eventsapply/<int:id>',views.eventsapply, name="eventsapply"),
    path('clubprofileviewforothers',views.clubprofileviewforothers, name="clubprofileviewforothers"),
    path('clubprofileviewforother/<int:id>',views.clubprofileviewforother, name="clubprofileviewforother"),
    path('clubprofileviewforother/ceventsapply/<int:id>',views.ceventsapply, name="ceventsapply"),
    path('cuserviewproducts/<int:id>',views.cuserviewproducts, name="cuserviewproducts"),
    path('productpayment/<int:id>/',views.productpayment, name="productpayment"),
    path('productpayment/placeorders/<int:id>/',views.placeorders, name="placeorders"),
    path('commonuserselfdelete/<int:id>/',views.commonuserselfdelete, name="commonuserselfdelete"),
    
    #coach section
    path('coachviewsinstituitions/', views.coachviewsinstituitions, name="coachviewsinstituitions"),
    path('coachviewsshops/', views.coachviewsshops, name="coachviewsshops"),
    path('coachprofile/', views.coachprofile, name="coachprofile"),
    path('coachedit/', views.coachedit, name="coachedit"),
    path('updatecoach/<int:id>',views.updatecoach,name='updatecoach'),
    path('updatecoach/coachedt/<int:id>',views.coachedt,name='coachedt'),
    path('coachselfdelete/<int:id>/',views.coachselfdelete, name="coachselfdelete"),

    #instituitions section
    path('instituitionprofile/', views.instituitionprofile, name="instituitionprofile"),
    path('instituitionedit/', views.instituitionedit, name="instituitionedit"),
    path('updateinstituition/<int:id>',views.updateinstituition,name='updateinstituition'),
    path('updateinstituition/institutionedt/<int:id>',views.institutionedt,name='institutionedt'),
    path('instituitionselfdelete/<int:id>',views.instituitionselfdelete,name='instituitionselfdelete'),
    path('instituitionevnt',views.instituitionevnt, name="instituitionevnt"),
    path('instituitionevnts',views.instituitionevnts, name="instituitionevnts"),
    path('institnevnts',views.institnevnts, name="institnevnts"),
    path('instituitioneventaddconfirmation',views.instituitioneventaddconfirmation, name="instituitioneventaddconfirmation"),
    path('instituitioneventdelete/<int:id>',views.instituitioneventdelete, name="instituitioneventdelete"),
    path('institutionsviewapplications',views.institutionsviewapplications, name="institutionsviewapplications"),
    path('instituitionseventsappltndelete/<int:id>',views.instituitionseventsappltndelete, name="instituitionseventsappltndelete"),
    
    # path('institutionseventsview',views.institutionseventsview, name="institutionseventsview"),
    
    #shops section
    path('shopprofile/', views.shopprofile, name="shopprofile"),
    path('shopedit/', views.shopedit, name="shopedit"),
    path('updateshop/<int:id>',views.updateshop,name='updateshop'),
    path('updateshop/shopedt/<int:id>',views.shopedt,name='shopedt'),
    path('shopaddproducts',views.shopaddproducts, name="shopaddproducts"),
    path('shopaddproduct',views.shopaddproduct, name="shopaddproduct"),
    path('shopproduct',views.shopproduct, name="shopproduct"),
    path('productsaddconfirmation',views.productsaddconfirmation, name="productsaddconfirmation"),
    path('vieworders',views.vieworders, name="vieworders"),
    path('shopsviewsproducts',views.shopsviewsproducts, name="shopsviewsproducts"),
    path('shopselfdelete/<int:id>',views.shopselfdelete, name="shopselfdelete"),
    path('shopproductdelete/<int:id>',views.shopproductdelete, name="shopproductdelete"),
    
    
    #clubs section
    path('clubprofile/', views.clubprofile, name="clubprofile"),
    path('clubedit/', views.clubedit, name="clubedit"),
    path('updateclub/<int:id>',views.updateclub,name='updateclub'),
    path('updateclub/clubedt/<int:id>',views.clubedt,name='clubedt'),
    path('clubevnt',views.clubevnt, name="clubevnt"),
    path('clubevnts',views.clubevnts, name="clubevnts"),
    path('clbevnts',views.clbevnts, name="clbevnts"),
    path('clubeventaddconfirmation',views.clubeventaddconfirmation, name="clubeventaddconfirmation"),
    path('clubsviewsapplications',views.clubsviewsapplications, name="clubsviewsapplications"),
    path('clubselfdelete/<int:id>/',views.clubselfdelete, name="clubselfdelete"),
    # path('clubeventsview',views.clubeventsview, name="clubeventsview"),
    # path('update_status/', views.update_status, name='update_status'),
    
]