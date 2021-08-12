from django.shortcuts import render,redirect,get_object_or_404
from .forms import PatientForm
from .models import Patient
from django.utils import timezone
# Create your views here.

def index(request):
	return render(request,'index.html')
	
def create(request):
    form = PatientForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'create.html',{"form":form})

    else:
        form = PatientForm()
        return render(request, 'create.html',{"form":form})
        
def detail(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    return render(request,'detail.html',{'patient':patient})

def update(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST or None, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'update.html', {"form": form,"patient":patient})


def delete(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        # messages.info(request, "1 item Deleted !")
        return redirect('list')
    else:
        return render(request,'delete.html', {'patient': patient})
        
        
def patient_list(request):
    patients=Patient.objects.all()
    context={
        "patients":patients,

    }
    return render(request,'list.html',context=context)