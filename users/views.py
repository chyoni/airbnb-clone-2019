from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(View):
    def get(self, request):

        form = forms.LoginForm(initial={"email": "admin@admin.com"})

        return render(request, "users/login.html", {"form": form})

    def post(self, request):

        form = forms.LoginForm(request.POST)

        # form으로 보낸 데이터들이 유효한지 확인을 해야함 즉, 유저가 로그인할 때 아이디와 패스워드가
        # 유효한지 확인을 한다는 얘기임
        # 그래서 form(LoginForm 을 의미)에서 데이터를 확인하는 method가 있음 그게 clean_xxx method임
        # 저기 xxx 는 유효한지 확인할 필드의 이름을 넣으면 됨
        # clean method는 확인을해서 return을 해줌
        # clean method가 return을 하지않으면 해당 필드의 데이터를 지워버림 그래서 return을 해줘야함

        # 결국 결론은 post를 하게되면 저기 form에 가서 데이터를 확인하고 다시 돌려준다는 얘기임
        # 돌려주면 여기서 확인을 함 is_valid로 확인을 하면 당연히 로그인을 시켜주겠지?

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})


def log_out(request):

    logout(request)

    return redirect(reverse("core:home"))
