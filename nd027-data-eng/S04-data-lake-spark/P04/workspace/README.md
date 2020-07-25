# Data Lake with Spark

## Introduction

A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The task is to build an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.

## Project Description

In this project, you'll apply what you've learned on Spark and data lakes to build an ETL pipeline for a data lake hosted on S3. To complete the project, you will need to load data from S3, process the data into analytics tables using Spark, and load them back into S3. You'll deploy this Spark process on a cluster using AWS.

## Project Datasets

**Song data: 's3://udacity-dend/song_data'

**Log data: 's3://udacity-dend/log_data'

Song Dataset
The first dataset is a subset of real data from the Million Song Dataset(https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example: *song_data/A/A/B/TRAABJL12903CDCF1A.json*

```{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}```

Log Dataset
The second dataset consists of log files in JSON format. The log files in the dataset with are partitioned by year and month. For example: *log_data/2018/11/2018-11-12-events.json log_data/2018/11/2018-11-13-events.json*

```{"artist":"Pavement", "auth":"Logged In", "firstName":"Sylvie", "gender", "F", "itemInSession":0, "lastName":"Cruz", "length":99.16036, "level":"free", "location":"Klamath Falls, OR", "method":"PUT", "page":"NextSong", "registration":"1.541078e+12", "sessionId":345, "song":"Mercy:The Laundromat", "status":200, "ts":1541990258796, "userAgent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_4...)", "userId":10}```

## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

## Schema for Song Play Analysis
Using the song and log datasets(json), I need to create a star schema optimized for queries on song play analysis. This includes the following tables.


### Fact Tables
* **songplays** - records in log data associated with song plays i.e. records with page NextSong (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent, month, year)

### Dimension Tables

* **users** - users in the app (user_id, first_name, last_name, gender, level)   
* **songs** - songs in music database (song_id, title, artist_id, year, duration)  
* **artists** - artists in music database (artist_id, name, location, latitude, longitude)  
* **time** - timestamps of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)

## Project Template
* **etl.py** reads data from S3, processes that data using Spark, and writes them back to S3  
* **etl.ipynb** test run for small data
* **dl.cfg** contains your AWS credentials    
* **README.md** provides discussion on your process and decisions    


## Project Steps
### Create user on AWS
* get the access key and secret key, and put it into dl.cfg

### Build ETL Pipeline
* Implement the logic in etl.py to extract data from s3 
* Transform data into fact and dimension tables
* Load tables into s3 in parquet format

### Steps
* Run `python3 etl.py` in terminal