from django.db import models

# Create your models here.

class Customers(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=200)
    cust_email=models.CharField(max_length=200, default='noemail@example.com')
    curr_balance=models.IntegerField()

    def __self__(self):
        return self.cust_name

class Transfers(models.Model):
    sender_id=models.ForeignKey(Customers, on_delete = models.CASCADE, related_name="sender_set", default=1000)
    receiver_id=models.ForeignKey(Customers, on_delete = models.CASCADE, related_name="receiver_set", default = 1000)
    sender_name=models.CharField(max_length=200, default="INVALID")
    receiver_name=models.CharField(max_length = 200)
    date_of_transfer=models.DateTimeField(auto_now=False,auto_now_add=False)
    amount=models.IntegerField()
    credit=models.BooleanField(default = True)