from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=255,unique=True)
    description=models.TextField()
    image_url = models.URLField("url",blank=True)
    quantity=models.IntegerField(default=0)
    def sell(self,qt=0):
        if qt>0:
            self.quantity=self.quantity-qt
            #print self.quantity
        else:
            self.quantity=self.quantity-1
            #print self.quantity
        self.save()
