from django.db import models

class Transaction(models.Model):
    wallet = models.CharField(verbose_name='wallet', max_length=2048)
    rdw = models.FloatField(verbose_name='rdw')
    class Meta:
        verbose_name = "transaction"
        verbose_name_plural = "transactions"
    def __str__(self):
        return self.wallet + " - " + str(self.rdw)