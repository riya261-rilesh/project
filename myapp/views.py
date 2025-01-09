import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from myapp.models import Login, Complaint, User, Document, Grp, Grpmember, GroupDocument, GroupDocumentHash


def mailsending(receiver_email,subject,body):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    def send_email(sender_email, sender_password, receiver_email, subject, body):
        # Gmail's SMTP server address and port
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Attach the body with the email
        msg.attach(MIMEText(body, "plain"))

        try:
            # Connect to Gmail's SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection

            # Login to the Gmail account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")

        except Exception as e:
            print(f"Failed to send email: {e}")

        finally:
            # Close the connection to the server
            server.quit()

    # Usage
    sender_email = "your_email@gmail.com"
    sender_password = "your_password_or_app_password"


    send_email(sender_email, sender_password, receiver_email, subject, body)


def login(request):
    return render(request,'lindex.html')

def login_post(request):
    lusername=request.POST['username']
    lpassword=request.POST['password']
    result=Login.objects.filter(username=lusername,password=lpassword)
    if result.exists():
        result2=Login.objects.get(username=lusername,password=lpassword)
        request.session['lid']=result2.id
        if result2.type=='admin':
            return HttpResponse('''<script>alert('admin login success');window.location='/myapp/admin_home/ '</script>''')
        elif result2.type=='user':
            return HttpResponse('''<script>alert('user login success');window.location='/myapp/user_home/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password or username');'</script>''')

    else:
        return HttpResponse('''<script>alert('invalid password or bad credential');window.location='/myapp/login/'</script>''')


def logout(request):
    request.session['lid']=""
    return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

def admin_home(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    return render(request,'admin/adminindex.html')



def admin_change_password(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    return render(request,'admin/admin_change_password.html')

def admin_change_password_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    old = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']
    var= Login.objects.get(id=request.session['lid'])
    if var.password==old:
        if new == confirm:
            var.password=confirm
            var.save()
            return HttpResponse(
                '''<script>alert("user password changed");window.location='/myapp/login'</script>''')
        else:
            HttpResponse('INVALID CONFIRM PASSWORD')
    else:
       return HttpResponse('''<script>alert("INVALID PASSWORD");window.location='/myapp/admin_change_password'</script>''')

def admin_view_complaints(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    var=Complaint.objects.all()
    return render(request,'admin/view_complaint.html',{'var':var})

def admin_view_complaints_search(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    f=request.POST["f"]
    t=request.POST["t"]
    var=Complaint.objects.filter(date__range=[f,t])
    return render(request,'admin/view_complaint.html',{'var':var})

def complaint_reply(request,id):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    var=Complaint.objects.get(id=id)
    return render(request,'admin/complaint_reply.html',{'var':var})

def complaint_reply_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    var=request.POST['reply']
    var2=request.POST['id']
    a=Complaint.objects.get(id=var2)
    a.reply=var
    a.status='repied'
    a.save()
    return HttpResponse('''<script>alert("reply has been successfully sent");window.location='/myapp/admin_view_complaints/'</script>''')



def view_user(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    res=User.objects.all()
    return render(request,"admin/viewuser.html",{'data':res})

def search_user(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    search = request.POST['search']
    res=User.objects.filter(name__icontains=search)
    return render(request,"admin/viewuser.html",{'data':res})






###################user


def user_home(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    return redirect('/myapp/view_user_profile/')


def change_password(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    return render(request,'user/change_password.html')

def change_password_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    old = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']
    var= Login.objects.get(id=request.session['lid'])
    if var.password==old:
        if new == confirm:
            var.password=confirm
            var.save()
            return HttpResponse('''<script>alert("user password changed");window.location='/myapp/login/'</script>''')
        else:
            HttpResponse('INVALID CONFIRM PASSWORD')
    else:
       return HttpResponse('''<script>alert("INVALID PASSWORD");window.location='/myapp/change_password/'</script>''')

def signup(request):

    return render(request, "user/user_signup_index.html")

def signup_post(request):

    name = request.POST['textfield']
    dob = request.POST['textfield8']
    gender = request.POST['RadioGroup1']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']

    house = request.POST['textfield14']
    place = request.POST['textfield4']

    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    password = request.POST['textfield16']

    photo = request.FILES['fileField']

    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    var = Login()
    var.username = email
    var.password = password
    var.type = 'user'
    var.save()

    var2 = User()
    var2.LOGIN_id = var.id
    var2.name = name
    var2.house_name = house
    var2.post_name = post
    var2.pin = pin
    var2.place = place
    var2.dob = dob
    var2.phone = phone
    var2.gender = gender
    var2.email = email
    var2.image=path
    var2.save()

    return HttpResponse('''<script>alert("user register success");window.location='/myapp/login/'</script>''')

def view_user_profile(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    var = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/view_profile.html',{'data':var})

def edit_profile(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    res = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/edit_profile.html",{'data':res})

def editprofilepost(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    name = request.POST['textfield']
    dob = request.POST['textfield8']
    gender = request.POST['RadioGroup1']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']

    house = request.POST['textfield14']
    place = request.POST['textfield4']

    post = request.POST['textfield5']
    pin = request.POST['textfield6']

    lid=request.session['lid']

    var2 = User.objects.get(LOGIN_id=lid)
    var2.name = name
    var2.house_name = house
    var2.post_name = post
    var2.pin = pin
    var2.place = place
    var2.dob = dob
    var2.phone = phone
    var2.gender = gender
    var2.email = email
    var2.save()

    l = Login.objects.get(id=lid)
    l.username = email
    l.save()

    return HttpResponse('''<script>alert("successfully updated");window.location='/myapp/view_user_profile/'</script>''')

def sent_complaint(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    return render(request,'user/send_complaints.html')

def sent_complaint_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    var=request.POST['complaint']

    date=datetime.datetime.now().strftime('%Y-%m-%d')
    c_obj=Complaint()
    c_obj.complaint=var
    c_obj.date=date
    lid = request.session['lid']
    id = User.objects.get(LOGIN_id=lid)
    c_obj.USER_id = id.id
    # c_obj.USER_id=User.objects.get(LOGIN_id=request.session['lid']).LOGIN_id
    c_obj.save()
    return HttpResponse('''<script>alert("complaint succesfully sent");window.location='/myapp/user_home/'</script>''')




def user_view_reply(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    var=Complaint.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/view_reply.html',{'var':var})

def user_view_replysearch(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert("You are Logout...");window.location='/myapp/login/'</script>''')

    f=request.POST['f']
    t=request.POST['t']
    var=Complaint.objects.filter(USER__LOGIN=request.session['lid'], date__range=[f,t])
    return render(request,'user/view_reply.html',{'var':var})



def start(request):

    return render(request,"start.html")




def fileupload(request):

    u=User.objects.all().exclude(LOGIN_id= request.session['lid'])

    return render(request,"user/fileupload.html",{'u':u})

def group_fileupload(request):

    u=Grp.objects.all()

    li=[]

    for i in u:

        if Grpmember.objects.filter(GRP=i,USER__LOGIN_id=request.session['lid']).exists():
            li.append(i)


    return render(request,"user/group_fileupload.html",{'u':li})


def fileuploadpost(request):

    image= request.FILES["file"]
    filetobeuploaded= request.FILES["file2"]
    narration= request.POST["narration"]
    # filetobeuploaded= request.FILES["file2"]
    import  cv2
    fs=FileSystemStorage()
    from datetime import  datetime

    fname= datetime.now().strftime("%y%m%d%H%M%S")+".bmp"
    fname2= datetime.now().strftime("%y%m%d%H%M%S")

    fs.save(fname,image)
    img= cv2.imread("D:\\vce\\media\\"+fname)

    fs.save(fname2+filetobeuploaded.name, filetobeuploaded)

    b,g,r= cv2.split(img)

    w=img.shape[0]
    h=img.shape[1]

    k=""


    for y in range(0,w):
        for x in range(0,h):
            d= r[y,x]
            d= d& 1
            k= k+ str(d)

    bytestring= k.encode("utf-8")
    import  hashlib
    shahash= hashlib.md5(bytestring)  ##using md5 hash
    print(type(shahash))

    hash_bytes = shahash.digest()
    print(hash_bytes, len(hash_bytes))  # Output: b'\x04\x1a\xdd\xcd...\x93\x1b\xcd'

    hash_hex = shahash.hexdigest()
    print(hash_hex)

    import pyAesCrypt
    # custom encryption/decryption buffer size (default is 64KB)
    bufferSize = 128 * 1024
    password = str(hash_hex)
    # encrypt
    pyAesCrypt.encryptFile("D:\\vce\\media\\"+fname2+filetobeuploaded.name, "D:\\vce\\media\\"+fname2+"data.txt.aes", password, bufferSize)

    # pyAesCrypt.decryptFile("J:\\2024\\mdit_crypto\\vce\\media\\"+fname2+"data.txt.aes","J:\\2024\\mdit_crypto\\vce\\media\\aa.bmp" , password, bufferSize)


    user= request.POST["user"]

    d=Document()
    d.FROM_USER= User.objects.get(LOGIN_id= request.session['lid'])
    d.date= datetime.now()
    d.file="/media/"+fname2+"data.txt.aes"
    d.originalfilename= filetobeuploaded.name
    d.imagenarration=  narration
    d.TO_USER = User.objects.get(id=user)
    d.save()

    return  HttpResponse("<script>alert('Document uploaded successfully');window.location='/myapp/fileupload/'</script>")




def group_fileuploadpost(request):

    filetobeuploaded= request.FILES["file2"]

    grpid= request.POST["grpid"]

    # filetobeuploaded= request.FILES["file2"]
    import  cv2
    fs=FileSystemStorage()
    from datetime import  datetime

    fname= datetime.now().strftime("%y%m%d%H%M%S")+".bmp"
    fname2= datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(fname2+filetobeuploaded.name, filetobeuploaded)

    grpfilename= Grp.objects.get(id=grpid).imagefile.replace("/media/","")

    print(grpfilename)

    print("D:\\vce\\media\\"+ grpfilename)

    img=cv2.imread("D:\\vce\\media\\"+ grpfilename)

    # cv2.imshow("imgname",img)
    #
    # cv2.waitKey(100)
    b,g,r= cv2.split(img)
    w=img.shape[0]
    h=img.shape[1]

    k=""
    for y in range(0,w):
        for x in range(0,h):
            d= r[y,x]
            d= d& 1
            k= k+ str(d)

    bytestring= k.encode("utf-8")
    import  hashlib
    shahash= hashlib.md5(bytestring)  ##using md5 hash
    print(type(shahash))

    hash_bytes = shahash.digest()
    print(hash_bytes, len(hash_bytes))  # Output: b'\x04\x1a\xdd\xcd...\x93\x1b\xcd'

    hash_hex = shahash.hexdigest()
    print(hash_hex)

    import pyAesCrypt
    # custom encryption/decryption buffer size (default is 64KB)
    bufferSize = 128 * 1024
    password = str(hash_hex)
    # encrypt
    pyAesCrypt.encryptFile("D:\\vce\\media\\"+fname2+filetobeuploaded.name, "D:\\vce\\media\\"+fname2+"data.txt.aes", password, bufferSize)
    d = GroupDocument()
    d.date = datetime.now()
    d.file = "/media/" + fname2 + "data.txt.aes"
    d.originalfilename = filetobeuploaded.name
    d.USER = User.objects.get(LOGIN_id= request.session['lid'])
    d.GROUP_id=grpid
    d.save()
    from py_essentials import hashing as hs
    filehash = hs.fileChecksum("D:\\vce\\media\\"+fname2+"data.txt.aes", "sha256")
    message = filehash.encode('utf-16')
    print(message, "Hello Likhil")
    print("D:\\vce\\media\\"+fname2+"data.txt.aes", "Hello Likhil")
    #####hashing filehash with ecc
    allgroupmembers=Grpmember.objects.filter(GRP_id=grpid)
    for a in allgroupmembers:
        from ecdsa import SigningKey, VerifyingKey, NIST256p
        from hashlib import sha256
        # Hexadecimal strings of the private key and public key (replace with actual values from generate_keys.py)
        private_key_hex = a.privatekey
        public_key_hex =a.publickey
        # Convert the hexadecimal strings back to bytes
        private_key_bytes = bytes.fromhex(private_key_hex)
        public_key_bytes = bytes.fromhex(public_key_hex)
        # Reconstruct the SigningKey (private key) and VerifyingKey (public key) from bytes
        sk = SigningKey.from_string(private_key_bytes, curve=NIST256p, hashfunc=sha256)
        vk = VerifyingKey.from_string(public_key_bytes, curve=NIST256p, hashfunc=sha256)
        # Message to be signed





        # Sign the message
        signature = sk.sign(message)

        # Convert the signature to hexadecimal
        signature_hex = signature.hex()

        membhash=GroupDocumentHash()
        membhash.GROUPDOCUMENT= d
        membhash.hashvalue=signature_hex
        membhash.USER=a.USER
        membhash.save()

    return  HttpResponse("<script>alert('Document uploaded successfully');window.location='/myapp/group_fileupload/'</script>")



def group_view_files(request,id):
    data=GroupDocument.objects.filter(GROUP_id=id)
    return  render(request,"user/view_grp_files.html",{'data':data})







def group_download_files(request,fileid,grpid):

    request.session["grpid"]=grpid
    # verify_signature.py

    return render(request,"user/groupdownloadfile.html",{'id':fileid})

def group_download_filepost(request):
    image= request.FILES["file"]
    id= request.POST["id"]
    pubkey= request.POST["pubkey"]

    import  cv2
    fs=FileSystemStorage()
    from datetime import  datetime

    fname= datetime.now().strftime("%y%m%d%H%M%S")+".bmp"

    fs.save(fname,image)
    img= cv2.imread("D:\\vce\\media\\"+fname)

    b,g,r= cv2.split(img)

    w=img.shape[0]
    h=img.shape[1]

    k=""


    for y in range(0,w):
        for x in range(0,h):
            d= r[y,x]
            d= d& 1
            k= k+ str(d)

    bytestring= k.encode("utf-8")
    import  hashlib
    shahash= hashlib.md5(bytestring)
    print(type(shahash))

    hash_bytes = shahash.digest()
    print(hash_bytes, len(hash_bytes))  # Output: b'\x04\x1a\xdd\xcd...\x93\x1b\xcd'

    hash_hex = shahash.hexdigest()
    print(hash_hex)

    import pyAesCrypt
    # custom encryption/decryption buffer size (default is 64KB)
    bufferSize = 128 * 1024
    password =str(hash_hex)
    # encrypt

    d=GroupDocument.objects.get(id=id)
    fname2= d.file

    fname2= fname2.replace("/media/","")


    originalfilename= "D:\\vce\\media\\"+fname2

    from ecdsa import VerifyingKey, NIST256p
    from hashlib import sha256
    from ecdsa import BadSignatureError

    # Hexadecimal strings of the private key, public key, and signature (you can replace these with the actual values)

    grpdocumentobj=GroupDocument.objects.get(id=id).id

    grpmemberobj=Grpmember.objects.get(GRP_id=request.session["grpid"],USER__LOGIN_id= request.session['lid'])
    private_key_hex = grpmemberobj.privatekey
    public_key_hex = grpmemberobj.publickey
    signature_hex = GroupDocumentHash.objects.get(GROUPDOCUMENT=grpdocumentobj,USER__LOGIN_id= request.session["lid"]).hashvalue

    from py_essentials import hashing as hs
    filehash = hs.fileChecksum(originalfilename, "sha256")
    # Message to verify
    message = filehash.encode('utf-16')

    print(originalfilename,"Hello Likhil")
    print(message,"Hello Likhil")

    # Convert hexadecimal strings back to bytes
    private_key = bytes.fromhex(private_key_hex)
    public_key = bytes.fromhex(public_key_hex)
    signature = bytes.fromhex(signature_hex)

    # Reconstruct the verifying key from the public key
    vk = VerifyingKey.from_string(public_key, curve=NIST256p, hashfunc=sha256)

    # Verify the signature
    try:
        vk.verify(signature, message)
        pyAesCrypt.decryptFile(originalfilename, "D:\\vce\\media\\" + d.originalfilename, password, bufferSize)
        return HttpResponse("<a  href='/media/" + d.originalfilename + "' download>Download</a>")
    except BadSignatureError as a:

        print(a)

        return HttpResponse("<script>alert('Singature verification failed');window.location='/myapp/user_view_groups/'</script>")


def user_view_sentfiles(request):
    res=Document.objects.filter(FROM_USER__LOGIN_id= request.session['lid'])
    return render(request,"user/view_files.html",{'data': res})


def user_view_sentfiles_search(request):
    fd = request.POST['fd']
    td = request.POST['td']

    res=Document.objects.filter(FROM_USER__LOGIN_id= request.session['lid'],date__range=[fd,td])
    return render(request,"user/view_files.html",{'data': res})



def user_download_file(request,id):
    return render(request,"user/downloadfile.html",{'id':id})


def userdownloadpost(request):

    image= request.FILES["file"]
    id= request.POST["id"]

    import  cv2
    fs=FileSystemStorage()
    from datetime import  datetime

    fname= datetime.now().strftime("%y%m%d%H%M%S")+".bmp"
    fname2= datetime.now().strftime("%y%m%d%H%M%S")

    fs.save(fname,image)
    img= cv2.imread("D:\\vce\\media\\"+fname)

    b,g,r= cv2.split(img)

    w=img.shape[0]
    h=img.shape[1]

    k=""


    for y in range(0,w):
        for x in range(0,h):
            d= r[y,x]
            d= d& 1
            k= k+ str(d)

    bytestring= k.encode("utf-8")
    import  hashlib
    shahash= hashlib.md5(bytestring)
    print(type(shahash))

    hash_bytes = shahash.digest()
    print(hash_bytes, len(hash_bytes))  # Output: b'\x04\x1a\xdd\xcd...\x93\x1b\xcd'

    hash_hex = shahash.hexdigest()
    print(hash_hex)

    import pyAesCrypt
    # custom encryption/decryption buffer size (default is 64KB)
    bufferSize = 128 * 1024
    password =str(hash_hex)
    # encrypt

    d=Document.objects.get(id=id)
    fname= d.file

    fname= fname.replace("/media/","")


    originalfilename= "D:\\vce\\media\\"+fname

    pyAesCrypt.decryptFile(originalfilename,"D:\\vce\\media\\"+d.originalfilename , password, bufferSize)


    return  HttpResponse("<a  href='/media/"+d.originalfilename+"' download>Download</a>")

##################volanteer chat with user



def user_view_inbox(request):
    res=Document.objects.filter(TO_USER__LOGIN_id= request.session['lid'])
    return render(request,"user/view_inbox.html",{'data': res})



def user_add_group(request):


    if request.method=="POST":
        grpname= request.POST["textfield"]
        file= request.FILES["file"]

        from datetime import  datetime
        filename= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"

        fs=FileSystemStorage()
        fs.save(filename,file)




        grp=Grp()
        grp.grpname= grpname
        grp.USER= User.objects.get(LOGIN_id=request.session['lid'])
        grp.imagefile= fs.url(filename)
        grp.save()

        from ecdsa import SigningKey, NIST256p
        from hashlib import sha256

        # Generate a private key (Signing Key) and its corresponding public key (Verifying Key)
        sk = SigningKey.generate(curve=NIST256p, hashfunc=sha256)
        vk = sk.get_verifying_key()

        # Convert the keys to hexadecimal strings
        private_key_hex1 = sk.to_string().hex()
        public_key_hex1 = vk.to_string().hex()

        # Output the keys as hexadecimal strings
        print("Private Key (Hex):", private_key_hex1)
        print("Public Key (Hex):", public_key_hex1)

        grpm=Grpmember()
        grpm.GRP= grp
        grpm.privatekey=private_key_hex1
        grpm.publickey=public_key_hex1

        mailsending(receiver_email=User.objects.get(LOGIN_id= request.session['lid']).email,subject="Your keys for "+grp.grpname,body= private_key_hex1 +","+public_key_hex1)

        grpm.USER= User.objects.get(LOGIN_id= request.session['lid'])
        grpm.save()


        return HttpResponse("<script>alert('Group added successfully');window.location='/myapp/user_add_group/'</script>")


    return  render(request,"user/add_group.html")




def user_view_groups(request):
    data = Grpmember.objects.filter(USER__LOGIN_id=request.session['lid'])

    if request.method=="POST":
        t=request.POST["t"]
        data = Grpmember.objects.filter(USER__LOGIN_id=request.session['lid'],GRP__grpname__icontains=t)


    li=[]
    for i in data:
        a="No"
        if i.GRP.USER.LOGIN.id== request.session['lid']:
            a="Yes"
        li.append(
            {
                'id':i.GRP.id,
                'grpname':i.GRP.grpname,
                'mecreated': a
            }
        )
    return render(request,"user/view_grps.html",{'data':li})



def user_search_view_members(request,grpid):

    request.session["grpid"]=grpid

    uall=User.objects.all().exclude(LOGIN_id= request.session['lid'])


    li=[]


    for i in uall:
        if not Grpmember.objects.filter(GRP_id=grpid,USER=i).exists():
            li.append(
                i
            )

    return  render(request,"user/viewuser.html",{'data':li})


def use_search_view_members(request):

    if request.method=="GET":
        uall = User.objects.all().exclude(LOGIN_id=request.session['lid'])

        li = []

        for i in uall:
            if not Grpmember.objects.filter(GRP_id=request.session["grpid"], USER=i).exists():
                li.append(
                    i
                )

        return render(request, "user/viewuser.html", {'data': li})

    else:
        search= request.POST["search"]
        uall = User.objects.filter(name__icontains=search).exclude(LOGIN_id=request.session['lid'])

        li = []

        for i in uall:
            if not Grpmember.objects.filter(GRP_id=request.session["grpid"], USER=i).exists():
                li.append(
                    i
                )

        return render(request, "user/viewuser.html", {'data': li})



def addtogrp(request,uid):
    from ecdsa import SigningKey, NIST256p
    from hashlib import sha256

    # Generate a private key (Signing Key) and its corresponding public key (Verifying Key)
    sk = SigningKey.generate(curve=NIST256p, hashfunc=sha256)
    vk = sk.get_verifying_key()

    # Convert the keys to hexadecimal strings
    private_key_hex1 = sk.to_string().hex()
    public_key_hex1 = vk.to_string().hex()

    # Output the keys as hexadecimal strings
    print("Private Key (Hex):", private_key_hex1)
    print("Public Key (Hex):", public_key_hex1)

    Grpmemberobj=Grpmember()
    Grpmemberobj.GRP_id=request.session["grpid"]
    Grpmemberobj.USER_id=uid
    Grpmemberobj.privatekey=private_key_hex1
    Grpmemberobj.publickey=public_key_hex1
    Grpmemberobj.save()

    mailsending(receiver_email=User.objects.get(id=uid).email,
                subject="Your keys for " + Grp.objects.get(id=request.session["grpid"]).grpname, body=private_key_hex1 + "," + public_key_hex1)

    return HttpResponse(
        "<script>alert('Group Added Successfully');window.location='/myapp/use_search_view_members/'</script>"
    )

def user_view_grpmembers(request,id):
    request.session["id"]=id
    data=Grpmember.objects.filter(GRP_id=id)
    request.session["gid"]=id
    return render(request,"user/viewgrpmembers.html",{'data':data})





def user_view_grpmembers_post(request):
    search= request.POST["search"]

    data = Grpmember.objects.filter(GRP_id=request.session["gid"],USER__name__icontains=search)
    # request.session["gid"] = id

    return render(request, "user/viewgrpmembers.html", {'data': data})






def user_view_grpmembers_search(request):
    search= request.POST["search"]
    data=Grpmember.objects.filter(GRP_id=request.session["gid"],USER__name__icontains=search)
    return render(request,"user/viewgrpmembers.html",{'data':data})

def deletegroup(request,gid):
    Grpmember.objects.filter(GRP_id=gid).delete()
    Grp.objects.filter(id=gid)
    return HttpResponse("<script>alert('Group deleted successfully');window.location='/myapp/user_view_groups/'</script>")
