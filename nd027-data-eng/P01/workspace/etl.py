import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    This procedure processes a song file 
    and insert into artists table and songs table.
    args:
    * cur: postgres cursor
    * filepath: the file path to the song file
    """
    # open song file
    df = pd.read_json(filepath, lines=True)
    #for col in df.columns: print(col)
    """
    COLUMNS in song file
    artist_id
    artist_latitude
    artist_location
    artist_longitude
    artist_name
    duration
    num_songs
    song_id
    title
    year
    """
    for artist_data in df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]].values:
        cur.execute(artist_table_insert, artist_data)
    
    for song_data in df[["song_id", "title", "artist_id", "year", "duration"]].values:
        cur.execute(song_table_insert, song_data)
    


def process_log_file(cur, filepath):
    """
    This procedure processes a log file 
    and insert into time table, user_table and songplays table.
    args:
    * cur: postgres cursor
    * filepath: the file path to the log file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)
    #for col in df.columns: print(col)
    """
    COLUMNS in log file
    artist
    auth
    firstName
    gender
    itemInSession
    lastName
    length
    level
    location
    method
    page
    registration
    sessionId
    song
    status
    ts
    userAgent
    userId
    """

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = [[t, t.hour, t.day, t.week, t.month, t.year, t.day_name()] for t in df['ts']]
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame.from_records(time_data, columns=column_labels)
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))
    #print(all_files)

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()