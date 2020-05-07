select (substr(date,7,4) || '-' || substr(date,1,2) || '-' || substr(date,4,2))::date
from sf_crime_data limit 10;