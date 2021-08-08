from django.shortcuts import render
from .models import Course, PaidCourse, Jamoamiz, Fikrlar, Manzil

def home_page(request):
    courses = Course.objects.all()
    paid_courses = PaidCourse.objects.all()
    jamoamiz = Jamoamiz.objects.all()
    fikrlar = Fikrlar.objects.all()
    manzil = Manzil.objects.all()
    ctx = {
        "courses": courses,
        "paid_courses": paid_courses,
        "jamoamiz": jamoamiz,
        "fikrlar": fikrlar,
        "manzil": manzil,
    }
    return render(request, "home/index.html", ctx)