from django.db import models
from django.utils.translation import ugettext_lazy as _


class Orders(models.Model):
    """ Model of orders. """
    ORDERS_STATUSES = [
        [-1, _("Error on payment")],
        [0, _("Awaiting payment")],
        [1, _("In process")],
        [2, _("Handed over to the courier")],
        [3, _("Delivered")],
    ]
    user = models.ForeignKey('users.Users', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=ORDERS_STATUSES, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def total_cost(self) -> float:
        offerings = ProductsInOrders.objects.filter(order=self)
        total = 0
        for ofrng in offerings:
            total += ofrng.get_total_cost()
        return total

    def products(self):
        return ProductsInOrders.objects.filter(order=self)


class ProductsInOrders(models.Model):
    """ Model of Products in order. """

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    qty = models.PositiveIntegerField(default=1)
    cost = models.FloatField()

    def get_total_cost(self) -> float:
        return self.cost*self.qty


class Cart(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    # cost = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'product']]
