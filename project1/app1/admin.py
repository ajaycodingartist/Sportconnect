from django.contrib import admin

# Register your models here.
from . models import commonuser
from . models import coaches
from . models import instituitions
from . models import shops
from . models import clubs
from . models import instituitionevents
from . models import clubevents
from . models import instituitionseventapplctn
from . models import clubseventapplctn
from . models import product
from . models import order


class commonuseradmin(admin.ModelAdmin):
    list_display = ('username','phone','age','gender','location','email','image','password')

class coachadmin(admin.ModelAdmin):
    list_display = ('coachname','phone','age','event','qualification','gender','location','email','image','password')

class instituitionsadmin(admin.ModelAdmin):
    list_display = ('instituitionname','supervisername','phone','event','icertificate','location','email','image','password')

class shopsadmin(admin.ModelAdmin):
    list_display = ('shopname','supervisername','phone','shopcertificate','location','email','image','password')

class clubsadmin(admin.ModelAdmin):
    list_display = ('clubname','managername','phone','clubid','location','email','image','password')

class instituitioneventsadmin(admin.ModelAdmin):
    list_filter = ('instituitionname','description','location','event_date')

class clubeventsadmin(admin.ModelAdmin):
    list_filter = ('clubname','description','location','event_date')

class instituitionseventapplctnadmin(admin.ModelAdmin):
    list_filter = ('username','instituitionname','applied_date','status')

class clubseventapplctnadmin(admin.ModelAdmin):
    list_filter = ('username','clubname','applied_date','status')

class productadmin(admin.ModelAdmin):
    list_filter = ('shopname','productname','brandname','price')

class orderadmin(admin.ModelAdmin):
    list_filter = ('username','shopname','productname','price','quantity')
    

admin.site.register(commonuser, commonuseradmin)
admin.site.register(coaches, coachadmin)
admin.site.register(instituitions, instituitionsadmin)
admin.site.register(shops, shopsadmin)
admin.site.register(clubs, clubsadmin)
admin.site.register(instituitionevents, instituitioneventsadmin)
admin.site.register(clubevents, clubeventsadmin)
admin.site.register(instituitionseventapplctn, instituitionseventapplctnadmin)
admin.site.register(clubseventapplctn, clubseventapplctnadmin)
admin.site.register(product, productadmin)
admin.site.register(order, orderadmin)