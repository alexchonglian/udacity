from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('LowerSongTitles').getOrCreate()

    log_of_songs = [
        "dest",
        "oakak",
        "All the stars",
        "Havana",
    ]

    distributed_song_log = spark.sparkContext.parallelize(log_of_songs)
    print(distributed_song_log.map(lambda x: x.lower()).collect())
    spark.stop()