#!/usr/bin/python

from thrift import ThriftPool
from snowflake_python.snowflake import Snowflake

if __name__ == "__main__":
     y = ThriftPool.ThriftPool(1,"192.168.1.163",7777,Snowflake.Client)
     #for x in range(10):
     z = y.get_connection()
     print z 
     #print 'sleep 1'
     #time.sleep(30)
     i = z.get_id("liufan")
     print i
     #y.release(z)
     print y.conn_size()
     print y.client_size()
     #del z
     #y.release(z)
     #y.destory()
     #print '=========================='
     #print y.conn_size()
     #print y.client_size()
     #print '=========================='
     #y.destory()
     #print 'sleep(3600*2)'
     #time.sleep(3600*2)
     #print 'sleep 2 hours then get id'
     #i = z.get_id("liufan")
     #print i
     #print '=========================='
     #del z
     #print 'del z'
     #pdb.set_trace()
     #del z
     #y.destory()
     #print y.conn_size()
     #print y.client_size()
     #time.sleep(30)

