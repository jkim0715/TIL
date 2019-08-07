하둡 



### 서버준비 

##### HADOOPSERVER1      

- 50기가

- 4기가 메모리

###### 브릿지 세팅 

- 70.12.114.0 대역으로 만들어짐

- 처음 만들때는 NAT로 만들고 OS설치 후에 Bridge 세팅으로 바꾸기

- ```bash
  IPADDR=70.12.114.222
  NETMASK=255.255.255.0
  GATEWAY=70.12.114.1
  DNS1=168.126.63.1
  ```

- 

###### RAID 사용 안함

###### Clone (HADOOPSERVER2)

- VMX file  가서 displayname 바꾸기
- **Moved it**

- IP ADDR
- MAC ADDR
- HOSTNAME
- /etc/hosts



DB 서버 만들기

- HADOOPSERVER1 클론. 
- 브릿지 사용 x
- 192.168.111.200 으로 세팅  하면 못들어감,... 대역대가 다름....

- ```bash
  scp -rp /etc/hosts root@70.12.114.222:/etc
  ```

- oracle download

  - ```bash
    cd file   (지정했던 다운로드 받는 파일 )
    wget http://70.12.114.50/test/oracle.rpm.zip
    unzip oracle.rpm.zip
    cd Disk1
    yum -y localinstall oracle자동완성..
    
    ```

  - 



### 하둡 환경 만들기

설치전 필요 SW

- 1. JDK
  2. mysql
  3. eclipse
  4. tomcat

1. 하둡 설치 (가상분산모드)

- 다운로드

  - ```bash
    wget "http://www.eu.apache.org/dist/hadoop/common/hadoop-1.2.1/hadoop-1.2.1.tar.gz"
    ```

  -  건물 내 방화벽에 막혔을 경우 따로 파일을 준비한다.

- 압축풀기 및 경로설정

  - ```bash
    tar xvf hadoop-1.2.1.tar.gz
    cp -r hadoop-1.2.1 /etc/
    
    ```

  - ```bash
    vi /etc/profile
    HADOOP_HOME=/etc/hadoop-1.2.1
    export HADOOP_HOME
    PATH.:$HADOOP_HOME/bin:$PATH
    
    
    vi /etc/bashrc
    . /etc/hadoop-1.2.1/conf/hadoop-env.sh 
    
    추가
    ```

  

- ssh 

  네트워크 상의 다른 컴퓨터에 로그인하거나 원격 시스템에서 명령을 실행하고 다른 시스템으로 파일을 복사할 수 있게 해주는 응용 프로토콜이나 응용 프로그램 또는 그 프로토콜을 가르킨다

  - ```bash 
    ssh HADOOPSERVER1
    ```

  - 여기선 원격 조종 같은 의미로 쓰였음.

  -  내가 내자신을 들어갈때도 한번 밖으로 나갔다가 들어와서 비밀번호를 물어봄.

  - Public Key랑 Private Key를 설정하고 들락날락 할떄마다 private key랑 public key를 맞춰보고 맞으면 비밀번호 없이 통과

- Public Key / Private Key 생성(~/.ssh)

  - ```bash
    ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
    ```

    - id_dsa 가 private key / id_dsa.pub 가 public key
    - Public Key  를 배포키로 만들기.

    ```bash
    cat id-dsa.pub >>authorized_keys
    ```

    - 하다가 오류나면 .ssh 폴더를 삭제 후 다시 진행.



하둡 configuration 수정  (/etc/hadoop-1.2.1/conf)

- vi core-site.xml (경로 바뀐거 주의)

  ```bash
  <configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
  </property>2
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/etc/hadoop-1.2.1/tmp</value>
  </property>
  </configuration>
  ```

  - namenode의 접근 포트 지정 (9000) 하는 곳

  

- vi hdfs-site.xml

  ```bash
  <configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.name.dir</name>
    <value>/etc/hadoop-1.2.1/name</value>
  </property>
  <property>
    <name>dfs.data.dir</name>
    <value>/etc/hadoop-1.2.1/data</value>
  </property>
  <property>
    <name>dfs.webhdfs.enabled</name>
    <value>true</value>
  </property>
  </configuration>
  ```

  - replication (복제 수 설정) :1
  - namenode dir 설정 : 어떤 머신에 어떠한 파일들이 들어가 있는지 나타내는 정보를 담는 곳
  - data dir : data가 저장되는 디렉토리
  - webhdfs: 으로 접근할 수 있게 해줌

  

- vi mapred-site.xml

  ```bash
  <configuration>
  <property>
  <name>mapred.job.tracker</name>
    <value>localhost:9001</value>
  </property>
  </configuration>
  ```

  - Jobtracker 포트 설정 : 9001
  - 실제 분석에 대한 요청을 받는 곳.
  - TaskTracker 한태 일을 시키는 곳

  

- vi hadoop-env.sh

  ```bash
  9라인 근처에 
  export JAVA_HOME=/etc/jdk1.8
  export HADOOP_HOME_WARN_SUPPRESS="TRUE"
  ```

-  설정 후 포맷 진행

  ```bash
  hadoop namenode -format
  ```

  sucessfully format 나오면 성공

- 하둡실행 / 종료

  ```bash
  start-all.sh
  stop-all.sh
  ```

  - ```bash
    jps
    ```

방화벽 없애기

```bash
systemctl disable firewalld
```





하둡 운용하기

- start-all.sh  하둡실행

하둡관리창 열기

- http:// localhost:50070

하둡명령어

```bash
hadoop dfs -mkdir /test
hadoop dfs -mkdir /data
hadoop dfs -mkdir /data/input1

hadoop -ls /
파일 넣기
hadoop dfs -put README.txt /test
hadoop dfs -put README.txt /data/input1
파일 가져오기 (/etc/hadoop-1.2.1 으로 가져와짐)
hadoop dfs -get /data/input1/README.txt RD.txt
```



Data 분석하기 ( MapReduce )

JOBTRACKER에 요청 하면 각 서버에 TASKTRACKER 한태 시킴

```bash
hadoop jar hadoop-examples-1.2.1.jar wordcount /data/input1 /data/output1
```

wordcount 위치

```bash
src>examples>org>apache>examples

vi WordCount.java
```

MapReduce가 어렵고 빡세기 때문에 현업에서 더 많이 사용하는 Tool로 대체하여 학습 할 것임.



### 완전분산모드 (서버 4대 / 가상 IP 이용)

HADOOP1  ~4 준비

- ssh 

  Public Key -> Authorized_Keys 배포

  ```bash
  ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
  cd .ssh
  cat id_dsa.pub > authorized_keys
  scp authorized_keys root@hadoop2:~/.ssh/authorized_keys
  scp authorized_keys root@hadoop3:~/.ssh/authorized_keys
  scp authorized_keys root@hadoop4:~/.ssh/authorized_keys
  
  ssh root@hadoop2 cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
  ```

  비밀번호 없이 ssh로 접근 가능.

- 서버 역할 나누기 및 하둡 환경설정

  - etc/hadoop-1.2.1/conf

  - masters

    ```bash
    hadoop2
    ```

  - slaves

    ```bash
    hadoop2
    hadoop3
    hadoop4
    ```

  - core-site.xml

    ```bash
    <configuration>
     <property>
        <name>fs.default.name</name>
        <value>hdfs://192.168.111.201:9000</value>
      </property>
      <property>
        <name>dfs.tmp.dir</name>
        <value>/etc/hadoop-1.2.1/tmp</value>
      </property> 
    </configuration>
    
    ```

  - hdfs-site.xml

    ```bash
    <configuration>
      <property>
        <name>dfs.permissions</name>
        <value>false</value>
      </property>
      <property>
        <name>dfs.replication</name>
        <value>2ㅗ</value>
      </property>
      <property>
        <name>dfs.http.address</name>
        <value>192.168.111.201:50070</value>
      </property>
      <property>
        <name>dfs.secondary.http.address</name>
        <value>192.168.111.202:50090</value>
      </property>
      <property>
        <name>dfs.name.dir</name>
        <value>/etc/hadoop-1.2.1/name</value>
      </property>
      <property>
        <name>dfs.data.dir</name>
        <value>/etc/hadoop-1.2.1/data</value>
      </property> 
    </configuration>
    
    ```

  - mapred-site.xml

    ```bash
    <configuration>
      <property>
       <name>mapred.job.tracker</name>
       <value>192.168.111.201:9001</value>
      </property> 
    </configuration>
    
    ```

  - hadoop-env.sh

    ```bash
    export JAVA_HOME=/etc/jdk1.8
    export HADOOP_HOME_WARN_SUPRESS="TRUE"
    ```

    

- 하둡 설정한거 압축 및 배포 후 압축풀기

  ```bash
  tar cvfz hadoop.tar.gz hadoop-1.2.1
  
  hadoop2,3,4동일하게 진행
  scp hadoop.tar.gz root@hadoop2:/etc
  scp /etc/profile root@hadoop2:/etc
  sco /etc/bashrc root@hadoop2:/etc
  ```

  압축풀기

  ```bash
  ssh root@hadoop2 tar xvf /etc/hadoop.jar.gz /etc
  ssh root@hadoop3 tar xvf /etc/hadoop.jar.gz /etc
  ssh root@hadoop4 tar xvf /etc/hadoop.jar.gz /etc
  혹은 한번에 가능
  ssh root@hadoop2 "cd /etc;tar xvfz hadoop.tar.gz;rm -rf hadoop.tar.gz"
  ```

  포멧 

  ```bash
  hadoop namenode -formant
  ```

  



### HDFS

#### HDFS 명령어 (난중에 정리 p 80쪽)

Hadoop fs -cmd [args] 치면 다나옴 쳐서 보셈.

HDFS에 폴더 생성 및 조회

```bash
hadoop fs -mkdir mydir 폴더 생성
hadoop fs -ls  현재 디렉토리 파일 리스트
hadoop fs -ls <PATH> PATH에 있는 파일 리스트 
hadoop fs -lsr 현재 디렉토리의 하위 디렉토리까지 풀어서 보여줌
```

파일 용량 확인

```bash
hadoop fs -du <path>  지정한 디렉터리나 파일의 사용량을 확인 (바이트단위)
hadoop fs -dus <path> -du는 파일별 용량 -dus는 디렉터리 용량합계
```

파일 내용보기

```bash
hadoop fs -cat <파일> 파일의 내용출력
hadoop fs -text <파일> -cat은 텍스트 파일만 가능하지만 -text는 zip파일도 가능
```

파일 복사 

```bash
hadoop fs -put / -get / -getmerge / -cp / -copyFromLocal / -copyToLocal
-put : 지정한 로컬 파일 시스템의 파일 및 디렉터리를 목적지 경로로 복사
-copyFromLocal : -put이랑 동일한 기능
-get : HDFS에 저장된 파일을 로컬 파일시스템으로 복사
-getmerge : 지정한 경로에 있는 모든 파일의 내용을 합친 후 로컬 파일 시스템에 하나의 파일로 복사
```



파일삭제

```bash
hadoop fs -rmr /mydir
```



휴지통 비우기 

```bash
hadoop fs -expunge 
```





#### 맵 리듀스 (Map Reduce)

Map + Reduce

구성 : 클라이언트 + 잡트래커 + 태스크트래커 





### 하이브

#### 사전준비 (Mysql)

1. Mysql 설치 및 root 아디 만들기 (LINUX 참고)

2. root로 로그인해서 기본환경 세팅

   ```bash
   mysqladmin -u root password '111111'
   mysql -u root -p mysql
   
   grant all privileges on *.* to 'hive'@'localhost' identified by '111111';
   flush privileges;
   
   create database hive_db;
   grant all privileges on hive_db.* to 'hive'@'%' identified by '111111' with grant option;
   grant all privileges on hive_db.* to 'hive'@'localhost' identified by '111111' with grant option;
   grant all privileges on hive_db.* to 'hive'@'%' identified by '111111' with grant option;
   flush privileges;
   commit;
   ```

   

3. 하둡 1이면 버전 1.0.1  / 하둡 2면 최신 ( 2.0.0 )

#### 설치

```bash
wget http://archive.apache.org/dist/hive/apache-hive-1.0.1-bin.tar
```

이거 안되면 웹에서 다운로드 후 가져오기

- 압축 풀고 이름 hive로 바꿔서 /etc 밑에 넣기 

- /etc/profile에 경로 설정

  - ```bash
    export HIVE_HOME=/usr/local/hive
    export HADOOP_HOME=/usr/local/hadoop
    PATH=$PATH:$HOME/bin:$HADOOP_HOME/bin:$HIVE_HOME/bin:
    ```

    

- /etc/hive/conf 에 hive-site.xml 만들기

  ```bash
  <?xml version="1.0"?>
  <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
  <configuration>
      <property>
          <name>hive.metastore.local</name>
          <value>true</value>
          <description>controls whether to connect to remove metastore server or open a new metastore server in Hive Client JVM</description>
      </property>
      <property>
          <name>javax.jdo.option.ConnectionURL</name>
          <value>jdbc:mariadb://localhost:3306/hive_db?createDatabaseIfNotExist=true</value>
          <description>JDBC connect string for a JDBC metastore</description>
      </property>
      <property>
          <name>javax.jdo.option.ConnectionDriverName</name>
          <value>org.mariadb.jdbc.Driver</value>
          <description>Driver class name for a JDBC metastore</description>
      </property>
      <property>
          <name>javax.jdo.option.ConnectionUserName</name>
          <value>hive</value>
          <description>username to use against metastore database</description>
      </property>
      <property>
          <name>javax.jdo.option.ConnectionPassword</name>
          <value>111111</value>
          <description>password to use against metastore database</description>
      </property>
  </configuration>
  
  ```



#### 하이브랑 MariaDB 연동하기 

하이브에 Maria JDBC lib 넣기.

```bash
cp mariadb-java-client-1.3.5-jar /etc/hive/lib
```

주의할 점 : MariaDB java Client 버전이 다르면 동작이 안할 수 있음 !!. (1.3.5 사용 할 것)

#### HDFS에 하이브가 사용할 파일 만들어 놓기  및 권한 부여 

1. 하이브 실행하기전에 HDFS 키고 MaraDB 준비 

2.  하이브가 사용할 폴더를 만들거임 tmp

   ```bash
   hadoop dfs -mkdir /tmp
   hadoop dfs -mkdir /user/hive/warehouse
   hadoop dfs -chmod g+w /tmp
   hadoop dfs -chmod g+w /user/hive/warehouse
   ```

   

3. Hive 실행

   ```bash
   hive
   ```

   - 명령어를 실행하면 한번 에러나면서 /tmp 밑에 hive 폴더가 생김 (권한이 없어서 Hive 실행이 안되는거임)

   - 하둡 제어창에서 확인(50070)

   

4. tmp/hive폴더에 권한 부여 후 하이브 재실행 하면 동작됨

   ```bash
   hadoop dfs -chmod 777 /tmp/hive
   
   hive
   ```

##### Hive에 데이터 테이블 작성 및 파일 업로드

- hdi.txt 파일 준비 (data)

- hive에서 hdi.txt 파일에 있는 데이터 형식 mysql에 테이블로 정의하기 (create table HDI)

  ```bash
  hive> CREATE TABLE HDI(id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, 
  
  eysch INT, gni INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS 
  
  TEXTFILE;
  ```

- 하이브에서 hid.txt 를 HDFS 에 올리기 (load)

  ```bash
  hive>load data local inpath '/root/hdi.txt' into table HDI;
  ```

- 확인

  ```bash
  hive> select * from hdi limit 5;
  ```

  

### 문제 발생시  대처

1. 하둡이 실행이 되지 않을 때

   - /etc/hadoop-1.2.1

   - name /data /tmp 삭제 후  format 및 실행

2. 윈도우에서 Hadoop관리창이 안열릴 경우
   - c\Windows\System32\drivers\etc 에 들어가서  hosts파일 수정 ( 하둡서버 호스트네임 추가)