4.1

--A) НЕСКОЛЬКО УСЛОВИЙ

SELECT o.*
FROM "order" o
JOIN "user" u ON o.user_id = u.id
WHERE u.is_staff = true
  AND o.status_id = 1;


SELECT p.*
FROM "product" p
JOIN "product_status" ps ON p.status_id = ps.id
JOIN "wheel" w ON p.wheel_id = w.id
WHERE ps.status = 1
  AND w.size > 18;


SELECT r.*
FROM "review" r
JOIN "user" u ON r.user_id = u.id
WHERE r.rating > 4
  AND (u.is_staff = true OR u.is_superuser = true);

SELECT *
FROM "order"
WHERE "sum" > 10000
  AND "time" > '2023-01-01';

--Б-В) ВЛОЖЕННЫЕ КОНСТРУКЦИИ, СЛОЖНЫЕ ВЫБОРКИ

--Получить список пользователей (user) и среднюю сумму их заказов (order), только для пользователей с суммой заказов выше среднего значения:

SELECT u.login, AVG(o."sum") AS average_order_sum
FROM "user" u
JOIN "order" o ON u.id = o.user_id
GROUP BY u.login
HAVING AVG(o."sum") > (
  SELECT AVG("sum")
  FROM "order"
);

--Получить список пользователей (user) и их общую сумму заказов (order), только для пользователей, у которых есть как минимум один заказ со статусом (order_status) "выполнен" и как минимум один заказ со статусом "в процессе":

SELECT u.login, SUM(o."sum") AS total_order_sum
FROM "user" u
JOIN "order" o ON u.id = o.user_id
WHERE o.status_id IN (
  SELECT id
  FROM "order_status"
  WHERE status = 1
) AND EXISTS (
  SELECT 1
  FROM "order" o2
  WHERE o2.user_id = u.id
    AND o2.status_id IN (
      SELECT id
      FROM "order_status"
      WHERE status = 0
    )
)
GROUP BY u.login;

--Получить список марок (mark) и количество моделей (model) для каждой марки, у которых есть хотя бы один продукт (product), использующий колеса (wheel) с диаметром, большим 17:

SELECT mk.name, COUNT(DISTINCT m.id) AS model_count
FROM "mark" mk
JOIN "model" m ON mk.id = m.mark_id
JOIN "product" p ON m.id = p.model_id
JOIN "wheel" w ON p.wheel_id = w.id
WHERE w.size > 17
GROUP BY mk.name;

--Получить все заказы (order) с суммой (sum), превышающей среднюю сумму заказов:

SELECT *
FROM "order"
WHERE "sum" > (
  SELECT AVG("sum")
  FROM "order"
);

--4.2 ДЖОИНЫ

SELECT *
FROM "user"
INNER JOIN "order" ON "user".id = "order".user_id;

SELECT *
FROM "user"
LEFT OUTER JOIN "order" ON "user".id = "order".user_id;

SELECT *
FROM "user"
RIGHT OUTER JOIN "order" ON "user".id = "order".user_id;

SELECT *
FROM "user"
FULL OUTER JOIN "order" ON "user".id = "order".user_id;

SELECT *
FROM "user"
CROSS JOIN "order";

SELECT u1.login, u2.login
FROM "user" u1
JOIN "user" u2 ON u1.id <> u2.id;

--4.3

--A) АГРЕГИРУЮЩИЕ

SELECT user_id, AVG("sum") AS avg_order_sum
FROM "order"
GROUP BY user_id;

SELECT EXTRACT(MONTH FROM "time") AS month, SUM("sum") AS total_profit
FROM "order"
WHERE "status_id" = 1 -- Завершенные заказы
GROUP BY EXTRACT(MONTH FROM "time");

--Б) ОКОННЫЕ

SELECT user_id, "sum", SUM("sum") OVER (PARTITION BY user_id) AS total_order_sum
FROM "order";

SELECT user_id, rating, MAX(rating) OVER (PARTITION BY user_id) AS max_rating
FROM "review";

SELECT user_id, "sum", MAX("sum") OVER (PARTITION BY user_id ORDER BY "time" ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS max_order_sum,
       MIN("sum") OVER (PARTITION BY user_id ORDER BY "time" ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS min_order_sum
FROM "order";

--В) HAViNG

SELECT model_id, COUNT(*) AS product_count
FROM "product"
GROUP BY model_id
HAVING COUNT(*) > 0;

SELECT user_id, SUM("sum") AS total_order_sum
FROM "order"
GROUP BY user_id
HAVING SUM("sum") > 1000;

SELECT user_id, AVG("sum") AS avg_order_sum
FROM "order"
WHERE "status_id" = 1 -- "done"
GROUP BY user_id
HAVING MAX("sum") > 500;

--Г) UNION

SELECT name AS model_name
FROM "model"
UNION
SELECT name AS mark_name
FROM "mark";

SELECT name AS model_name, COUNT(*) AS model_count
FROM "model"
GROUP BY name
UNION
SELECT login AS user_name, COUNT(*) AS order_count
FROM "user"
JOIN "order" ON "user"."id" = "order"."user_id"
GROUP BY login;

--4.4

--А) EXISTS

SELECT *
FROM "user"
WHERE NOT EXISTS (SELECT 1 FROM "order" WHERE "order"."user_id" = "user"."id");

SELECT *
FROM "user"
WHERE EXISTS (SELECT 1 FROM "order" WHERE "order"."user_id" = "user"."id");

--Б) INSERT INTO SELECT

INSERT INTO "user" ("login", "password", "phone", "email", "is_staff", "is_superuser")
SELECT "login", "password", "phone", "email", False, False
FROM <source_table>
WHERE <condition>;

INSERT INTO "order" ("sum", "user_id", "product_id", "time", "status_id")
SELECT "sum", "user_id", "product_id", "time", "status_id"
FROM <source_table>
WHERE "sum" > 1000 AND "status_id" = 1;

--В) CASE

SELECT "product"."id", "product"."exterior_color", "product_status"."status",
  CASE
    WHEN "product_status"."status" = 1 THEN 'In Stock'
    WHEN "product_status"."status" = 0 THEN 'Not Available'
    ELSE 'Unknown'
  END AS "availability"
FROM "product"
JOIN "product_status" ON "product"."status_id" = "product_status"."id";

SELECT "order"."id", "order"."sum", "order_status"."status",
  CASE
    WHEN "order"."sum" > 1000 THEN 'High Value'
    WHEN "order"."sum" <= 1000 THEN 'Low Value'
    ELSE 'Unknown'
  END AS "order_type"
FROM "order"
JOIN "order_status" ON "order"."status_id" = "order_status"."id";

--Г) EXPLAIN

EXPLAIN SELECT "product"."id", "product"."exterior_color", "product_status"."status",
  CASE
    WHEN "product_status"."status" = 1 THEN 'In Stock'
    WHEN "product_status"."status" = 0 THEN 'Not Available'
    ELSE 'Unknown'
  END AS "availability"
FROM "product"
JOIN "product_status" ON "product"."status_id" = "product_status"."id";

EXPLAIN SELECT "order"."id", "order"."sum", "user"."login"
FROM "order"
JOIN "user" ON "order"."user_id" = "user"."id";










