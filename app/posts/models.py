from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.db.utils import NotSupportedError
from django.utils.translation import gettext_lazy as _
from posts.managers import PostManager
from posts.service import get_weather_data


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name=_("제목"))
    body = models.CharField(max_length=200, verbose_name=_("본문"))
    password = models.CharField(max_length=255, verbose_name=_("비밀번호"))
    objects = PostManager()

    def __str__(self):
        return self.title


class PostWeather(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, verbose_name=_("위치"))
    country = models.CharField(max_length=20, verbose_name=_("국가"))
    lat = models.FloatField(verbose_name=_("위도"))
    lon = models.FloatField(verbose_name=_("경도"))
    tz_id = models.CharField(max_length=20, verbose_name=_("타임존"))
    localtime = models.CharField(max_length=20, verbose_name=_("로컬타임"))
    last_updated = models.CharField(max_length=20, verbose_name=_("최근업데이트"))
    temp_c = models.FloatField(verbose_name=_("섭씨온도"))
    temp_f = models.FloatField(verbose_name=_("화씨온도"))
    is_day = models.IntegerField(verbose_name=_("낮/밤"))
    condition = models.CharField(max_length=20, verbose_name=_("날씨 상태"))
    icon = models.CharField(max_length=255, verbose_name=_("아이콘"))
    code = models.IntegerField(verbose_name=_("코드"))
    wind_mph = models.FloatField(verbose_name=_("바람속도(mph)"))
    wind_kph = models.FloatField(verbose_name=_("바람속도(kph)"))
    wind_degree = models.IntegerField(verbose_name=_("바람방향"))
    wind_dir = models.CharField(max_length=20, verbose_name=_("바람방향"))
    pressure_mb = models.FloatField(verbose_name=_("기압(mb)"))
    pressure_in = models.FloatField(verbose_name=_("기압(in)"))
    precip_mm = models.FloatField(verbose_name=_("강수량(mm)"))
    precip_in = models.FloatField(verbose_name=_("강수량(in)"))
    humidity = models.IntegerField(verbose_name=_("습도"))
    cloud = models.IntegerField(verbose_name=_("구름"))
    feelslike_c = models.FloatField(verbose_name=_("체감온도(섭씨)"))
    feelslike_f = models.FloatField(verbose_name=_("체감온도(화씨)"))
    vis_km = models.FloatField(verbose_name=_("가시거리(km)"))
    vis_miles = models.FloatField(verbose_name=_("가시거리(miles)"))
    uv = models.FloatField(verbose_name=_("자외선지수"))
    gust_mph = models.FloatField(verbose_name=_("최대풍속(mph)"))
    gust_kph = models.FloatField(verbose_name=_("최대풍속(kph)"))


@receiver(post_save, sender=Post)
def create_post_weather(sender, instance, **kwargs):
    weather_data = get_weather_data()
    PostWeather.objects.create(
        post=instance,
        location=weather_data["location"]["name"],
        country=weather_data["location"]["country"],
        lat=weather_data["location"]["lat"],
        lon=weather_data["location"]["lon"],
        tz_id=weather_data["location"]["tz_id"],
        localtime=weather_data["location"]["localtime"],
        last_updated=weather_data["current"]["last_updated"],
        temp_c=weather_data["current"]["temp_c"],
        temp_f=weather_data["current"]["temp_f"],
        is_day=weather_data["current"]["is_day"],
        condition=weather_data["current"]["condition"]["text"],
        icon=weather_data["current"]["condition"]["icon"],
        code=weather_data["current"]["condition"]["code"],
        wind_mph=weather_data["current"]["wind_mph"],
        wind_kph=weather_data["current"]["wind_kph"],
        wind_degree=weather_data["current"]["wind_degree"],
        wind_dir=weather_data["current"]["wind_dir"],
        pressure_mb=weather_data["current"]["pressure_mb"],
        pressure_in=weather_data["current"]["pressure_in"],
        precip_mm=weather_data["current"]["precip_mm"],
        precip_in=weather_data["current"]["precip_in"],
        humidity=weather_data["current"]["humidity"],
        cloud=weather_data["current"]["cloud"],
        feelslike_c=weather_data["current"]["feelslike_c"],
        feelslike_f=weather_data["current"]["feelslike_f"],
        vis_km=weather_data["current"]["vis_km"],
        vis_miles=weather_data["current"]["vis_miles"],
        uv=weather_data["current"]["uv"],
        gust_mph=weather_data["current"]["gust_mph"],
        gust_kph=weather_data["current"]["gust_kph"],
    )


@receiver(pre_save, sender=PostWeather)
def block_change_anything(sender, instance, **kwargs):
    try:
        obj = sender.objects.filter(pk=instance.pk)
        if obj.exists():
            raise NotSupportedError("데이터를 변경할 수 없습니다.")
    except NotSupportedError as e:
        raise e
