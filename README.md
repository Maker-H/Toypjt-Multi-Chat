[socket 공식 문서](https://docs.python.org/ko/3/library/socket.html#socket.AF_INET)

### 결과

![image](https://github.com/Maker-H/Study-Algorithm-baekjun/assets/83294376/8fe81f77-cac9-4dfb-89a0-401a3ad75b31)

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

### 소켓 생성
- socket.AF_INET은 IPv4 주소 체계를 사용한다는 뜻이고 socket.SOCK_STREAM은 TCP 소켓을 의미
```
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP Socket 만들기
```

### 클라이언트와 소켓 연결
- 서버는 소켓을 만들고 count = count + 1까지 실행한 상태에서 server_sock.accept()를 만나면 클라이언트의 연결 요청이 수락되기 전까지 blocked 상태로 대기
- server_sock는 서버의 소켓 객체로 클라이언트의 접속을 위한 엔드포인트로서 역할을 수행 
- conn은 실제로 클라이언트와 통신을 담당하는 객체 
```
count = 0
while True:
    count = count + 1
    conn, addr = server_sock.accept()  # 해당 소켓을 열고 대기
    group.append(conn) #연결된 클라이언트의 소켓정보
    print('Connected ' + str(addr))

```

###  클라이언트와 소켓으로 데이터 송수신
- 클라이언트가 1명일 경우 다른 클라이언트가 없음으로 브로드캐스트 하지 않아도 됨
- 클라이언트가 1명 이상일 경우 다른 클라이언트에게 브로드캐스트 해야함
- thread를 실행시킨 이후 send_queue가 비어있는 경우 get()은 blocked 상태로 대기 
- thread1~5에게서 데이터 수신 받아서 send_queue에 데이터가 차있다면 get()이 실행
```
def Send(group, send_queue):
    while True:
        try:
            recv = send_queue.get()

if count > 1:
    send_queue.put('Group Changed')
    thread = threading.Thread(target=Send, args=(group, send_queue,))
    thread.start()
    pass
else:
    thread = threading.Thread(target=Send, args=(group, send_queue,))
    thread.start()

thread1 = threading.Thread(target=Recv, args=(conn, count, send_queue,))
thread1.start()
```

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