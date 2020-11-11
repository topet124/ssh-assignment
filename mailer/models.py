from __future__ import unicode_literals
from django.db import models
# from django.utils.encoding import python_2_unicode_compatible


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)

    def get_order_count(self):

        orders = self.orders.count()
        return orders

    def get_order_sum(self):

        total_sum = sum([a.total for a in Order.objects.filter(company=self)])
        return total_sum


    def __str__(self):
        return self.name


class Contact(models.Model):
    company = models.ForeignKey(
        Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()

    def get_order_count(self):

        orders = self.orders.count()

        return orders


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# @python_2_unicode_compatible
class Order(models.Model):
    order_number = models.CharField(max_length=150)
    company = models.ForeignKey(Company, related_name="orders")
    contact = models.ForeignKey(Contact, related_name="orders")
    total = models.DecimalField(max_digits=18, decimal_places=9)
    order_date = models.DateTimeField(null=True, blank=True)
    # for internal use only
    added_date = models.DateTimeField(auto_now_add=True)
    # for internal use only
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.order_number
