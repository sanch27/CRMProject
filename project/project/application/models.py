from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	



class Courses(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=255)
    CourseDescription = models.TextField()

    def __str__(self):
        return(f"{self.CourseName}")

class Packages(models.Model):
    PackageID = models.AutoField(primary_key=True)
    PackageName = models.CharField(max_length=255)
    PackageDescription = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return(f"{self.PackageName}")

class PackageOptions(models.Model):
    OptionID = models.AutoField(primary_key=True)
    PackageID = models.ForeignKey(Packages, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    


class Subscriptions(models.Model):
    SubscriptionID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PackageID = models.ForeignKey(Packages, on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    ExpiryDate = models.DateField()

    def __str__(self):
        return (f"SubscriptionID: {self.SubscriptionID}, UserID: {self.UserID}, PackageID: {self.PackageID}, PaymentDate: {self.PaymentDate}, ExpiryDate: {self.ExpiryDate}")


