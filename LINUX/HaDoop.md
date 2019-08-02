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



