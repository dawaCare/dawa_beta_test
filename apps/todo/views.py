from django.shortcuts import render, redirect
from django.views.generic import View
from apps.outpatients.models import Outpatient, MedicationReminder, AppointmentReminder
from django.contrib.auth.models import User
# Create your views here.

class Todo(View):
    def get(self, request):
        print(request.user.id)
        print(MedicationReminder.objects.all())
        print(AppointmentReminder.objects.all())
        # med_todos = MedicationReminder.objects.get(user=request.user.id)
        # print(med_todos)
        med_todos = MedicationReminder.objects.filter(pcc=request.user.id).order_by('date')
        appt_todos = AppointmentReminder.objects.filter(pcc=request.user.id).order_by('date')
        context = {
            'med_todos' : med_todos,
            'appt_todos' : appt_todos,
        }
        return render(request, 'todo/index.html', context)

class PatientContact(View):
    def post(self, request):
        print (request.POST)
        appt_rem = AppointmentReminder.objects.get(id=request.POST['todoid'])
        print(appt_rem)
        print(appt_rem.appt_date.appt_date)
        appt_rem.contacted_patient = "True"
        print(appt_rem.contacted_patient)
        appt_rem.save()
        return redirect('/')
        # input type checkbox doesnt send input data if false
