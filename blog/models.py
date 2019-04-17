from django.db import models
from django.utils import timezone
import uuid

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
    tags = (
         (0, '3C'),
         (1, '生活'),
         (2, '通訊'),
         (3, '日用'),
         (4, '周邊'),
         (5, '食品'),
         (6, 'N B'),
         (7, '戶外'),
         (8, '數位'),
         (9, '時尚'),
         (10, '家電'),
         (11, '美妝'),
    )

    name = models.CharField(max_length=255,verbose_name='商品名稱')
    class_s = models.IntegerField(choices=tags,verbose_name='分類', null=True)
    price = models.PositiveSmallIntegerField(verbose_name='商品價格')
    place = models.CharField(max_length=255,verbose_name='商品所在地點')
    # photo = models.ImageField(upload_to="/data/images/",verbose_name='商品圖片/狀態') 
    specification= models.CharField(max_length=255,verbose_name='商品規格')
    created = models.DateTimeField(default=timezone.now)
    # category = models.ForeignKey(category,on_delete=models.CASCADE, related_name="commodity",verbose_name='商品類別')
    token = models.UUIDField(db_index=True, default=uuid.uuid4)

    def __str__(self):
        return self.name