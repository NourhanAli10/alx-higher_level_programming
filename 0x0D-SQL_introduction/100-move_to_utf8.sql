-- script that converts hbtn_0c_0 database to UTF8 
-- (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

ALERT DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALERT TABLE first_table CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALERT TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
