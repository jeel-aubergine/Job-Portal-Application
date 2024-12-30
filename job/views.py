from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Job
from company.models import Company

# Create your views here.
@login_required
def create_job(request):

    """

    View to create a job posting.

    :param request: The Http request object.

    :return: render the template to create a job posting.

    """

    # get the company of current user
    company = Company.objects.filter(user=request.user).first()
    if not company:
        return redirect('register_company')

    # get the data from the form
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary_range = request.POST.get('salary_range')
        tags = request.POST.get('tags')

        # create a job object
        Job.objects.create(
            company=company,
            title=title,
            description=description,
            location=location,
            salary_range=salary_range,
            tags=tags
        )
        return redirect('list_jobs')        # redirect to job listing template

    return render(request, 'job/create.html')

@login_required
def list_jobs(request):

    """

    View to display the list of jobs created.

    :param request: The Http request object.

    :return: render the template to list out created jobs, with pagination.

    """

    # get the company of current user
    company = Company.objects.filter(user=request.user).first()
    if not company:
        return redirect('register_company')

    # get the all jobs of current company
    jobs = Job.objects.filter(company=company)

    # create paginator object to display 2 jobs per page
    paginator = Paginator(jobs, 2)

    # get the current page number
    page_number = request.GET.get('page')

    # get the job for current page number
    job_page = paginator.get_page(page_number)

    # get the total number of pages
    total_pages = job_page.paginator.num_pages

    return render(request, 'job/list.html', {'jobs': job_page, 'total_pages': list(range(1, total_pages + 1))})

@login_required
def edit_job(request, job_id):

    """

    View to edit a job posting.

    :param request: The Http request object.

    :param job_id: ID of the requested job to edit.

    :return: Render the template form to edit the requested job.

    """

    # get the requested job
    job = get_object_or_404(Job, id=job_id, company__user=request.user)

    # get the data from the form
    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.location = request.POST.get('location')
        job.salary_range = request.POST.get('salary_range')
        job.tags = request.POST.get('tags')
        job.save()
        return redirect('list_jobs')

    return render(request, 'job/edit.html', {'job': job})

@login_required
def delete_job(request, job_id):

    """

    View to delete a job posting.

    :param request: The Http request object.

    :param job_id: ID of the request job to be deleted.

    :return: Render the confirmation template to delete the requested job.

    """

    # get the requested job.
    job = get_object_or_404(Job, id=job_id, company__user=request.user)

    if request.method == 'POST':
        job.delete()
        return redirect('list_jobs')

    return render(request, 'job/delete.html', {'job': job})
