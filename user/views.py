from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def signup(request):

    """

    View to create user account (sign up).

    :param request: The Http request object.

    :return: Render the template form to sign up the user.

    """

    # get the data from the form
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # check if password and confirm_password match
        if password1 != password2:
            return HttpResponse("Passwords do not match!")

        try:

            # check if user already exists
            user = User.objects.filter(email=email).first()
            if user:
                return HttpResponse("User already exists!")

            # create user object
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()     # save the user

            # authenticate user, create the session
            login(request, user)

            # redirect to home page
            return redirect('home')

        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, 'user/signup.html')

def signin(request):
    """

    View to sign in a user.

    :param request: The Http request object.

    :return: Render the template form to sign in the user.

    """

    # get the data from the form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # authenticate the user, create a session
        user = authenticate(request, username=username, password=password)
        print(user)

        # if user s founded, redirect them to company dashboard page.
        if user is not None:
            login(request, user)
            return redirect('company_dashboard')

        else:
            return HttpResponse("Invalid credentials!")

    return render(request, 'user/signin.html')


def signout(request):

    """

    View to sign out a user.

    :param request: The Http request object.

    :return: Render the template for sign out confirmation.

    """

    # log out the user, delete the session
    if request.method == 'POST':
        logout(request)
        return redirect('signin')

    return render(request, 'user/signout.html')
