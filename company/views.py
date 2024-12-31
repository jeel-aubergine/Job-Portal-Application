from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company

# Create your views here.
@login_required
def register_company(request):

    """

    View to register the company of the user.

    :param request: The Http request object.

    :return: render the template for company registration.

    """

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')

        # check if user have already registered for the company
        if Company.objects.filter(user=request.user).exists():
            return render(request, 'company/register.html', {'error': 'You have already registered a company.'})

        # create the company object
        company = Company.objects.create(
            user=request.user,
            name=name,
            address=address,
            contact_number=contact_number
        )

        # return to the dashboard page
        return redirect('company_dashboard')

    return render(request, 'company/register.html')

@login_required
def company_dashboard(request):

    """

    View to display the details of the company.

    :param request: The Http request object.

    :return: render the template to display the details of the company.

    """

    # get the company of current user
    company = Company.objects.filter(user=request.user).first()

    # if not registered, redirect them to register page
    if not company:
        return redirect('register_company')

    return render(request, 'company/dashboard.html', {'company': company})

@login_required
def edit_company(request):

    """

    View to edit the company details.

    :param request: The Http request object.

    :return: render the template to edit the details of the company.
    """

    # get the company of current user
    company = Company.objects.filter(user=request.user).first()

    # if not registered, redirect them to register page
    if not company:
        return redirect('register_company')

    # get the data from the form
    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.address = request.POST.get('address')
        company.contact_number = request.POST.get('contact_number')
        company.save()      # update the changes
        return redirect('company_dashboard')

    return render(request, 'company/edit.html', {'company': company})
