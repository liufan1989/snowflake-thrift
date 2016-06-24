#include <iostream>

#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TTransportUtils.h>
#include <sys/time.h>

#include "Snowflake.h"
#include <pthread.h>

using namespace std;
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;

struct timeval minbegin;
struct timeval maxend;

void* thread_process(void * args) {
  int64_t x,y,z,u;
  int i;
  struct timeval begin,end;
  boost::shared_ptr<TTransport> socket(new TSocket("localhost", 7777));
  boost::shared_ptr<TTransport> transport(new TFramedTransport(socket));
  boost::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));
  SnowflakeClient client(protocol);
  try {
    transport->open();
    gettimeofday(&begin,NULL); 
    for(i = 0;i < 10000;++i)
    {
        x = client.get_id("liufan");
        y = client.get_station_id();
        z = client.get_process_id();
        u = client.get_timestamp();
        printf("%ld,%ld,%ld,%ld\n",x,y,z,u);
    }
    gettimeofday(&end,NULL); 
    printf("%ld\n",(end.tv_sec - begin.tv_sec) * 1000  + (end.tv_usec - begin.tv_usec)/1000);
    printf("begin:[%ld.%ld],end[%ld.%ld]\n",begin.tv_sec,begin.tv_usec,end.tv_sec,end.tv_usec);
    transport->close();

  } catch (TException& tx) {
    cout << "ERROR: " << tx.what() << endl;
  }
}

int main()
{
    /*
    int i;
    pthread_t id[10000] = {0};  
    struct timeval begin,end;
    gettimeofday(&begin,NULL); 
    for(i = 0;i < 10000;++i)
    {
        pthread_create(&id[i],NULL,thread_process,NULL);
    }
    pthread_join(id[i-1],NULL);
    gettimeofday(&end,NULL); 
    printf("%ld\n",(end.tv_sec - begin.tv_sec) * 1000  + (end.tv_usec - begin.tv_usec)/1000);
    */
    thread_process(NULL);
    return 0;
}


