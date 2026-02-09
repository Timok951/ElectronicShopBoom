CREATE MATERIALIZED VIEW user_orders AS
(
SELECT 
c.address AS user_adres,
u.email AS user_email,
u.username AS user_username,
uc.phonenumber AS user_phonenumber,
c.date AS cart_date

FROM cart_order c
	JOIN users_user u ON u.id = c.user_id
	JOIN users_usercredenetials uc on u.id = uc.user_id
);

CREATE MATERIALIZED VIEW  good_icome AS(
SELECT 
u.username AS users_income, 
c.date AS date_income,
(g.cost * ordi.amount)::Float AS oders_income
	FROM cart_order c
	JOIN users_user u ON u.id = c.user_id
	JOIN cart_orderitem ordi ON ordi.order_id = c.id
	JOIN shop_good g ON g.id = ordi.good_id
ORDER BY c.date
);


CREATE MATERIALIZED VIEW dangerous_goods AS(
SELECT 
	g.name AS good_name,
	g.amount AS good_amount,
	g.id
FROM shop_good g
WHERE g.amount <50
);

CREATE MATERIALIZED VIEW orders_report AS(
SELECT
	o.id AS order_id,
	o.date AS order_date ,
	u.username AS username,
	g.name AS product_name,
	oi.price_at_purchase AS price_at_purchase,
	(oi.amount * oi.price_at_purchase) AS total
FROM cart_order o
JOIN cart_orderitem oi ON oi.order_id = o.id
JOIN shop_good g ON g.id = oi.good_id
JOIN users_user u ON u.id = o.user_id
);


