# Project: Data Warehouse

## Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

Datasets

**Song Data Path** s3://udacity-dend/song_data

**Log Data Path** s3://udacity-dend/log_data

**Log Data JSON Path** s3://udacity-dend/log_json_path.json

Song Dataset
The first dataset is a subset of real data from the Million Song Dataset(https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example: *song_data/A/A/B/TRAABJL12903CDCF1A.json*

```{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}```

Log Dataset
The second dataset consists of log files in JSON format. The log files in the dataset with are partitioned by year and month. For example: *log_data/2018/11/2018-11-12-events.json log_data/2018/11/2018-11-13-events.json*

```{"artist":"Pavement", "auth":"Logged In", "firstName":"Sylvie", "gender", "F", "itemInSession":0, "lastName":"Cruz", "length":99.16036, "level":"free", "location":"Klamath Falls, OR", "method":"PUT", "page":"NextSong", "registration":"1.541078e+12", "sessionId":345, "song":"Mercy:The Laundromat", "status":200, "ts":1541990258796, "userAgent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_4...)", "userId":10}```

## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

## Fact Table
1. **songplays** - records in log data associated with song plays i.e. records with page NextSong
* songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## Dimension Tables
2. **users** - users in the app
* user_id, first_name, last_name, gender, level
3. **songs** - songs in music database
* song_id, title, artist_id, year, duration
4. **artists** - artists in music database
* artist_id, name, location, latitude, longitude
5. **time** - timestamps of records in songplays broken down into specific units
* start_time, hour, day, week, month, year, weekday

## Project Template
To get started with the project, go to the workspace on the next page, where you'll find the project template. You can work on your project and submit your work through this workspace.

Alternatively, you can download the template files in the Resources tab in the classroom and work on this project on your local computer.

The project template includes four files:
**create_table.py** is where you'll create your fact and dimension tables for the star schema in Redshift.
**etl.py** is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
**sql_queries.py** is where you'll define you SQL statements, which will be imported into the two other files above.
**README.md** is where you'll provide discussion on your process and decisions for this ETL pipeline.

## Steps
1. Run **redshift_create.ipynb** to create redshift cluster, configure dwh.cfg before doing so
2. Run **python3 create_tables.py** in terminal
3. Run **python3 etl.py** in terminal
4. Run **redshift_query_ext_sql.ipynb** (or redshift_query_psycopg2.ipynb) to verify data, e.g. describe tables, count each tables, analyze data by joining multiple tables, etc.
5. Run **redshift_delete.ipynb** to delete redshift cluster, cleanup configs in dwh.cfg, specifically AWS.KEY, AWS.SECRET, IAM_ROLE.ARN


