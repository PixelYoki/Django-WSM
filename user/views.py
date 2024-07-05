from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from user.models import Profile

# Create your views here.
def login_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        user = request.POST.username
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # 如果前端提交的有效则保存,到数据库中
            form.save()
            login(request, user)
            messages.add_message(request, messages.INFO, f'欢迎{user}')
            return redirect('dashboard-index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'user/login.html',context)


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # 如果前端提交的有效则保存,到数据库中
            user = form.save()
            Profile.objects.create(staff=user)  # 创建并保存空的profile对象
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username}创建成功！')
            login(request, user)
            return redirect('dashboard-index')
        else:
            messages.add_message(request, messages.WARNING, '未注册成功！可以重新再来！')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


def logout_page(request):
    return render(request, 'user/logout.html')


def profile(request):
    return render(request, 'user/profile.html')


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            # 如果前端提交的有效则保存,到数据库中
            user_form.save()
            profile_form.save()

            return redirect('user-profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/profile_update.html', context)
