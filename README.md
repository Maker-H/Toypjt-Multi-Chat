[socket 공식 문서](https://docs.python.org/ko/3/library/socket.html#socket.AF_INET)

class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
지정된 주소 패밀리, 소켓 유형, 및 프로토콜 번호를 사용하여 새로운 소켓을 만듭니다. 주소 패밀리는 AF_INET (기본값), AF_INET6, AF_UNIX, AF_CAN, AF_PACKET 또는 AF_RDS 여야 합니다. 소켓 유형은 SOCK_STREAM (기본값), SOCK_DGRAM, SOCK_RAW 또는 기타 SOCK_ 상수 중 하나여야 합니다. 프로토콜 번호는 일반적으로 0이며 생략될 수도 있고, 주소 패밀리가 AF_CAN 일 때 프로토콜은 CAN_RAW, CAN_BCM, CAN_ISOTP 또는 CAN_J1939 중 하나여야 합니다.