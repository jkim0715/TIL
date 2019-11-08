## CAN Program

## I. 라이브러리 준비

- RXTXcomm.jar

  Java와 Serial로 통신하기 위해 만들 Lib

  JDBC는 Listener만 있으면 됐기 때문에 jar file만 있으면 됐지만

  CAN은 Serial로 통신하기 위해  native한 프로그램이 있어야 함.

  (rxtxParallel.dll, rxtxSerial.dll)

- C:\Program Files\Java\jre1.8.0_221\bin 에 dll파일 넣어두기.

  - rxtxParallel.dll
  - rxtxSerial.dll
  - dll 은 C로 짠거임,,, C랑 연결 가능.



## II. 구조

### App - Serial - CAN

- APP은 CAN을 모름
- 실시간 통신이 아님 
- APP에서 데이터를 송신할 때 Serial이 busy할 경우 CAN으로 전송되는 데이터가 늦어질 수 있음. vice versa.

### Serial 통신

App에서 10byte를 여러개 보내지만 Serial은 보낼때 8byte, 7byte씩 보냄... 멍청..

때문에 통신 할 때 시작과 끝을 같이 보내줘서 데이터를 올바르게 인식하도록 함..

### App 

이벤트리스너를 만들어서, Serial에서 데이터 들어올 때만 Event를 발생, 감지하여 동작.



### 데이터(메세지) 구조

EX) U281FFFFFFFA111111111111111FA

HAED(U28) + ID(1FFFFFFF)+데이터(A111111111111111) + CheckSum(FA)

U28 : 내가 지금 받겠다는 의미.

EX) :W28 00000000 000000000000 53 \r

W28: 내가 지금 보내겠다는 의미

CheckSum : 자체 계산으로 만든 암구호 같은거임.



