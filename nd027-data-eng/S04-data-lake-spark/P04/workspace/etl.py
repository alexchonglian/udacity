import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.types import (
    StructType as R,
    StructField as Fld,
    DoubleType as Dbl,
    StringType as Str,
    IntegerType as Int,
    DateType as Date
)
import pyspark.sql.functions as F


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    read song data from s3
    create the songs_table and artists_table
    dump and upload back to s3.
    @args
        spark: spark session
        input_data: path of song data
        output_data: path of output data
    @return
        None
    """
    # get filepath to song data file
    song_data = os.path.join(input_data, "song_data/*/*/*/*.json")
    
    # create song table schema
    songSchema = R([
        Fld("num_songs",Int()),
        Fld("artist_id",Str()),
        Fld("artist_latitude",Dbl()),
        Fld("artist_longitude",Dbl()),
        Fld("artist_location",Str()),
        Fld("artist_name",Str()),  
        Fld("title",Str()),  
        Fld("duration",Dbl()),  
        Fld("year",Int()),  
    ])
    
    # read song data file
    df = spark.read.json(song_data, schema=songSchema)

    # extract columns to create songs table
    songs_table = df.select(
        [
            "title",
            "duration",
            "year",
            "artist_id"
        ]
    ).dropDuplicates()\
    .withColumn("song_id",F.monotonically_increasing_id())\
    .where(
        ~col("year").isin([0]) & col("year").isNotNull() & col("artist_id").isNotNull()
    )
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year", "artist_id").parquet(output_data + "songs/", mode="overwrite")

    # extract columns to create artists table
    artists_table = df.select(
        [
            "artist_id",
            "artist_name",
            "artist_location",
            "artist_latitude",
            "artist_longitude"
        ]
    ).dropDuplicates().dropna(subset=["artist_id","artist_name"])
    
    # write artists table to parquet files
    artists_table.write.parquet(output_data + "artists/", mode="overwrite")

def process_log_data(spark, input_data, output_data):
    """
    read log data from s3
    create the songplays_table, time_table and users_table
    dump and upload them back to s3.
    @args
        spark: spark session
        input_data: path of song data
        output_data: path of output data
    @return
        None
    """
    # get filepath to log data file
    log_data = input_data + "log_data/*/*/*.json"

    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.filter(df.page == 'NextSong')

    # extract columns for users table    
    users_table = df.selectExpr(
        [
            "userId as user_id",
            "firstName as first_name",
            "lastName as last_name",
            "gender",
            "level"
        ]
    ).dropDuplicates().dropna(how = "any")
    
    # write users table to parquet files
    users_table.write.parquet(output_data + "users/", mode="overwrite")

    df = df.withColumn("start_time", F.to_timestamp(col("ts") / 1000))
    
    # extract columns to create time table
    time_table = df.select("start_time").dropDuplicates()\
    .withColumn("hour",    hour("start_time"))\
    .withColumn("day",     dayofmonth("start_time"))\
    .withColumn("week",    weekofyear("start_time"))\
    .withColumn("month",   month("start_time"))\
    .withColumn("year",    year("start_time"))\
    .withColumn("weekday", date_format("start_time","E"))\
    .dropna(how="any")  
    
    # write time table to parquet files partitioned by year and month
    time_table.write.partitionBy("year", "month").parquet(output_data + "time/", mode="overwrite")

    # read in song data to use for songplays table
    song_df = spark.read.parquet(output_data + "songs/*/*/*")
    artist_df = spark.read.parquet(output_data + "artists/*")
    join_song = df.join(song_df, ((song_df.title == df.song) & (song_df.duration == df.length)))
    artists_songs_logs = join_song.join(artist_df, (join_song.artist == artist_df.artist_name))
    songplays = artists_songs_logs.join(time_table, (artists_songs_logs.start_time == time_table.start_time), 'left').drop(artists_songs_logs.start_time)

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = songplays.selectExpr(
        [
            "start_time",
            "userId as user_id",
            "level",
            "song_id",
            "artist_id",
            "sessionid as session_id",
            "artist_location as location",
            "userAgent as user_agent"
        ]
    ).dropDuplicates()\
    .dropna(subset=["user_id","artist_id", "song_id","start_time"])\
    .withColumn("songplay_id",F.monotonically_increasing_id())

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year", "month").parquet(output_data + "songplays/", mode="overwrite")


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://sparkifytest/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
