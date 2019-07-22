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







