from django.shortcuts import render,get_object_or_404
from.models import Work,Work_details,Art,LoveAndWar,Itswhatido,Exhibition,Awards,Bio

def home(request):
    work=Work.objects.all()
    works = Work.objects.prefetch_related('details').all()
    return render(request,'home.html', {"work": work ,"works":works})
def bio(request):
    work=Work.objects.all()
    bio = Bio.objects.filter(is_active=True).first()
    return render(request,'bio.html',{"work": work,"bio":bio})
def love(request):
    work=Work.objects.all()
    love_and_war = LoveAndWar.objects.filter(is_active=True).first()
    return render(request,'love_and_war.html',{"work": work,'love_and_war': love_and_war})
def thirdpage(request):
    work=Work.objects.all()
    itswhatido = Itswhatido.objects.filter(is_active=True).first()
    return render(request,'its-what-i-do.html',{"work": work,'itswhatido': itswhatido})
def awards(request):
    work=Work.objects.all()
    awards = Awards.objects.filter(is_active=True).first()
    return render(request,'awards.html',{"work": work,"awards":awards})
def exhibition(request):
    work=Work.objects.all()
    exhibition = Exhibition.objects.filter(is_active=True).first()
    return render(request,'Exhibition.html',{"work": work,"Exhibition":exhibition})

def contact(request):
    work=Work.objects.all()

    return render(request,'contact.html',{"work": work})

def art(request):
    work=Work.objects.all()
    images=Art.objects.all()
    return render(request,'fine-art-prints.html',{"work": work,"images":images})


def state(request, pk):
    selected_work = get_object_or_404(Work, pk=pk)
    images = Work_details.objects.filter(work=selected_work)
    all_works = Work.objects.all()
    return render(request, 'state.html', {
        "selected_work": selected_work,
        "images": images,
        "all_works": all_works
    })