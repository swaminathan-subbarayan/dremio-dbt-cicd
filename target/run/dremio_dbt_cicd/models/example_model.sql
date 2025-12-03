
  

  create or replace view "dbt_prod"."models"."example_model" as select *
from Samples."samples.dremio.com"."NYC-taxi-trips"
limit 100