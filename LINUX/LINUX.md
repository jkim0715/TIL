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



사용자관리 명령어

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





링크

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



파일 다운로드

YUM

- yum -y install 패키지이름
  - 패키지이름
- yum localinstall rpm파일이름.rpm
- yum groupinstall "패키지 그룹 이름"
  - 패키지 그룹이름은 자기가 직접 서치해야함.

RPM







시스템 전역변수 설정

- vi /etc/profile

  - ```
    JAVA_HOME=/etc/jdk1.8
    export JAVA_HOME
    CLASSPATH=$JAVA_HOME/lib
    export CLASSPATH
    PATH=.:JAVA_HOME/bin:$PATH
    ```

    



Eclipse 설치하기

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

Tomcat 9.0 설치하기

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