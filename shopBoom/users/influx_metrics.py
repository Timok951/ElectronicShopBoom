"""import os
from django.contrib.auth import get_user_model
from users.models import Role
from influxdb_client_3 import InfluxDBClient3, Point, WritePrecision
import time
import threading

INFLUXDB_TOKEN = os.environ.get("INFLUXDB_TOKEN")
ORG = "Studing"
BUCKET = "Metrics"  
HOST = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=HOST, token=INFLUXDB_TOKEN, org=ORG)

def write_total_users_metric():
    User = get_user_model()
    total = User.objects.count()
    point = Point("app_total_users") \
        .field("value", total) \
        .time(time.time_ns(), WritePrecision.NS)
    client.write(database=BUCKET, record=point)


def write_total_roles_metric():
    total = Role.objects.count()
    point = Point("app_total_roles") \
        .field("value", total) \
        .time(time.time_ns(), WritePrecision.NS)
    client.write(database=BUCKET, record=point)


def write_avg_bonus_metric():
    User = get_user_model()
    from django.db.models import Avg
    avg_bonus = User.objects.all().aggregate(avg=Avg('bonus'))['avg'] or 0
    point = Point("app_average_bonus") \
        .field("value", avg_bonus) \
        .time(time.time_ns(), WritePrecision.NS)
    client.write(database=BUCKET, record=point)
    update_all_metrics()



def write_login_metric(user_id):

    point = Point("app_logins_total") \
        .tag("user_id", str(user_id)) \
        .field("count", 1) \
        .time(time.time_ns(), WritePrecision.NS)
    client.write(database=BUCKET, record=point)


def update_all_metrics():
    write_total_users_metric()
    write_total_roles_metric()
    write_avg_bonus_metric()

def schedule_metrics(interval_seconds=60):
    update_all_metrics()
    threading.Timer(interval_seconds, schedule_metrics, [interval_seconds]).start()"""
