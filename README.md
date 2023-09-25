# Автосалон, Щиров Павел Дмитриевич, 153503

>Тема: Электронная Библиотека  
>Группа: 153503  
>Автор: Щиров Павел Дмитриевич

- [Функциональные требования](#функциональные-требования)
- [Перечень сущностей](#сущности)

## Функциональные требования

### Авторизация пользователя:
1. Пользователь должен иметь возможность регистрации нового аккаунта.
2. Пользователь должен иметь возможность входа в систему с использованием учетных данных.
3. Пользователь должен иметь возможность восстановления пароля.
4. Пользователь должен иметь возможность просматривать  каталог товаров(автомобилей).
5. Пользователь должен иметь возможность осуществлять заказ того или иного автомобиля.
   
### Управление пользователями (CRUD):
1. Администратор должен иметь возможность добавлять новых пользователей различных ролей в систему.
2. Администратор должен иметь возможность просматривать, изменять и удалять информацию о пользователях.
3. Администратор должен иметь возможность просматривать, изменять и удалять информацию о товарах.
4. Администратор должен иметь возможность добавлять и удалять товары из каталога.
5. Менеджер должен иметь возможность просматривать, изменять и удалять информацию о пользователях.
6. Менеджер должен иметь возможность просматривать, изменять и удалять информацию о товарах.
7. Менеджер должен иметь возможность добавлять и удалять товары из каталога.

### Система ролей:
1. Система должна поддерживать различные роли пользователей, такие как администратор, менеджер автосалона и клиент.
2. Администратор должен иметь полные права доступа ко всем функциям системы.
3. Менеджер автосалона должен иметь возможность добавлять, редактировать и удалять информацию об автомобилях, а также просматривать информацию о клиентах.
4. Клиент должен иметь возможность просматривать информацию об автомобилях и делать заказы.

### Журналирование действий пользователя:
1. Система должна регистрировать действия пользователей, такие как вход в систему, изменение данных, создание заказов и т.д.
2. Журнал действий пользователя должен содержать информацию о времени и дате действия, пользователе, выполнившем действие, и самом действии.

## Сущности

### 1. user
  - id integer [primary key]
  - login varchar(30) [unique, not null]
  - password varchar(30) [not null]
  - phone phone [not null]
  - email varchar [unique]
  - is_staff bool [not null]
  - is_superuser bool [not null]

### 2. wheel 
  - id integer [primary key]
  - name varchar [not null]

### 3. light 
  - id integer [primary key]
  - name varchar [not null]

### 4. feature 
  - id integer [primary key]
  - name varchar [not null]

### 5. engine 
  - id integer [primary key]
  - name varchar [not null]
  - volume integer [not null]

###6. brand 
  - id integer [primary key]
  - name varchar [not null]

### 7. product 
  - id integer [primary key]
  - model_id integer [not null, ref: - model.id]
  - status_id integer [not null, ref: - product_status.id]
  - wheel_id integer [ref: - wheel.id, not null]
  - light_id integer [ref: - light.id, not null]
  - engine_id integer [ref: < engine.id, not null]
  - feature_id integer [ref: <> feature.id]
  - exterior_color varchar [not null]
  - interior_color varchar [not null]
  - interior_material varchar [not null]

### 8. order
  - id integer [primary key]
  - sum integer [not null]
  - user_id integer [ref: > user.id, not null]
  - car_id integer [ref: - product.id, not null]
  - time datetime [not null]
  - status_id integer [not null, ref: - order_status.id]

### 9. log
  - id integer [primary key]
  - action bool [note: "1 - entrance || 0 - exit", not null]
  - id_user integer [ref: > user.id, not null]

### 10. finance
  - id integer [primary key]
  - action bool [not null, note: "1 - income, 0 - outcome"]
  - sum integer [not null]
  - time datetime [not null]

### 11. employee
  - id integer [primary key]
  - user_id integer [ref: - user.id]
  - hire_date datetime [not null]

### 12. review
  - id integer [primary key]
  - user_id integer [ref: - user.id]
  - text text 
  - rating integer [not null]

### 13. model
  - id integer [primary key] 
  - name varchar [not null]
  - year date [not null]
  - mark_id integer [ref: > mark.id]

### 14. mark
  - id integer [primary key]
  - name varchar [not null]
  - place_of_production varcharv [not null]

### 15. order_status
   - id integer [primary key]
   - status bool [note: "1 - done || 0 - processing", not null]

### 16. product_status
  - id integer [primary key]
  - status bool [note: "1 - in_stock || 0 - not available", not null]
