#!/usr/bin/python
##################this file is edited by liufan#########################

import sys
import datetime
import time  
import Queue
import threading

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

__metaclass__ = type 

class ThriftPool(object):  
    def __init__(self,max_conn=0,ip=None,port=None,clientobj=None,transobj=TTransport.TFramedTransport,protobj=TBinaryProtocol.TBinaryProtocol):#,ping=None,timecheck=60):  
        self.max_conn = max_conn
        self.clientsqueue = Queue.Queue(self.max_conn)
        if ip == None or port == None:
            raise Exception("ThriftPool init fail:ip and port is None.")
        self.thriftserver_ip = ip;
        self.thriftserver_port = port
        self.transobj = transobj
        self.protobj = protobj
        if clientobj == None:
            raise Exception("ThriftPool init fail:clientobj is None.")
        self.clientobj = clientobj
        self.queue_lock = threading.Lock()
        self.clientnum = 0
                
    def __make_connection(self):
        transport = TSocket.TSocket(self.thriftserver_ip,self.thriftserver_port)
        transport = self.transobj(transport)
        protocol  = self.protobj(transport)
        client    = self.clientobj(protocol)
        transport.open()
#       client.transport = transport
#        class ThriftClient(object):
#            def __init__(self,pool,trans,client):
#                self.pool = pool
#                self.client = client
#                self.transport = trans
#            def __del__(self):
#                self.pool.release(self)
#            def close(self):
#                self.pool.release(self)
#        client = ThriftClient(self,transport,client)

        class ThriftClient(self.clientobj):
            def __init__(self,pool,protocol):
                super(ThriftClient,self).__init__(protocol)
                self.pool = pool
                self.flag = True
            def __del__(self):
                if self.flag:
                    self.pool.release(self)
            def __close(self):
                self.transport.close()
                self.flag = False

        client = ThriftClient(self,protocol)
        client.transport = transport
        self.clientnum += 1
        return client

    def conn_size(self):
        if self.clientsqueue == None:
            raise Exception("ThriftPool:connection pool is destroy")
        with self.queue_lock:
            return self.clientsqueue.qsize()

    def client_size(self):
        if self.clientsqueue == None:
            raise Exception("ThriftPool:connection pool is destroy")
        with self.queue_lock:
            return self.clientnum

    def get_connection(self):  
        if self.clientsqueue == None:
            raise Exception("ThriftPool:connection pool is destroy")
        with self.queue_lock:
            if not self.clientsqueue.empty():
                client = self.clientsqueue.get()
                return client
            elif self.clientnum < self.max_conn or self.max_conn == 0:
                client = self.__make_connection()
                return client
            else:
                raise Exception("ThriftPool:no available connection to be used.")

    def release(self,client):
        if self.clientsqueue == None:
            return
        with self.queue_lock:
            try:
                if client.flag:
                    self.clientsqueue.put_nowait(client)
            except Queue.Full:
                client.__close()
                self.clientnum -= 1

    def destory(self):
        with self.queue_lock:
            if self.clientsqueue.qsize() != self.clientnum:
                raise Exception("ThriftPool:Some Connection is not send back to connection pool.")
            self.clientsqueue = None;
            self.clientnum = 0
        
    def __del__(self):
        pass


if __name__ == "__main__":
    pass
    #y = ThriftPool(1,"localhost",7777,Snowflake.Client)
    #z = y.get_connection()
    #print z 
    #print 'sleep 1'
    #time.sleep(30)
    #i = z.get_id("liufan")
    #print i
    #print y.conn_size()
    #print y.client_size()
    #y.release(z)
    #y.destory()
    #print y.conn_size()
    #print y.client_size()
    #del z
    #print 'del z'
    #pdb.set_trace()
    #del z
    #y.destory()
    #print y.conn_size()
    #print y.client_size()
    #time.sleep(30)
    #try:
    #    y.destory()
    #except:
    #    print 'nothing'
    #w = y.get_connection()
    #o = w.get_id("liufan")
    #print o
    
    #time.sleep(30)
    #time.sleep(30)
    #print 'del z'
    #del z 
    #print y.conn_size()

    #z1 = y.get_connection()
    #print z1 
    #for x in xrange(10):
    #    w = z1.get_id("xxx")
    #    print w 
    #time.sleep(30)
    #print 'sleep 2'
    #time.sleep(30)
    #a.release(c)
    #c.transport.close() 
    #print 'sleep 3'
    #time.sleep(30)
    #c1 = a.get_connection()

