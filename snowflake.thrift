/* Copyright 2016 Tomoon, Inc. */


service Snowflake {
  i64 get_station_id()
  i64 get_process_id()
  i64 get_timestamp()
  i64 get_id(1:string useragent)
}

