class Piece:
    piece = []
    maxState = None

    def __init__(self):
        self.state = 0

    def getWidth(self):
        return self.piece[self.state]['width']

    def getHeight(self):
        return self.piece[self.state]['height']

    def getBody(self):
        return self.piece[self.state]['represantation']

    def getSkirt(self):
        return self.piece[self.state]['skirt']

    def rotate(self):
        self.state += 1

        if(self.state > self.maxState):
            self.state = 0

        return self.piece[self.state]['represantation']

class I(Piece):
    '''
    state 0:
    oooo
    oooo
    oooo
    xxxx
    
    state 1:
    xooo
    xooo
    xooo
    xooo
    '''

    piece = [
        {
            'height': 1,
            'width': 4,
            'skirt': [0,0,0,0],
            'represantation': ((0,0), (1,0), (2,0), (3,0))
        },
        {
            'height': 4,
            'width': 1,
            'skirt': [0],
            'represantation': ((0,0), (0,1), (0,2), (0,3)),
        },
    ]

    maxState = 1

    def __init__(self):
        super().__init__()

class O(Piece):
    '''
    state 0:
    oooo
    oooo
    xxoo
    xxoo
    '''

    piece = [
        {
            'height': 2,
            'width': 2,
            'skirt': [0,0],
            'represantation': ((0,0), (0,1), (1,0), (1,1))
        },
    ]

    maxState = 0

    def __init__(self):
        super().__init__()

class J(Piece):
    '''
    state 0:
    oooo
    oooo
    xooo
    xxxo

    state 1:
    oooo
    oxoo
    oxoo
    xxoo

    state 2:
    oooo
    oooo
    xxxo
    ooxo

    state 3:
    oooo
    xxoo
    xooo
    xooo
    '''

    piece = [
        {
            'height': 2,
            'width': 3,
            'skirt': [0,0,0],
            'represantation': ((0,0), (1,0), (2,0), (0,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [0,0],
            'represantation': ((0,0), (1,0), (1,1), (1,2))
        },
        {
            'height': 2,
            'width': 3,
            'skirt': [1, 1, 0],
            'represantation': ((2,0), (0,1), (1,1), (2,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [0, 2],
            'represantation': ((0,0), (0,1), (0,2), (1,2))
        },
    ]

    maxState = 3

    def __init__(self):
        super().__init__()

class L(Piece):
    '''
    state 0:
    oooo
    xooo
    xooo
    xxoo

    state 1:
    oooo
    oooo
    ooxo
    xxxo

    state 2:
    oooo
    xxoo
    oxoo
    oxoo

    state 3:
    oooo
    oooo
    xxxo
    xooo
    '''

    piece = [
        {
            'height': 3,
            'width': 2,
            'skirt': [0,0],
            'represantation': ((0,0), (1,0), (0,1), (0,2))
        },
        {
            'height': 2,
            'width': 3,
            'skirt': [0,0,0],
            'represantation': ((0,0), (1,0), (2,0), (2,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [2, 0],
            'represantation': ((1,0), (1,1), (0,2), (1,2))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [0, 1, 1],
            'represantation': ((0,0), (0,1), (1,1), (2,1))
        },
    ]

    maxState = 3

    def __init__(self):
        super().__init__()

class T(Piece):
    '''
    state 0:
    oooo
    oooo
    xxxo
    oxoo

    state 1:
    oooo
    oxoo
    xxoo
    oxoo

    state 2:
    oooo
    oooo
    oxoo
    xxxo

    state 3:
    oooo
    xooo
    xxoo
    xooo
    '''

    piece = [
        {
            'height': 2,
            'width': 3,
            'skirt': [1,0,1],
            'represantation': ((1,0), (0,1), (1,1), (2,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [1,0],
            'represantation': ((1,0), (0,1), (1,1), (1,2))
        },
        {
            'height': 2,
            'width': 3,
            'skirt': [0,0,0],
            'represantation': ((0,0), (1,0), (2,0), (1,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [0, 1],
            'represantation': ((0,0), (0,1), (1,1), (0,2))
        },
    ]

    maxState = 3

    def __init__(self):
        super().__init__()

class S(Piece):
    '''
    state 0:
    oooo
    oooo
    oxxo
    xxoo

    state 1:
    oooo
    xooo
    xxoo
    oxoo
    '''

    piece = [
        {
            'height': 2,
            'width': 3,
            'skirt': [0,0,1],
            'represantation': ((0,0), (1,0), (1,1), (2,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [1,0],
            'represantation': ((1,0), (0,1), (1,1), (0,2))
        },
    ]

    maxState = 1

    def __init__(self):
        super().__init__()

class Z(Piece):
    '''
    state 0:
    oooo
    oooo
    xxoo
    oxxo

    state 1:
    oooo
    oxoo
    xxoo
    xooo
    '''

    piece = [
        {
            'height': 2,
            'width': 3,
            'skirt': [1,0,0],
            'represantation': ((1,0), (2,0), (0,1), (1,1))
        },
        {
            'height': 3,
            'width': 2,
            'skirt': [0,1],
            'represantation': ((0,0), (0,1), (1,1), (1,2))
        },
    ]

    maxState = 1

    def __init__(self):
        super().__init__()