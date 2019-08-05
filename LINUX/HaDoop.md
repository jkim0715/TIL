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
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/etc/hadoop-1.2.1/tmp</value>
  </property>
  </configuration>
  ```

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

- vi mapred-site.xml

  ```bash
  <configuration>
  <property>
  <name>mapred.job.tracker</name>
    <value>localhost:9001</value>
  </property>
  </configuration>
  ```

- vi hadoop-env.sh

  ```bash
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
hadoop dfs -put README.txt /test
hadoop dfs -put README.txt /data/input1
```



Data 분석하기 ( MapReduce )

```bash
hadoop jar hadoop-examples-1.2.1.jar wordcount /data/input1 /data/output1
```

wordcount 위치

```bash
src>examples>org>apache>examples

vi WordCount.java
```

MapReduce가 어렵고 빡세기 때문에 현업에서 더 많이 사용하는 Tool로 대체하여 학습 할 것임.