[socket 공식 문서](https://docs.python.org/ko/3/library/socket.html#socket.AF_INET)

class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
지정된 주소 패밀리, 소켓 유형, 및 프로토콜 번호를 사용하여 새로운 소켓을 만듭니다. 주소 패밀리는 AF_INET (기본값), AF_INET6, AF_UNIX, AF_CAN, AF_PACKET 또는 AF_RDS 여야 합니다. 소켓 유형은 SOCK_STREAM (기본값), SOCK_DGRAM, SOCK_RAW 또는 기타 SOCK_ 상수 중 하나여야 합니다. 프로토콜 번호는 일반적으로 0이며 생략될 수도 있고, 주소 패밀리가 AF_CAN 일 때 프로토콜은 CAN_RAW, CAN_BCM, CAN_ISOTP 또는 CAN_J1939 중 하나여야 합니다.

<br><br>


### 쓰레드 생성
- target은 스레드가 실행할 함수를 지정, 여기서는 Send 함수가 스레드로 실행
- args로 target으로 지정한 함수에 전달할 인자 지정 
- 즉 Send(client_sock)를 실행하는 별도의 스레드가 만들어짐
```
thread1 = threading.Thread(target=Send, args=(client_sock, ))
thread1.start()
```
## 서버측

### 



<br><br>

## 클라이언트 측

### 문자열 인코딩 후 전송
- 문자열은 기본적으로 유니코드로 인코딩 해야하지만 네트워크 통신을 위해서는 바이트 형식으로 데이터를 전송해야하기 때문에 인코딩 해야함
- encode('UTF-8') 이렇게 전송할 수 있지만 ()로 비워놓으면 시스템 인코딩 방식을 따라감 sys.getdefaultencoding()으로 알아볼 수 있음
```
def Send(client_sock):
    while True:
        send_data = bytes(input().encode())
        client_sock.send(send_data)  # Client -> Server 데이터 송신
```


### 문자열 수신 후 디코딩
- client_sock.recv(1024)는 소켓에서 데이터가 수신되기 전까지 블로킹 상태로 있다가 데이터가 도착되면 프로그램이 실행됨
- 즉 서버에서 송신하기 전까진 cpu 측면에서 blocked 상태로 대기하게됨. (다른 작업을 수행하지 않고) 대기 큐에 머무르게 됨
```
def Recv(client_sock):
    while True:
        recv_data = client_sock.recv(1024).decode()  # Server -> Client 데이터 수신
        print(recv_data)
```