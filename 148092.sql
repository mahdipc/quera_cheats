-- Section1
ALTER TABLE users ADD INDEX IX_name(`name`, `id`);


-- Section2
ALTER TABLE products
    ADD INDEX IX_price(`price`, `id`, `name`),
    ADD INDEX IX_category(`category_id`,`price`,`id`, `name`);