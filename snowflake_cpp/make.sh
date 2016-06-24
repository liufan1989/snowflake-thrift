#!/bin/bash

server()
{
g++ -g -O0 -I. -I/usr/local/include/thrift -L/usr/local/lib snowflake_types.cpp snowflake_constants.cpp Snowflake.cpp Snowflake_server.cpp -o snowflaked -Wl,-dn -lthriftnb -lthrift -levent -Wl,-dy -lpthread
}

client()
{
g++ -g -O0 -I. -I/usr/local/include/thrift -L/usr/local/lib snowflake_client.cpp Snowflake.cpp -o snowflake_client -Wl,-dn -lthriftnb -lthrift -levent -Wl,-dy -lpthread
}

install()
{
  cp snowflaked /usr/bin
}
clean()
{
rm snowflaked 
rm snowflake_client
}
if [ "$1" = "server" ]
then
    server
elif [ "$1" = "client" ]
then
    client
elif [ "$1" = "install" ]
then
    install
elif [ "$1" = "clean" ]
then
    clean
else
    server
    client
fi


