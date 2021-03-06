class missingNameTypeError(SyntaxError):
    def __init__(self):
        super().__init__("변수, 함수, 클래스의 '이름' 이 없습니다")

class missingEOSError(SyntaxError):
    def __init__(self):
        super().__init__("'임' 혹은 '이고'가 없습니다")

class missingThenError(SyntaxError):
    def __init__(self):
        super().__init__("'이면' 혹은 '라면'이 없습니다")

class missingEndError(SyntaxError):
    def __init__(self):
        super().__init__("'함' 혹은 '하고'가 없습니다")

class missingEORError(SyntaxError):
    def __init__(self):
        super().__init__("'반환함' 혹은 '반환하고'가 없습니다")

class missingEqualError(SyntaxError):
    def __init__(self):
        super().__init__("'은' 혹은 '는'이 없습니다")