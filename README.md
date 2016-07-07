# snowflake-thrift
###ID generator is achieved through Apache Thrift library!
* server:cpp 
* client:python  
####  Please install apache thrift library fristly;
#####1. Download source code from http://thrift.apache.org/download
#####2. Install library from http://thrift.apache.org/lib/ [c++ ,python]

* snowflaked由静态链接生成,所以snowfaked运行环境可以不用安装thrift库文件.
* Thrift编译器生成的python文件,修改Iface继承object对象.
* thriftpool-1.0/thrift/ThriftPool.py为新添加文件，其他为thrift python库的原始文件，用法可以参考test.py程序运行.
* ./make.sh //编译snowflaked
* ./make.sh clean //清理 snowflaked
* tar -zcvf thriftpool-1.0.tar.gz thriftpool-1.0
* pip install thriftpool-1.0.tar.gz




