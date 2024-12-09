CREATE TABLE `piuudcupa_schema`.`migrations` (
  `migration_script_name` VARCHAR(100) NOT NULL,
  `exec_date` DATETIME NULL,
  PRIMARY KEY (`migration_script_name`));
  
ALTER TABLE `piuudcupa_schema`.`migrations` 
CHANGE COLUMN `exec_date` `exec_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ;
