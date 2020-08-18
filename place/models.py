from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from collections import Counter


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     pass


class Place(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='places')
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=50)
    website = models.CharField(null=True, blank=True, max_length=100)
    phone_number = models.CharField(null=True, blank=True, max_length=13)
    image = models.ImageField(null=True, blank=True, upload_to='place/')
    lat = models.FloatField()
    lng = models.FloatField()
    # 추가 부분
    open_at = models.TimeField(null=True, blank=True)
    closed_at = models.TimeField(null=True, blank=True)
    fee = models.CharField(null=True, max_length=50, blank=True)
    weekend = models.CharField(max_length=100, null=True, blank=True)
    hashtag = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_congestion_avg(self):
        # 혼잡도 평가가 없을시
        if not self.congestions.all():
            return 1

        all_congestions = self.congestions.all().order_by('-created_at')[:5]
        value_list = [x.value for x in all_congestions]
        cnt = Counter(value_list)
        cnt_list = cnt.most_common()
        result = cnt_list[0][0]

        return result


class Congestion(TimeStampedModel):
    value = models.IntegerField(validators=[RegexValidator(r'\d{1}')])
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='congestions')
    expiration_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.place.name} - {self.value}'

    def time_since_created(self):
        timesince = (timezone.now()-self.created_at).total_seconds()
        minute = timesince // 60
        hour = timesince // 3600

        if timesince // 60 < 1:
            return f'{int(timesince)}초 전'

        elif minute and minute < 60:
            return f'{int(minute)}분 전'

        else:
            return f'{int(hour)}시간 전'
