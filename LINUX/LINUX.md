# LINUX



### 1.Virtual Machine 설치,

- vmware
- Virtual Box



**VMware-player-5.0.4**

1. create new virtual machine
2. select i will install os later
3. select CentOS 64-bit
4. name :CentOS 64-bit 20190718
5. location: C:\CENTOS
6. max disc size :30 GB
7. edit virtual machine setting
   1. CD/DVD
   2. Use ISO image file to install linux

CentOS 설정

1. 키보드 
   1. 영어(미국)
2. 소프트웨어 선택
   1. 개발 및 창조를 위한 
3. 네트워크
   1. 켬 (IP주소를 자동으로 할당해 줌)
4. 설치대상
   1. 파티션 설정
   2. /SWAP: 2GB (하드웨어를 메모리로 설정하여 부족한 메모리 충당) , 마운트 지점 추가
   3. / 추가
5. 관리자 및 사용자 정보설정
   1. 관리자 비번 111111
   2. 사용자 아이디 비번 : centos/111111

### 2. 가상머신 파일을 복사해서 Clone 만들기

1. C드라이브에 있는 CENTOS 를 복사하여 CENTOS2를 만들고 
2. Configuration file의 displayname을 바꾸고
3. VMware에서 CENTOS2 로 들어가서 추가하기.
4.  반드시 moved it 을 선택하여 실행.
5. edit -network Adapter -advanced- Mac addr generate
6. terminal 에서 gedit /etc/sysconfig/network-scripts/ifcfg-ens33   ex)ens33 달라질 수 있음.
7. Mac addr 복사한거 HWADDR 에 붙여넣기 ex)00:50:56:35:05:0C



### 3. 가상 컴퓨터 설정 (매우 중요)

1. YUM 명령어를 이용하여 소프트웨어 업데이트를 할때도 버전에 맞는 소프트웨어만 다운로드하도록 설정
   - cd /etc/yum.repos.d/
   - ls
   - gedit CentOS-Base.repo
     - 최소모드로 LINUX를 설치 했을 경우 wget이 없기 떄문에 먼저 설치해야함
     - yum -y install wget* 로 설치
   - released updates 부분 삭제
   - gedit CentOS-Sources.repo
   - released updates 삭제



2. CentOS 7.0 (1406) 버전이 계속 설치되도록 터미널에서 설정 변경

   - cd /etc/yum.repos.d/
   - mv CentOS-Base.repo CentOs-Base.repo.bak
   - wget http://download.hanbit.co.kr/centos/7/CentOS-Base.repo
   - rm *.repo~

   

3. IP 주소 고정할당

   - cd /etc/sysconfig/network-scripts/
   - gedit ifcfg-ens33
     - 수정 : BOOTPROTO = "dhcp " --> none
     - 추가 :
       -  IPADDR =192.168.111.100
       - NETMASK=255.255.255.0
       - GATEWAY=192.168.111.2
       - DNS1 = 192.168.111.2
   - **systemctl restart network**   이 명령어를 사용하여 항상 바꾼뒤에 변경내용을 Apply 해줘야 함

4. HOSTNAME 변경하기 

   - hostnamectl set-hostname server1
   - gedit /etc/hosts
     - 192.168.111.100   server1 저장하고 나오기
   - reboot 한번 하기 

5.  SELinux 보안 해제 

   - gedit /etc/sysconfig/selinux
     - SELINUX = disabled 로 바꾸고 저장.





gedit /etc/sysconfig/network-scripts/ifcfg-ens33 

00:50:56:35:05:0C



### 4.WinClient 설치해보기

display name: WIN8

HDD: 30G

MEMORY :4G

IP: 192.168.111.200

- N6KXJ - P6YWY - 4C92Q - J7BVB - R6XGM
- Window만 설치 하기로  INSTALL하기.
- 계정 없이 로그인으로 설정 
- HOTS file에 IP ADDRESS랑 이름 등록해두기



윈도우에서 다른 컴퓨터 가상머신으로 접근 할 노ㅕㅅ수 있도록 만들어 보기.





# 서버 구축시 필수 개념 및 명령어

### 시작과 종료 (p147)

##### 종료

- poweroff
- shutdown -p now
  - now 자리에 숫자를 쓰면 몇분 후 에 종료인지 명시
  - ex) shutdown -p +3  : 3분후에 종료.
- halt -p
- init 0



단축키

- TAB  :자동완성
- Ctrl + l :콘솔창 청소 

### 리눅스 기본 명령어 (p183)

- cd : (change directory) home으로 가기
  - cd ~centos 
    - centos라는 사용자의 홈으로 가기
  - cd .. 
    - 바로 상위 dir로 이동                   
  - cd /etc/sysconfig
    - /etc/sysconifg 경로대로 이동
  - cd ../etc/sysconfig
    - 상대 경로로 이동

- pwd	: (print working directory)
- ls : (LiSt) directory 내 파일명 출력
  - ls /etc/sysconfig
  - ls -a
    - 숨김파일 목록도 표시
  - ls -l
    - 현재 dir 목록을 자세히 보여줌
  - ls -la
  - ls *.cfg
    - 확장자가 cfg인 애들을 보여줌
  - ls -l .etc.sysconfig/a*
    - 앞글자가 a인거 list 하기.
  - man ls
    - 매뉴얼 보기
- su : Switch User
  - su centos
  - su root (관리자 비번 필요)
  - exit : logout 같은거  (가상의 공간에서 여러개의 계정으로 계속 들어갈 수 있다.) 맨 끝까지 exit하면 터미널 종료됨.
- rm : ReMove
  - rm abc.txt
  - rm -i abc.txt
    - 삭제시 한번 더 물어봄
  - rm -f abc.txt
    - 확인하지 않고 바로 삭제
  - rm -r abc
    - 해당 dir을 삭제
  - rm -rf abc
    - dir와 그아래 파일들 싹 다 삭제 
- cp : CoPy
  - cp abc.txt cba.txt
  - cp -r abc cba
- mv : Move
  - mv abc.txt /etc/sysconfig/
  - mv aaa bbb ccc ddd
  - mv abc.txt www.txt
- mkdir : MaKe DIRectory
  - mkdir dir1
  - mkdir -p /def/fgh
- rmdir : ReMove DIRectory
  - rmdir abc
  - rm -rf dir

- history : 명령어 기록보기. 방향키를 눌러 선택가능

- cat (file_name) : 문서를 콘솔창에 display

  - more (file_name) : space를 치면 조금씩 내려감. 천천히 볼 수 있음.

- touch 를 이용하여 원하는 파일 생성

  



vi : 명령모드 진입. (p165 참고)

- vi (file name) 으로 원하는 파일의 명령모드 진임.
-  :  누르고 q   : 나가기
  - q!  저장 안하고 나가기.
  - Terminal을 비정상적으로 종료했을 시 swp file로 저장된다.
  - ls -al
    - rm .t2.txt.swp   :swp 파일 지워서 메시지 안뜨게 하기
-  i :  insert mode
  - 명령모드로 ESC를 누르면 나가짐
  - 소문자 I는 왼쪽  a는 오른쪽
  - 대문자 I는 왼쪽 끝  대문자 A는 오른쪽 끝으로 커서 이동
- : wq (file name)   파일이름 저장하고 나오기
- y 누르고 p  :복사 붙혀넣기
- hjkl : 방향 키 



### 사용자 관리

리눅스는 다중 사용자 시스템이다. 즉 1대의 리눅스에 사용자 여러명이 동시에 접속 가능.



사용자와 그룹

/etc/passwd 로 사용자 정보 확인



###### 사용자관리 명령어

- useradd
  - useradd newuser
    - newuser 라는 사용자 생성
  - useradd -u 1111 newuser
    - newuser라는 아이디를 생성하면서 사용자 ID를 1111로 지정
  - useradd -g myhome newuser
    - newuser라는 사용자를 생성하면서 mygroup에 newuser 사용자 포함(mygroup을 먼저 만들어야함)
  - useradd -d /newhome newuser
    - newuser 사용자를 생성하면서 홈 디렉터리를 /newhome으로 지정
  - useradd -s /bin/csh newuser 
    - newuser 사용자를 생성하면서 기본 셸을 /bin/csh로 지정
- passwd
  - passwd newuser
    - newuser의 비밀번호 생성
- usermod 
  - usermod -g root newuser
    - newuser의 사용자의 그룹을 root그룹으로 변경
- userdel
  - userdel newuser 
  - userdel -r newuser 
    - newuser를 삭제하면 홈디렉토리까지 삭제 
- change
  - change -l newuser
    - newuser사용자에 설정된 사항 확인
  - change -m 2 newuser
    - newuser 사용자에 설정한 암호를 사용해야하는 최소 일자 (즉 변경 후 최소 2일 사용해야함)
  - change -M 30 newuser
    - newuser 사용자에 설정한 암호를 사용할 수 있는 최대 일자.
  - change -E 2019/07/23
    - newuser 사용자에 설정된 비번 만료날자
  - change -W 10 newuser
    - newuser 사용자에 설정한 암호가 만료되기 전에 경고하는 기간, 기본값 7일 
- groups
  - groups
    -  현재 사용자의 소속을 보여줌
  - groups newuser
    - newuser가 소속된 그룹을 보여줌
- groupadd
  - groupadd newgroup
    - newgroup이라는 그룹을 생성
  - groupadd -g 2222 newgroup
    - 그룹을 생성하면서 그룹 ID를 2222로 설정
- groupmod
  - groupmod -n newgroup mygroup 
    - newgroup의 이름을 mygroup으로 바꿈
- groupdel
  - groupdel newgroup 
    - newgroup삭제
- gpasswd
  - gpasswd newgroup
    - newgroup암호지정
  - gpasswd -A newuser newgroup 
    - newuser사용자를 newgroup의 관리자로 지정
  - gpasswd -a user1 newgroup
    - user1을 newgroup의 사용자로 추가
  - gpasswd -d newuser newgroup
    - user1을 newgroup 사용자에서 제거



파일과 디렉토리 소유와 허가권

파일 유형 

- d (디렉토리)
- -(일반파일)
- b(블록파일)
- c(문자 디바이스)
- l(링크)



파일 허가권 (Read, Write, X)

| 소유자    | 그룹      | 그외 사용자 |
| --------- | --------- | ----------- |
| r - w - x | r - w - x | r - w - x   |
| 4 - 2 - 1 | 4 - 2- 1  | 4 - 2 - 1   |

- chmod _ _ _ (file/dir)
  - chmod 4 4 0 musersfile

파일 소유권



- chown 으로 바꿀 수 있음
  - chown .group (file/dir)  (file/dir)의 그룹권한을 바꿀 수있음
- chgrp 로도 가능





###### 링크

- 하드링크
  - 용량 그대로
- 심볼릭 링크
  - 바로가기 같은 느낌  용량 없음



파일 위치 검색

- find
  - find ~ -size 0k -exec cp {} temp \;



파일 압축 및 묶음

- xz
  - xz 파일이름
  - xz -d 파일이름
  - xz -l 파일이름
  - xz -k 파일이름
- bzip2
  - bzip2 파일이름
  - bzip2 -d 파일이름
- gzip
  - gzip 파일이름
  - gzip -d 파일이름.gz
- zip



압축풀기

- tar

- 동작

  - c (소문자) 
    - 새로운 묶음을 만든다
  - x
    - 묶인 파일을 푼다
  - t
    - 묶음을 풀기전에 묶인 경로를 보여준다
  - C(대문자)
    - 묶음을 풀 떄 지정된 디렉터리에 압축을 푼다. 지정하지 않으면 묶을 떄와 동일한 디렉토리에 묶음이 풀린다

- 옵션

  - f(필수)

    - 묶음 파일 이름 지정, 원래 tar는 테이프 장치 백업이 기본이다.(생략하면 테이프로 보내짐)

  - v 

    - visual의 의미로 파일이 묶이거나 풀리는 과정을 보여준다

  - J(대문자)

    - tar+xz

  - z(소문자)

    - tar + gzip

  - j(소문자)

    - tar + bzip2

    

  



### **파일 다운로드**

YUM

- yum -y install 패키지이름
  - 패키지이름
- yum localinstall rpm파일이름.rpm
- yum groupinstall "패키지 그룹 이름"
  - 패키지 그룹이름은 자기가 직접 서치해야함.

RPM



##### JDK 설치하기

- mkdir file

- cd/file 

  - file에 복사해서 붙혀넣기

- ```
  tar xvf jdk-8u221-linux-x64. tar.gz
  mv jdk1.8.0_221/ jdk1.8
  cp -r jdk1.8 /etc
  cd /usr/bin
  ln -s /etc/jdk1.8/bin/java java
  ```

- 

- 



시스템 전역변수 설정

- vi /etc/profile

  - ```
    JAVA_HOME=/etc/jdk1.8
    export JAVA_HOME
    CLASSPATH=$JAVA_HOME/lib
    export CLASSPATH
    PATH=.:JAVA_HOME/bin:$PATH
    ```

    



##### Eclipse 설치하기

- home 에 file 이라는 폴더를 만들고  eclipse .tar.gz 파일을 넣어둔다
- tar xvf eclipse- jee- oxygen- 3a- linux- gtk- x86_64.tar.gz  
  - 압축, 묶음 동시에 풀기
  - tab키를 잘 활용한다
- cp -r eclipse /etc
  - etc 밑에 이클립스 폴더 복사 
- cd /usr/bin
  - 여기 밑에 링크파일 만들거임
- ln -s  /etc/eclipse/eclipse eclipse
  - 심볼릭 링크 만들기

##### Tomcat 9.0 설치하기

- file이라는 폴더안에 tomcat.tar.gz 파일 넣어두고
- tar xvf tomcatxxxxxx.tar.gz
  - 압축 풀기
- 압축 풀면 설치 끝
- firewall-config 
  - HTTP 체크
  - 1521포트 추가
- conf 폴더 
  - 들어가서 Server.xml 에 포트 8080을 80으로 바꾸기
- bin 폴더
  - startup.sh 서버 실행 
  - shutdown.sh 서버 종료 



CRON

- minute hour dayofmonth month dayofweek username command to be executed.

```
vi /etc/crontab
```

- ex) 매월 24일 11시 10분에 home을 backup에 카피
  - ```
    10 11 24 * * root cp -r /home /backup
    ```

- systemctl status crond

  - crondemon. 눈에 보이지 않지만 뒤에서 돌아가는 process.

- systemctl restart crond



- 특정 dir에 실행 파일 넣어두고 주기적으로 동작 시킬 수 도 있음.

- /etc 
  - ls cron* 
    - daily / hourly / monthly / weekly 디렉토리가 있다.



AT

- 일회성 작업을 예약 실행 ( 한번 실행 후 소멸 )

- ```
  at 11:25 am today
  cp -r /home /backup
  reboot
  ```

- 오늘 11시 25분에  home을 backup 폴더에 카피 후 리부팅. 

- Ctrl + D 를 눌러서 edit창 종료.



정확한 시간을 맞추는 방법

```
rdate -s time.bora.net
```



##### Oracle DB Express 설치

- www.oracle.com 

  - 리눅스용 오라클 11g  Release 2 를  다운 받아서 file에 넣어두기

- unzip oracle

  - zip파일로 압축 되어있는 파일을 풀면 Disk1

- 먼저 메모리 swap을 충분히 확보

  - ```
    dd if=/dev/zero of=/swapfile bs=1024 count=4194304
    mkswap /swapfile
    swapon /swapfile
    swapon -s
    ```

  - 기존 2기가에 4기가 추가.

  - 재부팅 후에도 사용하려면

    - ```
      /etc/rc.d/
      chmod 755 rc.local
      
      ```

    - ```
      vi rc.local
      swapon /swapfile
      ```

- 설치

  - cd /root/file/Disk1
  - ls -l
  - yum -y localinstall oracle*

- service oracle-xe configure  또는 /etc/init.d/oracle-xe configure 를 입력해 환경설정

  - Specify the HTTP ~~Application Express (8080) :
  - Specify the port ~~ database listner (1521) :
  - Specify password ~ initial cofiguration: 암호입력
  - confirm password
  - Do you want ~~boot : [y]

- 설치가 완료되면

  - /etc/init.d/oracle-xe start  로 실행
  - start/stop/status

- 오라클 환경 설정

  - . /u01/app/oracle/product/11.2.0/xe/bin/oracle_env.sh  (제일앞에 . / 공백있음)
  - vi /etc/bashrc 에 똑같이 적어주면 재부팅 후에도 설정유지
    - . /u01/app/oracle/product/11.2.0/xe/bin.oracle_env.sh

- firewall-config

  - 포트 8080 추가
  - 포트 1521 추가 







##### 관리자 명령어

파이프(pipe)

- ls -a | more
  - 첫번째 명령어에 더해서 다른 명령어를 더하고 싶을 때 사용



ps -ef 

- 프로그램에서 사용하고 있는 모든 프로세스를 리스트
- ps -ef | grep oracle
  - grep을 사용하여 oracle 필터링
- ps -ef | grep java
  - kill 61292 



kill 

- 현재 동작하고 있는 프로세서 를 강제적으로 죽임
  - kill -9
    - 강제로 죽이기



Redirection

- 터미널에서 실행된 내용을 파일로 만들 수 있음
- ls -l > list.txt
- sort < 20190725.txt > sort201907125.txt



foreground 

- 터미널 조작 불가. 
- yes
- 

 background로 프로그램돌리기

- yes end

- gedit &



##### Maria DB 설치

- 마리아 DB 설치파일 받기

  - ```
    MariaDB-10.0.15-centos7_0-x86_64-client.rpm
    MariaDB-10.0.15-centos7_0-x86_64-common.rpm
    MariaDB-10.0.15-centos7_0-x86_64-server.rpm
    ```

- 다운로드한 파일설치

  - ```
    yum -y remove mariadb-libs
    ```

    -  설치 전 충돌나는 파일 미리 제거

  - yum -y localinstall Maria*

- 실행

  - ```
    systemctl restart mysql
    systemctl status mysql
    chkconfig mysql on
    ```

- firewall-config

  - mysql 포트 오픈 



###### MariaDB 활용

- ADMIN 계정 설정
  - mysqladmin -u root password '111111'
- ADMIN 계정 접속
  - mysql -u root -p
    - 비밀번호 입력.
- 



유저정보

- SELECT user, host from user;

  - 유저정보 조회

- 유저 권한 추가

  - ```
    GRANT ALL PRIVILEGES ON *.* TO user@'192.168.111.%' IDENTIFIED BY '111111';
    ```

  - 

유저로 로그인

- mysql -h localhost -u user1 -p
- 



workspace 생성

- create database shop;
- USE shop



TABLE 작성

- ```
  CREATE TABLE PRODUCT(
  	ID INT PRIMARY KEY,
  	NAME NVARCHAR(20) NOT NULL,
  	PRICE INT NOT NULL,
  	REGDATE DATE
  );
  ```

- ```
  INSERT INTO PRODCUT VALUES (100, 'pants1',10000, SYSDATE());
  ```

  - TABLE 이름 대소문자 구분 !!
  - SYSDATE는 함수로 사용한다.

### Maria DB

1. Query 문 새로작성
   - DDL
   - DML - squence
2. Spring MVC
   - MariaDB JDBC 설치
     - maven
   - Spring 환경설정
3. Mybatis Mapper 작업
   - XML





##### 하드디스크 추가하기 

VMware 는 두가지 종류의 장치 사용가능

1. IDE(PC)
   - 백업 
2. SCSI (Server)



과정

1. Add를 눌러 Harddisk 를 선택하고 추가
2. 1기가 추가 
3. specify disk file
   1. scsi0-1



설정

1. ls - l /dev/sd*

   1. 일단 추가된 하드디스크 이름 검색

2. ```
   fdisk /dev/sdb
   Command :n
   Select :p
   Partition number : 1
   First sector : enter
   Last sector : enter
   
   ```

3. 마운트 및 마운트 유지하기

   - mkdir /mydata

   - mount /dev/sdb1 /mydata

   - vi /etc/fstab 

   - ```
     /dev/sdb1 /mydata ext4 defaults 1 2
     ```

4. 장치 제거

   1. fstab에 마운트 설정해 놓은 것 부터 제거 한다.

      - ```
        vi /etc/fstab
        
        # 주석으로 막거나 
        dd 로 삭제
        실수 하면 q! 로 저장안하고 나가거나
        u 를 눌러 undo 하기
        ```

      - 

   2. 물리적으로 HD를  제거한다



RAID & LVM

여러 하드디스크를 하나의 하드디스크 처럼 사용할 수 있게 만들 수 있음.

하드웨어 RAID

소프트웨어 RAID



RAID 종류

- linear
  - 두개 하드디스크 사용 하나 꽉차면 다른하나 사용하기 시작
  - 뻥나면 쥐쥐 (파일이 첫번째 하드디스크보다 작다면 살아있을 수도... 첫번째 하드가 뻥나면 쥐쥐)
- RAID0 
  - 두개의 하드디스크를 동시에 사용
  - 데이터가 두개의 하드디스크로 나눠서 들어가짐
  - 뻥나면 쥐쥐
- RAID1
  - 하드디스크 두개 동시에사용
  - 미러링
  - 하나는 백업용..  때문에 **용량을 반밖에 사용하지 못함**
- RAID5
  - RAID0 과 RAID1를 합쳐 개선한 것
  - 페리티 비트를 사용하여 백업도모
  - 3개이상의 하드디스크를 묶어야 함.
  - 3개중 하나가 고장나도 복구가능. 그러나 두개이상 고장나면 복구불가능





사전준비 

Edit virtual machine setting 에서 하드디스크 추가하기



Linear RAID 

1. 각각의 Disk fdisk - fd

2. mdadm - 디스크 묶기

   - ```
     mdadm --create /dev/md9 --level=linear --raid-devices=2 /dev/sdb1 /dev/sdc1
     ```

3. mkfs.ext4 -- ext4 방식으로 포멧

   - ```
     mkfs.ext4 /dev/md9
     ```

4. folder 생성 (linear)

   - ```
     mkdir /linear
     ```

5. mount 

   - ```
     mount /dev/md9 /linear
     ```

6.  /etc/fstab

   - ```
     vi /etc/fstab
     
     /dev/md9 /linear ext4 default 1 2
     ```

RAID0

- ```
  mdadm --create /dev/md0 --level=0 --raid-devices=2 /dev/sdd1 /dev/sde1
  ```

RAID1

- ```
  mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sdf1 /dev/sdg1
  ```

RAID5

- ```
  mdadm --create /dev/md5 --level=5 --raid-devices=2 /dev/sdh1 /dev/sdi1 /dev/sdk1
  ```

  

하드 고장내고 새로 추가하기

Edit virtual machine setting 에서 remove Hardisk 로 고의적으로 하드디스크 제거하기



- 부팅이 안되면 root 비밀번호 치고 터미널로 들어가기
  - 부팅이 안되는 이유는 /etc/fstab에 하드디스크를 자동으로 마운트 시키는데 하드디스를 못찾기 때문.
  - 따라서 vi /etc/fstab 로 fstab에 접근 후 해당 라인 주석처리 / 삭제

- linear 나 RAID0 은 회생불가

- RAID 1 이랑 RAID 5는 회생가능 하므로

  - ```
    mdadm --run /dev/md1
    mdadm --run /dev/md5
    
    을 입력하여 RAID 실행
    
    ls /raid1
    ls /raid5
    를 통해 파일이 살아있는 것을 확인.
    ```

  - 

새로운 하드디스크 추가하여 RAID 복구하기

Edit virtual machine setting에서 새로운 하드디스크 를 추가

- SCSI 포트넘버는 상관없음



일단 실행되고 있는 RAID를 STOP

- ```
  mdadm --stop /dev/md9
  mdadm --stop /dev/md0
  ```

새로 RAID 생성

- ```
  mdadm --create /dev/md9 --level=linear --raid-devices=2 /dev/sdb1 /dev/sdc1
  ```

새로 마운트를 걸어줘도 보이는 파일은 손상된 파일이므로 미리 포멧 진행

- ```
  mkfs.ext4 /dev/md9
  ```

새로 마운트

- ```
  mount /dev/md9 /linear
  ```

잘 돌아가는지 확인

- df
  - 동작하고 있는 device를 나열해줌
- mdadm --detail /dev/md9
  - /dev/md9 ( linear raid ) 의 상세정보를 확인.



RAID 1 / RAID 5 복구 (ADD)

- ```
  mdadm /dev/md1 --add /dev/sdg1
  ```

- 





LVM (Logical Volume Manager)

- 두개를 붙여서 여러개 만들기 가능
  - ex) 사용자에게 dir를 할당할 수 있음.



- 생성 절차

  1. fdisk 설정 

     - Type of Partition = Linux LVM

     - Hex Code = 8e

  2. 물리적 볼륨 생성

     - ```
       pvcreate /dev/sdb1
       pvcreate /dev/sdc1
       ```

  3. 물리적 볼륨 하나로 묶기

     - ```
       vgcreate myVG /dev/sdb1 /dev/sdc1
       ```

  4. vgdisplay로 상태확인

  5.  볼륨 그룹의 파티션 나누기

     - ```
       lvcreate --size 1G --name myLG1 myVG
       lvcreate --size 3G --name myLG2 myVG
       lvcreate --extents 100%FREE --name myLG3 myVG
       ```

     - 마지막줄은 용량이 정확하게 나뉘어지지 않기 때문에 나머지를 다 myLG3로 넣으라는 뜻임

  6. 디바이스 포멧

     - ```
       mkfs.ext4 /dev/myVG/myLG1
       mkfs.ext4 /dev/myVG/myLG2
       mkfs.ext4 /dev/myVG/myLG3
       ```

  7. 마운트 할 디렉토리 생성 및 마운트

     - ```
       mkdir /lvm1
       mkdir /lvm2
       mkdir /lvm3
       ```

     - ```
       mount /dev/myVG/myLG1 /lvm1
       mount /dev/myVG/myLG2 /lvm2
       mount /dev/myVG/myLG2 /lvm3
       ```

     - vi /etc/fstab 에서 설정

     - ```
       /dev/myVG/myLG1 /lvm1 ext4 defaults 1 2
       /dev/myVG/myLG2 /lvm2 ext4 defaults 1 2
       /dev/myVG/myLG3 /lvm3 ext4 defaults 1 2
       ```




### 최소설치 모드

- 텍스트 모드로 부팅.  UI가 없음.

- 여러가지 tool을 yum으로 다운로드 받아야 함.

  - ```
    yum -y install wget
    yum -y install 
    ```







### 셸 스크립트

커널을 통해서 하드웨어를 조종.

커널에서 HW에 있는 내용을 조회 할 수 있음.

이런 커널을 명령을 전달하는 부분이 셸.

CentOS 

- bash shell 사용. ( 가장 최신 버전임)



bash shell

- Alias 기능 (명령어 단축 기능)
- History
- 연산
- Job Control
- 자동 이름 완성
- 프롬프트 기능
- 명령 편집기능.



명령어

- echo
  - 자바로 치면 sysout
  - ex)  echo $JAVA_HOME
- printenv
  - 환경정보 보기



셸 스크립트 프로그래밍 (script language)

```
mkdir shell
cd shell 

```



Shell Script에서 숫자도 모조리 다 String이다.

```
#!/bin/sh
echo "Input number..?"
read v1 v2
echo "Input number is " $v1 $v2
echo "Input number is $v1 $v2"
exit 0
```

- $v1은 자바 스크립트의 이엘 변수랑 비슷하다. "" 안에서도 변수값을 가짐



연산

Input 받기 

1. read 사용

   - ```
     read v1
     read v2
     sum1=`expr $v1 + $v2`
     ```

   - equal(=) 부호는 양옆에 붙여서 쓴다.

   - 연산은 맨 앞과 끝에 `를 붙이고  앞에 expr를 쓴다.

   - 괄호 (  ) 및 * 연산 같은경우 \ 를 붙여서 다른 기호와 구별해준다

2.  parameter 사용

   - ```
     para3.sh /root sh /shfile
     
     $0 은 para3.sh 
     $1 /root
     $2 sh
     $3 /shfile
     
     이런식으로 감
     
     ```

   - 