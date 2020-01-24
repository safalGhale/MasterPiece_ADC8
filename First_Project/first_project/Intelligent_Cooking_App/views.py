from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden
from django.template import Template,Context
from .models import Recipes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_recipes_page(request):
    return render(request,'recipes/recipes.html')

def view_recipes_lists(request):
    list_of_recipes= Recipes.objects.all()
    # print(list_of_recipes)
    context_variable = {
        'Recipes':'list_of_recipes'
    }
    return render(request,'recipes/recipes.html',context_variable)

def view_recipes_form(request):
    return render(request,'recipes/recipesform.html')

# create
def view_recipesdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_Username = request.POST['recipes_Username']
        print(type(get_Username))
        get_Dishname = request.POST['recipes_Dishname']
        print(type(get_Dishname))
        get_Recipe = request.POST['recipes_Recipe']
        print(type(get_Recipe))
        recipes_obj = Recipes(Username=get_Username,Dishname=get_Dishname,Recipe=get_Recipe)
        recipes_obj.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")

def view_recipesdata_updateform(request,ID):
    print(ID)
    recipes_obj = Recipes.objects.get(id=ID)
    print(recipes_obj)
    context_varible = {
        'recipes':'recipes_obj'
    }
    return render(request,'recipes/recipesupdateform.html',context_varible)

def view_update_form_data_in_db(request,ID):
    Recipes_obj = Recipes.objects.get(id=ID)
    print(recipes_obj)
    fligh_form_data = request.POST
    print(fligh_form_data)
    recipes_obj.Username = request.POST['recipes_Username']
    recipes_obj.Dishname =request.POST['recipes_Dishname']
    recipes_obj.Recipe = request.POST['recipes_Recipe']
    recipes_obj.save()
    return HttpResponse("Record Updated!!")

def view_register_user(request):
    if request.method =="GET":
        return render(request,'recipes/registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful")


def view_authenticate_user(request):
    if request.method =="GET":
        return render (request,'recipes/registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"recipes/registration/page.html")
        else:
            return redirect("login")

def view_logout(request):
    if (not request.user.is_authenticated):
        return HttpResponseForbidden('Please login to logout!')
    logout(request)
    return redirect('login')   
