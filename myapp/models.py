from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post_name = models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    image = models.CharField(max_length=500)


class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    complaint=models.CharField(max_length=500)
    status=models.CharField(max_length=100,default='pending')
    reply=models.CharField(max_length=100,default='pending')


class Document(models.Model):
    FROM_USER= models.ForeignKey(User,on_delete=models.CASCADE,related_name="frm")
    TO_USER= models.ForeignKey(User,on_delete=models.CASCADE,related_name="tom")
    file= models.CharField(max_length=500)
    date=models.DateField()
    imagenarration= models.CharField(max_length=200)
    originalfilename= models.CharField(max_length=250)


class Grp(models.Model):
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    grpname= models.CharField(max_length=100)
    imagefile= models.CharField(max_length=250)


class Grpmember(models.Model):
    GRP= models.ForeignKey(Grp, on_delete=models.CASCADE)
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    privatekey=models.CharField(max_length=1000)
    publickey=models.CharField(max_length=1000)




class GroupDocument(models.Model):
    GROUP= models.ForeignKey(Grp,on_delete=models.CASCADE)
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    file= models.CharField(max_length=500)
    date=models.DateField()
    originalfilename= models.CharField(max_length=250)

class GroupDocumentHash(models.Model):
    GROUPDOCUMENT = models.ForeignKey(GroupDocument, on_delete=models.CASCADE)
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    hashvalue=models.CharField(max_length=1000)







