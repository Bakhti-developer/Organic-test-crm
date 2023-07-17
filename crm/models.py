from hashlib import blake2s
from django.db import models
from control.models import Course, Account


class Table(models.Model):
    title = models.CharField(max_length=200)
    priority = models.IntegerField(unique=True)

    def __str__(self):
        return f"Table: {self.title}"

    class Meta:
        ordering = ("priority",)



class Lead(models.Model):
    table = models.ForeignKey(Table, on_delete=models.PROTECT, null=True, blank=True)
    plan = models.ForeignKey(Course, on_delete=models.CASCADE)
    operator = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    fio = models.CharField(max_length=200)
    phone = models.IntegerField()
    customer_comment = models.TextField(null=True, blank=True)
    drop = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)
    reminder = models.CharField(max_length=200, null=True, blank=True)
    social = models.CharField(max_length=200)
    droped_table = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.fio}"

    class Meta:
        ordering = ("date_created",)



class LeadComment(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    pin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Auther: {self.account.user.first_name} {self.account.user.last_name}"

    class Meta:
        ordering = ("-pin",)
    






