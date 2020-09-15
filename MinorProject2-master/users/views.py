from django.conf import settings
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

#utility functions
'''
def hours_vs_date_every_employee():
	qs = Attendance.objects.all()
	diff=[]
	
	for obj in qs:
		ti=obj.time_in
		to=obj.time_out
		hours=((to-ti).total_seconds())/3600
		diff.append(hours)
		
	df = read_frame(qs)
	df['hours']=diff
	figure=plt.figure()
	sns.barplot(data=df,x='date',y='')
	html_graph=mpld3.fig_to_html(fig)


'''







# Create your views here.

@login_required
def register(request):
	if request.user.username!='admin':
		return redirect('not-authorised')
	if request.method=='POST':
		form=CustomUserCreationForm(request.POST)
		# form=UserCreationForm(request.POST)
		if form.is_valid():
			saveit = form.save(commit=False)
			saveit.save()
			# form.save() ###add user to database
			messages.success(request, f'Employee registered successfully!')

			subject="test1"
			message="testm"
			fromMail = settings.EMAIL_HOST_USER
			recipient = [saveit.email, settings.EMAIL_HOST_USER]
			send_mail(subject, message, fromMail, recipient, fail_silently=True)
			return redirect('dashboard')
		


	else:
		form=CustomUserCreationForm()
	return render(request,'users/register.html', {'form' : form})





