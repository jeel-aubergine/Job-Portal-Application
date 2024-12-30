from django.db import models
from company.models import Company

# Create your models here.
class Job(models.Model):

    """

    Model to store the data about the jobs.

    :attributes:
        - company: id of the company that created the job.
        - title: title of the job.
        - description: description of the job.
        - location: location of the job.
        - salary_range: salary_range of the job.
        - tag: tag of the job.

    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=50)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
