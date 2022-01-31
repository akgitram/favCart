from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id',"cname","capic","cdate")
admin.site.register(category,categoryAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","passwd","ppic","address")
admin.site.register(profile,profileAdmin)


class loginAdmin(admin.ModelAdmin):
    list_display=("username","passwd")
admin.site.register(login,loginAdmin)


class productsAdmin(admin.ModelAdmin):
    list_display=("name","ppic","color","tprice","disprice","pdes","category","pdate")
admin.site.register(products,productsAdmin)

class orderAdmin(admin.ModelAdmin):
    list_display=("id","pid","userid","remarks","status","odate")
admin.site.register(order,orderAdmin)

class addtocartAdmin(admin.ModelAdmin):
    list_display=('id',"pid","userid","status","odate")
admin.site.register(addtocart,addtocartAdmin)
