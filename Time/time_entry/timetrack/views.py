from django.shortcuts import render,redirect

# Create your views here.
from timetrack.models import *
from timetrack.forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# from django.contrib.auth.forms import UserCreationForm

# class ListTaskView(View):
# 	form_class=TaskForm()
# 	model=Task
# 	template_name='list_task.html'
	
# 	def get(self,request):
# 		# form = self.form_class()
# 		form = TaskForm()
# 		context={'form':form}

# 		return render(request,self.template_name,context)
		
# 	def POST(self,request):
# 		queryset = self.objects.order_by('complete','due')
# 		form=self.form_class(request.POST,instance=queryset)
		
# 		if form.is_valid():
# 			form.save()
		
# 		context={'form':form}	

# 		return render(request,self.template_name,context)


def listTask(request):
	queryset = Task.objects.order_by('complete','due')
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		# return redirect('/')
	context = {
		'tasks':queryset,
		'form':form,
		}
	return render(request, 'list_task.html', context)

def updateTask(request, pk):
	queryset = Task.objects.get(id=pk)
	form = UpdateForm(instance=queryset)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'form':form
		}

	return render(request, 'update_task.html', context)    

def deleteTask(request, pk):
	queryset = Task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/')

	context = {
		'item':queryset
		}
	return render(request, 'delete_task.html', context)



def registrationPage(request):
	if request.user.is_authenticated:
		return redirect('task_list')
	else:

		form=CreateUserForm()
		if request.method == 'POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request,'Account is created for '+user)
				return redirect('login')

		context={'form':form}
		return render(request,'register.html',context)


def loginPage(request):
	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('task_list')
		else:
			messages.info(request,'Username or password is incorrect')			

	context={}
	return render(request,'login.html',context)	


def logoutUser(request):
	logout(request)
	return redirect('login')	