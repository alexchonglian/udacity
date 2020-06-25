import configparser


# CONFIG

config = configparser.ConfigParser()
config.read('dwh.cfg')

LOG_DATA  = config.get("S3", "LOG_DATA")
LOG_PATH  = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")
IAM_ROLE  = config.get("IAM_ROLE","ARN")

# DROP TABLES

staging_events_table_drop   = "drop table if exists staging_events"
staging_songs_table_drop    = "drop table if exists staging_songs"
songplay_table_drop         = "drop table if exists songplays"
user_table_drop             = "drop table if exists users"
song_table_drop             = "drop table if exists songs"
artist_table_drop           = "drop table if exists artists"
time_table_drop             = "drop table if exists time"

# CREATE TABLES

staging_events_table_create= ("""
    create table staging_events (
        artist              varchar,
        auth                varchar,
        firstName           varchar,
        gender              varchar,
        itemInSession       integer,
        lastName            varchar,
        length              float,
        level               varchar,
        location            varchar,
        method              varchar,
        page                varchar,
        registration        float,
        sessionId           integer,
        song                varchar,
        status              integer,
        ts                  timestamp,
        userAgent           varchar,
        userId              integer 
    )
""")

staging_songs_table_create = ("""
    create table staging_songs (
        num_songs           integer,
        artist_id           varchar,
        artist_latitude     float,
        artist_longitude    float,
        artist_location     varchar,
        artist_name         varchar,
        song_id             varchar,
        title               varchar,
        duration            float,
        year                integer
    )
""")

songplay_table_create = ("""
    create table songplays (
        songplay_id         integer identity(0,1) primary key,
        start_time          timestamp not null sortkey distkey,
        user_id             integer not null,
        level               varchar,
        song_id             varchar not null,
        artist_id           varchar not null,
        session_id          integer,
        location            varchar,
        user_agent          varchar
    )
""")

user_table_create = ("""
    create table users (
        user_id             integer not null sortkey primary key,
        first_name          varchar not null,
        last_name           varchar not null,
        gender              varchar not null,
        level               varchar not null
    )
""")

song_table_create = ("""
    create table songs (
        song_id             varchar not null sortkey primary key,
        title               varchar not null,
        artist_id           varchar not null,
        year                integer not null,
        duration            float
    )
""")

artist_table_create = ("""
    create table artists (
        artist_id           varchar not null sortkey primary key,
        name                varchar not null,
        location            varchar,
        latitude            float,
        longitude           float
    )
""")

time_table_create = ("""
    create table time (
        start_time          timestamp not null distkey sortkey primary key,
        hour                integer not null,
        day                 integer not null,
        week                integer not null,
        month               integer not null,
        year                integer not null,
        weekday             varchar not null
    )
""")

# STAGING TABLES

staging_events_copy = ("""
    copy staging_events from {bucket}
    credentials 'aws_iam_role={role}'
    region      'us-west-2'
    format       as JSON {path}
    timeformat   as 'epochmillisecs'
""").format(bucket=LOG_DATA, role=IAM_ROLE, path=LOG_PATH)

staging_songs_copy = ("""
    copy staging_songs from {bucket}
    credentials 'aws_iam_role={role}'
    region      'us-west-2'
    format       as JSON 'auto'
""").format(bucket=SONG_DATA, role=IAM_ROLE)

# FINAL TABLES

songplay_table_insert = ("""
    insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    select
        distinct(e.ts)  as start_time, 
        e.userId        as user_id, 
        e.level         as level, 
        s.song_id       as song_id, 
        s.artist_id     as artist_id, 
        e.sessionId     as session_id, 
        e.location      as location, 
        e.userAgent     as user_agent
    from staging_events e
    join staging_songs  s
    on e.song = s.title and e.artist = s.artist_name and e.page = 'NextSong'
""")

user_table_insert = ("""
    insert into users (user_id, first_name, last_name, gender, level)
    select
        distinct(userId)    as user_id,
        firstName           as first_name,
        lastName            as last_name,
        gender,
        level
    from staging_events
    where user_id is not null
    and page = 'NextSong'
""")

song_table_insert = ("""
    insert into songs (song_id, title, artist_id, year, duration)
    select
        distinct(song_id) as song_id,
        title,
        artist_id,
        year,
        duration
    from staging_songs
    where song_id is not null
""")

artist_table_insert = ("""
    insert into artists (artist_id, name, location, latitude, longitude)
    select
        distinct(artist_id) as artist_id,
        artist_name         as name,
        artist_location     as location,
        artist_latitude     as latitude,
        artist_longitude    as longitude
    from staging_songs
    where artist_id is not null
""")

time_table_insert = ("""
    insert into time (start_time, hour, day, week, month, year, weekday)
    select 
        distinct(start_time)               as start_time,
        extract(hour  from start_time)     as hour,
        extract(day   from start_time)     as day,
        extract(week  from start_time)     as week,
        extract(month from start_time)     as month,
        extract(year  from start_time)     as year,
        extract(dayofweek from start_time) as weekday
    from songplays
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
