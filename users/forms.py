from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # clean_xxx 처럼 특정 필드의 유효검사를 할때는 에러 메세지는 해당 필드에서 나오지만
    # clean method는 필드간 서로 연관성이 있을때 한꺼번에 같이 검사하는 이런 메소드는
    # 해당 에러가 어디서 생기는건지 따로 저렇게 self.add_error(field) 저 field 부분에 알려줘야함

    def clean(self):

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong."))

        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist."))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    # 장고가 위에서부터 하나씩 clean해서 cleaned_data 에 데이터를 넣기때문에
    # 만약 clean_password 에서 password2 를 가져오려한다면 가져오지 못할 것

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Password confirmation does not match.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
