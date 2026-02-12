from django.db import migrations


USER_ORDERS_VIEW = """
DROP MATERIALIZED VIEW IF EXISTS user_orders;
DROP VIEW IF EXISTS user_orders;
DROP TABLE IF EXISTS user_orders;
CREATE OR REPLACE VIEW user_orders AS
SELECT 
    c.address AS user_adres,
    u.email AS user_email,
    u.username AS user_username,
    uc.phonenumber AS user_phonenumber,
    c.date AS cart_date
FROM cart_order c
JOIN users_user u ON u.id = c.user_id
LEFT JOIN users_usercredenetials uc ON u.id = uc.user_id;
"""

GOOD_INCOME_VIEW = """
DROP MATERIALIZED VIEW IF EXISTS good_income;
DROP VIEW IF EXISTS good_income;
DROP TABLE IF EXISTS good_income;
CREATE OR REPLACE VIEW good_income AS
SELECT
    ROW_NUMBER() OVER () AS id,
    u.username AS users_income,
    c.date AS date_income,
    CAST(g.cost * ordi.amount AS DOUBLE PRECISION) AS orders_income
FROM cart_order c
JOIN users_user u ON u.id = c.user_id
JOIN cart_orderitem ordi ON ordi.order_id = c.id
JOIN shop_good g ON g.id = ordi.good_id;
"""

DANGEROUS_GOODS_VIEW = """
DROP MATERIALIZED VIEW IF EXISTS dangerous_goods;
DROP VIEW IF EXISTS dangerous_goods;
DROP TABLE IF EXISTS dangerous_goods;
CREATE OR REPLACE VIEW dangerous_goods AS
SELECT 
    g.id,
    g.name AS good_name,
    g.amount AS good_amount
FROM shop_good g
WHERE g.amount < 50;
"""

ORDERS_REPORT_VIEW = """
DROP MATERIALIZED VIEW IF EXISTS orders_report;
DROP VIEW IF EXISTS orders_report;
DROP TABLE IF EXISTS orders_report;
CREATE OR REPLACE VIEW orders_report AS
SELECT
    o.id AS order_id,
    o.date AS order_date,
    u.username AS username,
    g.name AS product_name,
    oi.price_at_purchase AS price_at_purchase,
    oi.amount * oi.price_at_purchase AS total
FROM cart_order o
JOIN cart_orderitem oi ON oi.order_id = o.id
JOIN shop_good g ON g.id = oi.good_id
JOIN users_user u ON u.id = o.user_id;
"""


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0002_create_views"),
    ]

    operations = [
        migrations.RunSQL(
            sql=USER_ORDERS_VIEW,
            reverse_sql="DROP MATERIALIZED VIEW IF EXISTS user_orders; DROP VIEW IF EXISTS user_orders;",
        ),
        migrations.RunSQL(
            sql=GOOD_INCOME_VIEW,
            reverse_sql="DROP MATERIALIZED VIEW IF EXISTS good_income; DROP VIEW IF EXISTS good_income;",
        ),
        migrations.RunSQL(
            sql=DANGEROUS_GOODS_VIEW,
            reverse_sql="DROP MATERIALIZED VIEW IF EXISTS dangerous_goods; DROP VIEW IF EXISTS dangerous_goods;",
        ),
        migrations.RunSQL(
            sql=ORDERS_REPORT_VIEW,
            reverse_sql="DROP MATERIALIZED VIEW IF EXISTS orders_report; DROP VIEW IF EXISTS orders_report;",
        ),
    ]
