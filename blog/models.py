from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tag(models.Model):
    contact = models.ForeignKey(Post,on_delete=models.CASCADE)
    name    = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class commodity(models.Model):
    name = models.CharField(max_length=255,verbose_name='商品名稱')
    price = models.PositiveSmallIntegerField(verbose_name='商品價格')
    place = models.CharField(max_length=255,verbose_name='商品所在地點')
    # photo = models.ImageField(upload_to="/data/images/",verbose_name='商品圖片/狀態') 
    specification= models.CharField(max_length=255,verbose_name='商品規格')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    # category = models.ForeignKey(category,on_delete=models.CASCADE, related_name="commodity",verbose_name='商品類別')

    def __str__(self):
        return self.name