# staging-phaas-giving-api:donation {#donation}

# Donation - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar |  |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
| 4 | deleted | 0 | NO | tinyint |  |
| 5 | organization_id | | NO | varchar |  |
| 6 | user_id |  | NO | varchar | Mostly empty, or one of: 000000, genclient:Giving, genclient:GivingManagement, integration-tester@bidpalnetwork.com, phaas-int-test, testUserId |
| 7 | purchase_id | | NO | varchar |  |
| 8 | source |  | NO | varchar |  |
| 9 | source_name |  | NO | varchar |  |
| 10 | source_data |  | NO | varchar |  |
| 11 | impact_name |  | NO | varchar |  |
| 12 | tags |  | NO | varchar |  |
| 13 | tags_searchable |  | NO | varchar |  |
| 14 | amount | 0.00 | NO | decimal |  |
| 15 | donor_first_name |  | NO | varchar |  |
| 16 | donor_last_name |  | NO | varchar |  |
| 17 | donor_street |  | NO | varchar |  |
| 18 | donor_city |  | NO | varchar |  |
| 19 | donor_state |  | NO | varchar |  |
| 20 | donor_zip |  | NO | varchar |  |
| 21 | donor_phone |  | NO | varchar |  |
| 22 | donor_email |  | NO | varchar |  |
| 23 | recipient |  | NO | varchar |  |
| 24 | recipient_url |  | NO | varchar |  |
| 25 | display_name |  | NO | varchar |  |
| 26 | is_anonymous | 0 | NO | tinyint |  |
| 27 | is_dedication | 0 | NO | tinyint |  |
| 28 | dedication_honoree |  | NO | varchar |  |
| 29 | dedication_options |  | NO | varchar |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp | MUL |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | donation |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | donation |
| 4 | deleted | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | donation |
| 5 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 6 | user_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 7 | purchase_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 8 | source |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 9 | source_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 10 | source_data |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 11 | impact_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 12 | tags |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 13 | tags_searchable |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 14 | amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | donation |
| 15 | donor_first_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 16 | donor_last_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 17 | donor_street |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 18 | donor_city |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 19 | donor_state |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 20 | donor_zip |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 21 | donor_phone |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 22 | donor_email |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 23 | recipient |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 24 | recipient_url |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 25 | display_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 26 | is_anonymous | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | donation |
| 27 | is_dedication | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | donation |
| 28 | dedication_honoree |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |
| 29 | dedication_options |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | donation |


@package staging-phaas-giving-api/public
