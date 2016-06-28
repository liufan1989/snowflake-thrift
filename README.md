# snowflake-thrift
###ID generator is achieved through Apache Thrift library!
* server:cpp 
* client:python  
### Please install apache thrift library fristly;
####1.download source code from http://thrift.apache.org/download
####2.install library from http://thrift.apache.org/lib/ [c++ ,python]

* snowflaked进程是由静态链接生成,所以snowfaked服务进程所运行环境可以不用安装thrift库文件.

* cd snowflake_cpp
* ./make.sh 
* ./make.sh clean

* thrift编译器生成的python文件时,请继承object对象.

* 把thriftpool-1.0文件打包成thriftpool-1.0.tar.gz,然后使用pip install安装这个软件包.

* thriftpool用法可以参考test.py程序运行.


