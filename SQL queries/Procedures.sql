CREATE OR REPLACE PROCEDURE add_good_cost(
	id_good int
)
AS $$
BEGIN
IF	id_good < 1 THEN
	ROLLBACK;
ELSE
	UPDATE shop_good sg
	SET sg.cost = sg.cost + sg.cost * 0.10
	WHERE sg.id = id_good;
END IF;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE add_good_stock(
	good_id INT,
	good_add INT
)
AS $$
BEGIN
IF good_id < 1 THEN
	ROLLBACK;
ELSE
	UPDATE shop_good
	SET amount = amount + good_add
	WHERE id = good_id;
END IF;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_bad_goods(
	rate FLOAT
)
AS $$
	DELETE FROM shop_good 
	USING 
		shop_rate
	WHERE shop_good.id = shop_rate.good_id
		AND shop_rate.rating = rate
$$
LANGUAGE SQL;


	
