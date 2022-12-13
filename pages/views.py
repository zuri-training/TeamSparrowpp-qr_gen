from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import qrcode
from .models import QRModel

def homePage(request):
    return render(request, "pages/landing_page.html")

@login_required(login_url="login")
def dashboard(request):

    return render(request, "pages/dashboard.html")    

def generateQRcode(request):

    if request.method == "POST":
        # if "url" in request.POST:
        print(request.POST.get("url"))
            # url = request.POST.get("url")
            # qr = qrcode.make('{}'.format(url))
            # qrc = qrcode.QRCode()
            # # qr.save('static/images/myQR.png')
            # qr_model = QRModel.objects.create(url="{}".format(url))

    return render(request, "pages/dashboard.html")