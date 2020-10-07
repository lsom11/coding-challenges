select owner_name, pe_description from los_angeles_restaurant_health_inspections
where owner_name ILIKE '%BAKERY%'
AND pe_description ILIKE '%LOW%'