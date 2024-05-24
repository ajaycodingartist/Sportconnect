from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from datetime import date
from django.http import JsonResponse
from django.views.generic.base import TemplateView
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from .models import commonuser
from .models import coaches
from .models import instituitions
from .models import shops
from .models import clubs
from .models import instituitionevents
from .models import instituitionseventapplctn
from .models import clubevents
from .models import clubseventapplctn
from .models import product
from .models import order
# Create your views here.
# def index(request):
#     return render(request,'index.html')

def index(request):
    cid = request.session.get('cid')
    chid = request.session.get('chid')
    iid = request.session.get('iid')
    shid = request.session.get('shid')
    clid = request.session.get('clid')

    return render(request, 'index.html', {'cid': cid, 'chid': chid, 'iid': iid, 'shid': shid, 'clid': clid})


def usernametaken(request):
    return render(request, 'usernametaken.html')

#commonuser registration
def commonuserregistration(request):
    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        exists=commonuser.objects.filter(email=email).exists()
        if exists:
            return render(request, 'usernametaken.html')
        else:
            registration=commonuser(username=username,phone=phone,age=age,gender=gender,location=location,email=email,image=image,password=password)
            registration.save()
            return render(request, 'userregistrationconfirmation.html')

    return render(request,'commonuserregistration.html')

def userregistrationconfirmation(request):
    return render(request, 'userregistrationconfirmation.html')

def coachregistration(request):
    if request.method=="POST":
        coachname=request.POST.get('coachname')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        event=request.POST.get('event')
        qualification=request.FILES['qualification']
        g=FileSystemStorage()
        gs=g.save(qualification.name,qualification)
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=coaches(coachname=coachname,phone=phone,age=age,event=event,qualification=qualification,gender=gender,location=location,email=email,image=image,password=password)
        registration.save()
        return render(request, 'coachregistrationconfirmation.html')
    
    return render(request, 'coachregistration.html')

def coachregistrationconfirmation(request):
    return render(request, 'coachregistrationconfirmation.html')

def institutionregistration(request):
    if request.method=="POST":
        instituitionname=request.POST.get('instituitionname')
        supervisername=request.POST.get('supervisername')
        phone=request.POST.get('phone')
        event=request.POST.get('event')
        icertificate=request.FILES['icertificate']
        h=FileSystemStorage()
        hs=h.save(icertificate.name,icertificate)
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=instituitions(instituitionname=instituitionname,supervisername=supervisername,phone=phone,event=event,icertificate=icertificate,location=location,email=email,image=image,password=password)
        registration.save()
        return render(request, 'instituitionregistrationconfirmation.html')
    
    return render(request, 'institutionregistration.html')

def instituitionregistrationconfirmation(request):
    return render(request, 'instituitionregistrationconfirmation.html')

def shopsregistration(request):
    if request.method=="POST":
        shopname=request.POST.get('shopname')
        supervisername=request.POST.get('supervisername')
        phone=request.POST.get('phone')
        shopcertificate=request.FILES['shopcertificate']
        h=FileSystemStorage()
        hs=h.save(shopcertificate.name,shopcertificate)
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=shops(shopname=shopname,supervisername=supervisername,phone=phone,shopcertificate=shopcertificate,location=location,email=email,image=image,password=password)
        registration.save()
        return render(request, 'shopsregistrationconfirmation.html')
    
    return render(request, 'shopsregistration.html')

def shopsregistrationconfirmation(request):
    return render(request, 'shopsregistrationconfirmation.html')

def clubregistration(request):
    if request.method=="POST":
        clubname=request.POST.get('clubname')
        managername=request.POST.get('managername')
        phone=request.POST.get('phone')
        clubid=request.POST.get('clubid')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=clubs(clubname=clubname,managername=managername,phone=phone,clubid=clubid,location=location,email=email,image=image,password=password)
        registration.save()
        return render(request, 'clubregistrationconfirmation.html')
    
    return render(request, 'clubregistration.html')

def clubregistrationconfirmation(request):
    return render(request, 'clubregistrationconfirmation.html')


#login and logout
def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if commonuser.objects.filter(email=email,password=password).exists():
        commonuserdetls=commonuser.objects.get(email=request.POST['email'], password=password)
        if commonuserdetls.password == request.POST['password']:
            request.session['cid'] = commonuserdetls.id
            request.session['cname'] = commonuserdetls.username

            request.session['phone'] = commonuserdetls.phone

            request.session['email'] = email

            request.session['cuser'] = 'cuser'

            return render(request,'index.html')
        
    elif coaches.objects.filter(email=email,password=password).exists():
        coachesdetls=coaches.objects.get(email=request.POST['email'], password=password)
        if coachesdetls.password == request.POST['password']:
            request.session['chid'] = coachesdetls.id
            request.session['chname'] = coachesdetls.coachname

            request.session['phone'] = coachesdetls.phone

            request.session['email'] = email

            request.session['coach'] = 'coach'

            return render(request,'index.html')
        
    elif instituitions.objects.filter(email=email,password=password).exists():
        instituitionsdetls=instituitions.objects.get(email=request.POST['email'], password=password)
        if instituitionsdetls.password == request.POST['password']:
            request.session['iid'] = instituitionsdetls.id
            request.session['iname'] = instituitionsdetls.instituitionname

            request.session['phone'] = instituitionsdetls.phone

            request.session['email'] = email

            request.session['instituition'] = 'instituition'

            return render(request,'index.html')
        
    elif shops.objects.filter(email=email,password=password).exists():
        shopsdetls=shops.objects.get(email=request.POST['email'], password=password)
        if shopsdetls.password == request.POST['password']:
            request.session['shid'] = shopsdetls.id
            request.session['shname'] = shopsdetls.shopname

            request.session['phone'] = shopsdetls.phone

            request.session['email'] = email

            request.session['shop'] = 'shop'

            return render(request,'index.html')
        
    elif clubs.objects.filter(email=email,password=password).exists():
        clubsdetls=clubs.objects.get(email=request.POST['email'], password=password)
        if clubsdetls.password == request.POST['password']:
            request.session['clid'] = clubsdetls.id
            
            request.session['clname'] = clubsdetls.clubname

            request.session['phone'] = clubsdetls.phone

            request.session['email'] = email

            request.session['club'] = 'club'

            return render(request,'index.html')

    else:
        return render(request, 'login.html', {'status': 'Invalid Username or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)
 
#-------------------------Common User section --------------------------------

def cuserviewscoach(request):
    dict_pc={
        'pc': coaches.objects.all()
    }
    return render(request,'cuserviewscoach.html', dict_pc)

def cuserviewsinstituitions(request):
    dict_pc={
        'pc': instituitions.objects.all()
    }
    return render(request,'cuserviewsinstituitions.html', dict_pc)

def cuserviewsshops(request):
    dict_pc={
        'pc': shops.objects.all()
    }
    return render(request,'cuserviewsshops.html', dict_pc)

def cuserviewsclubs(request):
    dict_pc={
        'pc': clubs.objects.all()
    }
    return render(request,'cuserviewsclubs.html', dict_pc)

#commonuser profile

def commonuserprofile(request):
    tem=request.session['cid'] 
    vpro=commonuser.objects.get(id=tem)
    pro=instituitionseventapplctn.objects.filter(username=vpro)
    ro=clubseventapplctn.objects.filter(username=vpro)
    return render(request,'commonuserprofile.html',{'result':vpro, 'res':pro, 're':ro})

class eventlistview(TemplateView):  # Update YourParentClass with the actual parent class
    template_name='commonuserprofile.html'
    # Your view code

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

#commonuser details edit
def commonuseredit(request):
    return render(request,'commonuseredit.html')

def updatecommonuser(request,id):
    upt = commonuser.objects.get(id=id)
    return render(request,'commonuseredit.html',{'result':upt}) 

def commonuseredt(request,id):
    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        commonuseredit=commonuser(username=username,phone=phone,age=age,gender=gender,location=location,email=email,image=image,password=password,id=id)
        commonuseredit.save()

    return redirect(commonuserprofile)

def commonuserselfdelete(request,id):
    member = commonuser.objects.get(id=id)
    member.delete()
    return redirect(commonuserregistration)

def instituitionprofileviewforothers(request):
    return render(request,'instituitionprofileviewforothers.html')

def instituitionprofileviewforother(request,id):
    tem=request.session['cid']
    ro=commonuser.objects.get(id=tem)
    vpro=instituitions.objects.get(id=id)
    pro=instituitionevents.objects.filter(instituitionname=vpro)
    applied_events = instituitionseventapplctn.objects.filter(username=ro, instituitionname__in=pro).values_list('instituitionname_id', flat=True)
    return render(request,'instituitionprofileviewforothers.html',{'res':ro,'result':vpro, 'evnt':pro,'applied_events': applied_events})

def eventsapply(request,id):
    tem=request.session['cid'] 
    if request.method=="POST":
        events_instance = instituitionevents.objects.get(id=id)
        cuser_instance = commonuser.objects.get(id=tem)
        # instituitions_instance = instituitions.objects.get(id=id)
        # instituition_instance = instituitionevents.objects.get(instituitionname=instituitions_instance)
        # instituition_instance = events_instance.instituitionname
        applied_date = date.today()
        evntapply=instituitionseventapplctn(username=cuser_instance,instituitionname=events_instance,applied_date=applied_date,status=False)
        evntapply.save()
        return redirect('instituitionprofileviewforother', id=events_instance.instituitionname.id)

    return redirect('instituitionprofileviewforothers')

def clubprofileviewforothers(request):
    return render(request,'clubprofileviewforothers.html')

def clubprofileviewforother(request,id):
    tem=request.session['cid']
    ro=commonuser.objects.get(id=tem)
    vpro=clubs.objects.get(id=id)
    pro=clubevents.objects.filter(clubname=vpro)
    applied_events = clubseventapplctn.objects.filter(username=ro, clubname__in=pro).values_list('clubname_id', flat=True)
    return render(request,'clubprofileviewforothers.html',{'res':ro,'result':vpro, 'evnt':pro, 'applied_events': applied_events})

# def ceventsapply(request,id):
#     # tem=request.session['cid']
#     tem = request.session.get('cid')
#     if request.method=="POST":
#         clubevents_instance = clubevents.objects.get(id=id)
#         cuser_instance = commonuser.objects.get(id=tem)
#         applied_date = date.today()
#         evntapply=clubseventapplctn(username=cuser_instance,clubname=clubevents_instance,applied_date=applied_date,status=False)
#         evntapply.save()
#         return redirect('clubprofileviewforother', id=clubevents_instance.clubname.id)
    
#     return redirect('clubprofileviewforothers')

def ceventsapply(request,id):
    tem=request.session['cid'] 
    if request.method=="POST":
        clubevents_instance = clubevents.objects.get(id=id)
        cuser_instance = commonuser.objects.get(id=tem)
        applied_date = date.today()
        evntapply=clubseventapplctn(username=cuser_instance,clubname=clubevents_instance,applied_date=applied_date,status=False)
        evntapply.save()
        return redirect('clubprofileviewforother', id=clubevents_instance.clubname.id)

    return redirect('clubprofileviewforothers')

# def cuserviewproducts(request):
#     return render(request,'cuserviewproducts.html')

def cuserviewproducts(request,id):
    vpro=shops.objects.get(id=id)
    pro=product.objects.filter(shopname=vpro)
    return render(request,'cuserviewproducts.html',{'pdt':pro})

def productpayment(request,id):
    tem=request.session['cid']
    ro=commonuser.objects.get(id=tem)
    vpro=product.objects.get(id=id)
    # pro=product.objects.filter(shopname=vpro)
    return render(request,'productpayment.html',{'res':ro,'result':vpro})


def placeorders(request,id):
    tem=request.session['cid'] 
    if request.method=="POST":
        cuser_instance = commonuser.objects.get(id=tem)
        shop_instance = product.objects.get(id=id)
        quantity=request.POST.get('quantity')
        evntapply=order(username=cuser_instance,shopname=shop_instance,productname=shop_instance,price=shop_instance,quantity=quantity)
        evntapply.save()
        # return redirect('productpayment', id=shop_instance.id)
        return redirect('successfullyplacedorder')

    return redirect('successfullyplacedorder')

def successfullyplacedorder(request):
    return render(request,'successfullyplacedorder.html')

def commonuserselfdelete(request,id):
    member = commonuser.objects.get(id=id)
    member.delete()
    return redirect(commonuserregistration)
#-------------------------End of Common User section --------------------------------

#-------------------------Coach section --------------------------------
def coachviewsinstituitions(request):
    dict_pc={
        'pc': instituitions.objects.all()
    }
    return render(request,'coachviewsinstituitions.html', dict_pc)

def coachviewsshops(request):
    dict_pc={
        'pc': shops.objects.all()
    }
    return render(request,'coachviewsshops.html', dict_pc)

def coachprofile(request):
    tem=request.session['chid']
    vpro=coaches.objects.get(id=tem)
    return render(request,'coachprofile.html',{'result':vpro})

#coach details edit
def coachedit(request):
    return render(request,'coachedit.html')

def updatecoach(request,id):
    upt = coaches.objects.get(id=id)
    return render(request,'coachedit.html',{'result':upt}) 

def coachedt(request,id):
    if request.method=="POST":
        coachname=request.POST.get('coachname')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        event=request.POST.get('event')
        qualification=request.FILES['qualification']
        g=FileSystemStorage()
        gs=g.save(qualification.name,qualification)
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=coaches(coachname=coachname,phone=phone,age=age,event=event,qualification=qualification,gender=gender,location=location,email=email,image=image,password=password,id=id)
        registration.save()

    return redirect(coachprofile)

def coachselfdelete(request,id):
    member = coaches.objects.get(id=id)
    member.delete()
    return redirect(coachregistration)
#-------------------------End of Coach section --------------------------------

#-------------------------Instituition section --------------------------------

def instituitionprofile(request):
    tem=request.session['iid']
    vpro=instituitions.objects.get(id=tem)
    pro=instituitionevents.objects.filter(instituitionname=tem)
    return render(request,'instituitionprofile.html',{'result':vpro, 'evnt':pro})

def instituitionedit(request):
    return render(request,'instituitionedit.html')

def updateinstituition(request,id):
    upt = instituitions.objects.get(id=id)
    return render(request,'instituitionedit.html',{'result':upt})

def institutionedt(request,id):
    if request.method=="POST":
        instituitionname=request.POST.get('instituitionname')
        supervisername=request.POST.get('supervisername')
        phone=request.POST.get('phone')
        event=request.POST.get('event')
        icertificate=request.FILES['icertificate']
        h=FileSystemStorage()
        hs=h.save(icertificate.name,icertificate)
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=instituitions(instituitionname=instituitionname,supervisername=supervisername,phone=phone,event=event,icertificate=icertificate,location=location,email=email,image=image,password=password,id=id)
        registration.save()
    
    return redirect(instituitionprofile)

def instituitioneventdelete(request,id):
    member = instituitionevents.objects.get(id=id)
    member.delete()
    return redirect(instituitionprofile)

def instituitionevnt(request):
    return render(request,'instituitionevnt.html')

def instituitionevnts(request):
    tem=request.session['iid']
    upt=instituitions.objects.get(id=tem)
    return render(request,'instituitionevnt.html',{'result':upt})

def institnevnts(request): 
    tem=request.session['iid']
    if request.method=="POST":
        instituition_instance = instituitions.objects.get(id=tem)
        description=request.POST.get('description')
        location=request.POST.get('location')
        event_date=request.POST.get('event_date')
        # event_date = date.today()
        eventsave=instituitionevents(instituitionname=instituition_instance,description=description,location=location,event_date=event_date)
        eventsave.save()
    return render(request,'instituitioneventaddconfirmation.html',{'success':'registered successfully'})

def instituitioneventaddconfirmation(request):
    return render(request,'instituitioneventaddconfirmation.html')


# def institutionsviewapplications(request):
#     tem=request.session['iid']
#     instituition_instance=instituitionevents.objects.get(id=tem)
#     instituitionseventapplctn_instance=instituitionseventapplctn.objects.filter(instituitionname=instituition_instance)
#     return render(request,'institutionsviewapplications.html',{'acknowledgements': instituitionseventapplctn_instance})


def institutionsviewapplications(request):
    tem = request.session['iid']
    vpro = instituitions.objects.get(id=tem)
    pro = instituitionevents.objects.filter(instituitionname=vpro)
    iusers = instituitionseventapplctn.objects.filter(instituitionname__in=pro)
    return render(request, 'institutionsviewapplications.html', {'res': iusers})

def instituitionselfdelete(request,id):
    member = instituitions.objects.get(id=id)
    member.delete()
    return redirect(institutionregistration)

def instituitionseventsappltndelete(request,id):
    member = instituitionseventapplctn.objects.get(id=id)
    member.delete()
    return redirect(institutionsviewapplications)
#-------------------------End of Instituitions section --------------------------------

#-------------------------Shops section --------------------------------
def shopprofile(request):
    tem=request.session['shid']
    vpro=shops.objects.get(id=tem)
    return render(request,'shopprofile.html',{'result':vpro})

def shopedit(request):
    return render(request,'shopedit.html')

def updateshop(request,id):
    upt = shops.objects.get(id=id)
    return render(request,'shopedit.html',{'result':upt})

def shopedt(request,id):
    if request.method=="POST":
        shopname=request.POST.get('shopname')
        supervisername=request.POST.get('supervisername')
        phone=request.POST.get('phone')
        shopcertificate=request.FILES['shopcertificate']
        h=FileSystemStorage()
        hs=h.save(shopcertificate.name,shopcertificate)
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=shops(shopname=shopname,supervisername=supervisername,phone=phone,shopcertificate=shopcertificate,location=location,email=email,image=image,password=password,id=id)
        registration.save()
    
    return redirect(shopprofile)

def shopaddproducts(request):
    return render(request,'shopaddproducts.html')

def shopaddproduct(request):
    tem=request.session['shid']
    upt=shops.objects.get(id=tem)
    return render(request,'shopaddproducts.html',{'result':upt})

def shopproduct(request): 
    tem=request.session['shid']
    if request.method=="POST":
        shops_instance = shops.objects.get(id=tem)
        productname=request.POST.get('productname')
        brandname=request.POST.get('brandname')
        price=request.POST.get('price')
        # event_date = date.today()
        pdtsave=product(shopname=shops_instance,productname=productname,brandname=brandname,price=price)
        pdtsave.save()
    return render(request,'productsaddconfirmation.html',{'success':'registered successfully'})

def productsaddconfirmation(request):
    return render(request,'productsaddconfirmation.html')

def shopsviewsproducts(request):
    tem = request.session['shid']
    vpro = shops.objects.get(id=tem)
    pro = product.objects.filter(shopname=vpro)
    return render(request,'shopsviewsproducts.html', {'res': pro})

def vieworders(request):
    tem = request.session['shid']
    vpro = shops.objects.get(id=tem)
    pro = product.objects.filter(shopname=vpro)
    iusers = order.objects.filter(shopname__in=pro)
    return render(request,'vieworders.html', {'res': iusers})

def shopselfdelete(request,id):
    member = shops.objects.get(id=id)
    member.delete()
    return redirect(shopsregistration)

def shopproductdelete(request,id):
    member = product.objects.get(id=id)
    member.delete()
    return redirect(shopaddproducts)

# tem = request.session['clid']
#     vpro = clubs.objects.get(id=tem)
#     pro = clubevents.objects.filter(clubname=vpro)
#     iusers = clubseventapplctn.objects.filter(clubname__in=pro)
#     return render(request, 'clubsviewsapplications.html', {'res': iusers})
#-------------------------End of Shop section --------------------------------

#-------------------------Clubs section --------------------------------
def clubprofile(request):
    tem=request.session['clid']
    vpro=clubs.objects.get(id=tem)
    pro=clubevents.objects.filter(clubname=tem)
    return render(request,'clubprofile.html',{'result':vpro, 'eventlist':pro})

def clubedit(request):
    return render(request,'clubedit.html')

def updateclub(request,id):
    upt = clubs.objects.get(id=id)
    return render(request,'clubedit.html',{'result':upt})

def clubedt(request,id):
    if request.method=="POST":
        clubname=request.POST.get('clubname')
        managername=request.POST.get('managername')
        phone=request.POST.get('phone')
        clubid=request.POST.get('clubid')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=clubs(clubname=clubname,managername=managername,phone=phone,clubid=clubid,location=location,email=email,image=image,password=password,id=id)
        registration.save()
    
    return redirect(clubprofile)

def clubevnt(request):
    return render(request,'clubevnt.html')

def clubevnts(request):
    tem=request.session['clid']
    upt=clubs.objects.get(id=tem)
    return render(request,'clubevnt.html',{'result':upt})

def clbevnts(request): 
    tem=request.session['clid']
    if request.method=="POST":
        club_instance = clubs.objects.get(id=tem)
        description=request.POST.get('description')
        location=request.POST.get('location')
        event_date=request.POST.get('event_date')
        # event_date = date.today()
        eventsave=clubevents(clubname=club_instance,description=description,location=location,event_date=event_date)
        eventsave.save()
    return render(request,'clubeventaddconfirmation.html',{'success':'registered successfully'})

def clubeventaddconfirmation(request):
    return render(request,'clubeventaddconfirmation.html')



# def clubsviewsapplications(request):
#     tem=request.session['clid']
#     vpro=clubs.objects.get(id=tem)
#     pro=clubevents.objects.filter(clubname=vpro)
#     # iusers=clubseventapplctn.objects.filter(clubname=vpro)
#     iusers = clubseventapplctn.objects.filter(clubname__in=pro.values_list('clubname', flat=True))
#     return render(request,'clubsviewsapplications.html',{ 'res':iusers })

def clubsviewsapplications(request):
    tem = request.session['clid']
    vpro = clubs.objects.get(id=tem)
    pro = clubevents.objects.filter(clubname=vpro)
    iusers = clubseventapplctn.objects.filter(clubname__in=pro)
    return render(request, 'clubsviewsapplications.html', {'res': iusers})

def clubselfdelete(request,id):
    member = clubs.objects.get(id=id)
    member.delete()
    return redirect(clubregistration)


# def update_status(request):
#     if request.method == 'POST' and request.is_ajax():
#         application_id = request.POST.get('application_id')
#         new_status = request.POST.get('new_status')

#         # Perform validation and update status in the database
#         try:
#             application = clubseventapplctn.objects.get(pk=application_id)
#             application.status = new_status
#             application.save()
#             return JsonResponse({'success': True})
#         except clubseventapplctn.DoesNotExist:
#             pass  # Handle the case where the application does not exist

#     return JsonResponse({'success': False})
#-------------------------End of Club section --------------------------------

def paymentsuccess(request):  #1st option payment
    if request.method == 'POST':
        # stripe.api_key = settings.STRIPE_SECRET_KEY 
        paymentsuccess = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request,'paymentsuccess.html')
    
def paymentsuccesstwo(request):  #1st option payment
    if request.method == 'POST':
        # stripe.api_key = settings.STRIPE_SECRET_KEY 
        paymentsuccess = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request,'paymentsuccess.html')