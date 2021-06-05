class missingNameTypeError(SyntaxError):
    def __init__(self):
        super().__init__("변수, 함수, 클래스의 '이름' 이 없습니다")

class missingEOSError(SyntaxError):
    def __init__(self):
        super().__init__("'임' 혹은 '이고'가 없습니다")