from django.shortcuts import render, redirect, get_object_or_404
from .forms import CpppForm, GemForm, OfflineForm
from .models import Cppp, Gem, Offline
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def adminMIS(request):
    return render(request, 'MIS/adminMIS.html')


@login_required(login_url='/')
def procurement(request):
    return render(request, 'MIS/procurement/procurement.html')


@login_required(login_url='/')
def cppp(request):
    return render(request, 'MIS/procurement/cppp/cppp.html')


@login_required(login_url='/')
def cpppUpdate(request):
    context = {'form': CpppForm}
    return render(request, 'MIS/procurement/cppp/cpppUpdate.html', context)


@login_required(login_url='/')
def gem(request):
    return render(request, 'MIS/procurement/gem/gem.html')


@login_required(login_url='/')
def gemUpdate(request):
    context = {'form': GemForm}
    return render(request, 'MIS/procurement/gem/gemUpdate.html', context)


@login_required(login_url='/')
def offline(request):
    return render(request, 'MIS/procurement/offline/offline.html')


@login_required(login_url='/')
def offlineUpdate(request):
    context = {'form': OfflineForm}
    return render(request, 'MIS/procurement/offline/offlineUpdate.html', context)


@login_required(login_url='/')
def addCppp(request):
    if request.method == 'POST':
        form = CpppForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.usern = request.user
            task.save()
            return redirect('cppp')

    else:
        form = CpppForm()

    return render(request, 'MIS/procurement/cppp/cpppUpdate.html', {'form': CpppForm})


@login_required(login_url='/')
def addGem(request):
    if request.method == 'POST':
        form = GemForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.usern = request.user
            task.save()
            return redirect('gem')

    else:
        form = GemForm()

    return render(request, 'MIS/procurement/gem/gemUpdate.html', {'form': GemForm})


@login_required(login_url='/')
def addOffline(request):
    if request.method == 'POST':
        form = OfflineForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.usern = request.user
            task.save()
            return redirect('offline')

    else:
        form = OfflineForm()

    return render(request, 'MIS/procurement/offline/offlineUpdate.html', {'form': OfflineForm})


@login_required(login_url='/')
def cpppStatus(request):
    cpppEntries = Cppp.objects.all()
    return render(request, 'MIS/procurement/cppp/cpppStatus.html', {'cpppEntries': cpppEntries})


@login_required(login_url='/')
def cpppDetail(request, pk):
    entry = get_object_or_404(Cppp, pk=pk)
    return render(request, 'MIS/procurement/cppp/cpppDetail.html', {'entry': entry})


@login_required(login_url='/')
def gemStatus(request):
    gemEntries = Gem.objects.all()
    return render(request, 'MIS/procurement/gem/gemStatus.html', {'gemEntries': gemEntries})


@login_required(login_url='/')
def gemDetail(request, pk):
    entry = get_object_or_404(Gem, pk=pk)
    return render(request, 'MIS/procurement/gem/gemDetail.html', {'entry': entry})


@login_required(login_url='/')
def offlineStatus(request):
    offlineEntries = Offline.objects.all()
    return render(request, 'MIS/procurement/offline/offlineStatus.html', {'offlineEntries': offlineEntries})


@login_required(login_url='/')
def offlineDetail(request, pk):
    entry = get_object_or_404(Offline, pk=pk)
    return render (request, 'MIS/procurement/offline/offlineDetail.html', {'entry': entry})
