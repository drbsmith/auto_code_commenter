# staging-phaas-giving-api:unattached_user_card {#unattached_user_card}

# Unattached User Card - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | unattached_user_card_id | | NO | varchar |  |
| 2 | organization_id | | NO | varchar |  |
| 3 | source_type | | NO | varchar |  |
| 4 | source_id | | NO | varchar |  |
| 5 | email | | NO | varchar |  |
| 6 | token | | NO | varchar |  |
| 7 | card_last_four |  | NO | varchar |  |
| 8 | card_expiration |  | NO | varchar |  |
| 9 | card_type |  | NO | varchar |  |
| 10 | card_name |  | NO | varchar |  |
| 11 | billing_street |  | NO | varchar |  |
| 12 | billing_city |  | NO | varchar |  |
| 13 | billing_state |  | NO | varchar |  |
| 14 | billing_zip |  | NO | varchar |  |
| 15 | billing_country |  | NO | varchar |  |
| 16 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 17 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | unattached_user_card_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 2 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 3 | source_type | | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 4 | source_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 5 | email | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 6 | token | | NO | varchar | latin1_swedish_ci | varchar(100) |  |  | select |  |  | 100 | 100 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 7 | card_last_four |  | NO | varchar | latin1_swedish_ci | varchar(4) |  |  | select |  |  | 4 | 4 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 8 | card_expiration |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 9 | card_type |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 10 | card_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 11 | billing_street |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 12 | billing_city |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 13 | billing_state |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 14 | billing_zip |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 15 | billing_country |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | unattached_user_card |
| 16 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | 0 | def | staging-phaas-giving-api | unattached_user_card |
| 17 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | 0 | def | staging-phaas-giving-api | unattached_user_card |


@package staging-phaas-giving-api/public
