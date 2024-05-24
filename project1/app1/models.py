from django.db import models

# Create your models here.
class commonuser(models.Model):
    username=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='cmnusers')
    password=models.CharField(max_length=200)

    def __str__(self): 
        return self.username
    
class coaches(models.Model):
    coachname=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    event=models.CharField(max_length=200)
    qualification=models.FileField(upload_to='certificates')
    gender=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='chusers')
    password=models.CharField(max_length=200)

    def __str__(self): 
        return self.coachname
    
class instituitions(models.Model):
    instituitionname=models.CharField(max_length=200)
    supervisername=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    event=models.CharField(max_length=200)
    icertificate=models.FileField(upload_to='instncertificates')
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='instn')
    password=models.CharField(max_length=200)

    def __str__(self): 
        return self.instituitionname
    
class shops(models.Model):
    shopname=models.CharField(max_length=200)
    supervisername=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    shopcertificate=models.FileField(upload_to='shpcertificates')
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='shp')
    password=models.CharField(max_length=200)

    def __str__(self): 
        return self.shopname
    
class clubs(models.Model):
    clubname=models.CharField(max_length=200)
    managername=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    clubid=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='clb')
    password=models.CharField(max_length=200)

    def __str__(self): 
        return self.clubname
    
class instituitionevents(models.Model):
    instituitionname=models.ForeignKey(instituitions, on_delete=models.CASCADE)
    description=models.TextField()
    location=models.CharField(max_length=200)
    event_date=models.DateField(max_length=200)

    def __str__(self): 
        return f"{self.instituitionname}"

class clubevents(models.Model):
    clubname=models.ForeignKey(clubs, on_delete=models.CASCADE)
    description=models.TextField()
    location=models.CharField(max_length=200)
    event_date=models.DateField(max_length=200)

    def __str__(self): 
        return f"{self.clubname}"

class  instituitionseventapplctn(models.Model):
    username = models.ForeignKey(commonuser, on_delete=models.CASCADE)
    instituitionname=models.ForeignKey(instituitionevents, on_delete=models.CASCADE)
    applied_date=models.DateField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.username} applied for {self.instituitionname}"


class  clubseventapplctn(models.Model):
    username = models.ForeignKey(commonuser, on_delete=models.CASCADE)
    clubname=models.ForeignKey(clubevents, on_delete=models.CASCADE)
    applied_date=models.DateField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.username} applied for {self.clubname}"
    
class products(models.Model):
    shopname = models.ForeignKey(shops, on_delete=models.CASCADE)
    productname=models.CharField(max_length=200)
    brandname=models.CharField(max_length=200)
    price=models.CharField(max_length=200)

    def __str__(self): 
        return f"{self.shopname} added {self.productname}"
    
class product(models.Model):
    shopname = models.ForeignKey(shops, on_delete=models.CASCADE)
    productname=models.CharField(max_length=200)
    brandname=models.CharField(max_length=200)
    price=models.CharField(max_length=200)

    def __str__(self): 
        return f"{self.shopname} added {self.productname}"
    
class order(models.Model):
    username = models.ForeignKey(commonuser, on_delete=models.CASCADE)
    shopname = models.ForeignKey(product, on_delete=models.CASCADE, related_name='orders_by_shopname')
    productname=models.ForeignKey(product, on_delete=models.CASCADE, related_name='orders_by_productname')
    price=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=200)

    def __str__(self): 
        return f"{self.username} ordered {self.productname} from {self.shopname}"