## CAN 통신  Intro

### I. 실습

- 실제 자동차 없이 컴퓨터를 이용해 테스트

- 전송하는 데이터를 CAN버스에 물려있는 모든 ECU가 응답.

  ![CANpro시작](https://user-images.githubusercontent.com/50862254/65656601-643ee500-e05b-11e9-8970-edf7f190e784.png)

### II. 연결

High - High

Low - Low

컴퓨터랑 연결 할 때는, USB로 인식시키고 , CAN장비를 가상의 Serial로 연결할 수 있도로 하는 드라이버 각각 두개 설치. ( USB로 연결되어 있지만 Serial로 인식하도록 만들어 줌)

실제 자동차랑 연결할 땐 USB로 연결하지 않고 Serial로 연결 함.

 Comm Port는 Serial 과 Parallel 로 나뉨

### III. 설치

1. 드라이버 설치

   1. CAN장비 연결

      ```
      제어판 > 하드웨어 및 소리 > 장치관리자를 확인하면
      기타장치 > CANPro Analyzer가 
      노란색 느낌표가 표시된 상태로 등록된것을 볼 수 있다.
      ```

      ![USB연결](https://user-images.githubusercontent.com/50862254/65656673-acf69e00-e05b-11e9-89d2-74ea1083d0f8.png)

   2. dp-chooser 실행

      ```
      개발툴용 USB Device Driver를 설치한다. 
         설치가 완료되면 노란색 느낌표가 있던 기타장치는
         사라지고
         장치관리자 > 포트 부분에 CANPro가 등록된걸 
         확인할 수 있다.
      ```

   3. 연결확인 

      ```
      CANPro_v1.4.exe를 실행, 설치하여 analyzer프로그램을
      설치하고 실행시켜 동작을 확인한다.
      ```

      ![데이터 송수신](https://user-images.githubusercontent.com/50862254/65656752-ea5b2b80-e05b-11e9-8f20-ba1bc0f6bcf1.png)

      3-1. 여러개 연결

      ```
      CANPro를 하나 더 준비하여 서로 Serial로 연결한 후 각 PC에 연결하면 장치관리자 > 포트 부분에 USB Serial Port가 하나 더 잡히는걸 확인할 수 있다. 이제 analyzer를 2개 실행해서 serial com포트를 각기 다른 port번호로 설정한 후 로 데이터 통신을 할 수 있는지를 확인한다.
      ```

      ![4대연결(2)](https://user-images.githubusercontent.com/50862254/65656725-d1eb1100-e05b-11e9-817b-98cd72a89370.png)

2. CAN pro Analyzer 설치

   ![CANpro시작](https://user-images.githubusercontent.com/50862254/65656601-643ee500-e05b-11e9-8970-edf7f190e784.png)

   1. 환경설정.

      CAN장비들끼리 환결설정이 일치해야 데이터를 송 수신 가능. (EX Serial 전송속도, 프로토콜, CAN BPS)

      ![환경설정](https://user-images.githubusercontent.com/50862254/65656851-43c35a80-e05c-11e9-9272-2be16c842d6f.png)

      

### IV. CAN protocol

1. 데이터 사이즈 설정

   1. 명령부 데이터부	

      회사들마다 각기 다르게 다 정함.

   2. 명령부

      Hex 코드 (8진수)

      CAN protocol은 데이터 사이즈가 정해져 있기 8진수를 사용해서 더 다양한 종류의 데이터를 주고받을 수 있음.

   3. 데이터부

      

### V. 데이터 송수신

CAN은 송수신 동시에 가능.

1. 수신부 

   수신준비

2. 송신부 

   1. 송신 데이터 설정

대신 한개의 포트는 한개의 CAN Proanalyzer만 사용 가능.

ODB

1. 속도, RPM, 온도 등 기본적인 gerneral한 Protocol을 