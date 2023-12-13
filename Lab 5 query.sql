---------------
--Триггер №1--
--------------
CREATE OR REPLACE FUNCTION order_insert_trigger_fnc() RETURNS TRIGGER AS $$
DECLARE action_val INT;
BEGIN IF NEW."sum" >= 0 THEN action_val := 1;
-- Прибыль
ELSE action_val := 0;
-- Убыток
END IF;
INSERT INTO "finance" ("action", "sum", "time")
VALUES (action_val, NEW."sum", NEW."time");
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE TRIGGER order_insert_trigger
AFTER
INSERT ON "order" FOR EACH ROW EXECUTE FUNCTION order_insert_trigger_fnc();
-----------------------------Инсерт для проверки 
INSERT INTO "order" (
        "sum",
        "user_id",
        "product_id",
        "time",
        "status_id"
    )
VALUES (20000, 5, 33, '2023-11-16 10:00:00', 1);
----------------
--Триггер №2--
--------------
CREATE OR REPLACE FUNCTION product_status_update_trigger_fnc() RETURNS TRIGGER AS $$ BEGIN
UPDATE "order"
SET "status_id" = CASE
        WHEN NEW."status_id" = 1 THEN 1 -- Заказ выполнен
        ELSE 2 -- Заказ в процессе
    END
WHERE "product_id" = NEW."id";
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE TRIGGER product_status_update_trigger
AFTER
UPDATE ON "product" FOR EACH ROW
    WHEN (OLD."status_id" <> NEW."status_id") EXECUTE FUNCTION product_status_update_trigger_fnc();
---------------------------------Инсерт для проверки 
INSERT INTO "order" (
        "sum",
        "user_id",
        "product_id",
        "time",
        "status_id"
    )
VALUES (100, 1, 34, CURRENT_TIMESTAMP, 2);
---------------------------------Апдейт для проверки
UPDATE "product"
SET "status_id" = 1 -- Изменяем статус продукта на "в наличии"
WHERE "id" = 34;
----------------
--Триггер №3----
----------------
CREATE OR REPLACE FUNCTION log_insert_trigger_fnc() RETURNS TRIGGER AS $$ BEGIN IF TG_OP = 'INSERT' THEN
INSERT INTO "log" ("action", "id_user")
SELECT 1,
    NEW."id"
FROM "user"
WHERE "id" = NEW."id"
END IF;
RETURN NULL;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE TRIGGER user_login_logout_trigger
AFTER
INSERT ON "user" FOR EACH ROW EXECUTE FUNCTION log_insert_trigger_fnc();
--------------Вставка для проверки
INSERT INTO "user" (
        "login",
        "password",
        "phone",
        "email",
        "is_staff",
        "is_superuser"
    )
VALUES (
        'testuser',
        'password123',
        '1234567890',
        'testuser@example.com',
        false,
        false
    );
--------------Удаление для проверки
DELETE FROM "user"
WHERE "id" = 7;
--айишник ищменится
-------------------------------------------------------------------
--------------------------ПРОЦЕДУРЫ--------------------------------
-------------------------------------------------------------------
------№1-----------------------
CREATE PROCEDURE create_user(
    p_login varchar(30),
    p_password varchar(30),
    p_phone varchar(11),
    p_email varchar,
    p_is_staff bool,
    p_is_superuser bool
) AS $$ BEGIN
INSERT INTO "user" (
        "login",
        "password",
        "phone",
        "email",
        "is_staff",
        "is_superuser"
    )
VALUES (
        p_login,
        p_password,
        p_phone,
        p_email,
        p_is_staff,
        p_is_superuser
    );
END;
$$ LANGUAGE plpgsql;
-----------№2----------------
CREATE PROCEDURE create_order(
    p_sum integer,
    p_user_id integer,
    p_product_id integer,
    p_time timestamp without time zone,
    p_status_id integer
) AS $$ BEGIN
INSERT INTO "order" (
        "sum",
        "user_id",
        "product_id",
        "time",
        "status_id"
    )
VALUES (
        p_sum,
        p_user_id,
        p_product_id,
        p_time,
        p_status_id
    );
END;
$$ LANGUAGE plpgsql;
-------------№3---------------
CREATE PROCEDURE get_order_by_id(
    p_order_id integer,
    OUT p_sum integer,
    OUT p_user_id integer,
    OUT p_product_id integer,
    OUT p_time timestamp without time zone,
    OUT p_status_id integer
) AS $$ BEGIN
SELECT "sum",
    "user_id",
    "product_id",
    "time",
    "status_id" INTO p_sum,
    p_user_id,
    p_product_id,
    p_time,
    p_status_id
FROM "order"
WHERE "id" = p_order_id;
END;
$$ LANGUAGE plpgsql;
---------------№4------------------
CREATE PROCEDURE update_order_status(p_order_id integer, p_status_id integer) AS $$ BEGIN
UPDATE "order"
SET "status_id" = p_status_id
WHERE "id" = p_order_id;
END;
$$ LANGUAGE plpgsql;