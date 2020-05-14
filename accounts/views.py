from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    #회원가입 기능 구현
    #정해진 틀에 맞게 타이핑만 하면 됨
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password1"]
            )
            auth.login(request, user)
            #이 부분이 author를 login하는 건데..
            #즉, 이 부분이 없으면 회원가입만 하고 login을 안 하는 것인데 
            #login이 되면! admin 페이지에 들어갔을 때 로그아웃 되어 있는게 보인다
            #즉, 새로운 유저가 생겼으니까 admin에 들어갔을 때 어떤 user인지 모르니까 튕김
            return redirect('read_blog_list')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        #input에 해당하는 값을 변수에 저장한다
        password = request.POST['password1']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('read_blog_list')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
        #없다면 login페이지로 다시 가면서 error 경고문을 띄워라
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('read_blog_list')