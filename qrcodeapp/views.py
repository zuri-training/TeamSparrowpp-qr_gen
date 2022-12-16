from django.shortcuts import render
from .models import QRModel
import qrcode.image.svg
from io import BytesIO
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def URL(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        QRModel.objects.create(url=request.POST.get("qr_text",""), user=request.user)
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "URL.html", context=context)

