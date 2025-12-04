from Config.settings import FACE_COLS, FACE_ROWS

def _blank_face():
    return [[0 for _ in range(FACE_COLS)] for _ in range(FACE_ROWS)]

def _center():
    mid_y = FACE_ROWS // 2
    mid_x = FACE_COLS // 2
    return mid_x, mid_y

def happy_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 3][mid_x + 5] = 1
    face[mid_y - 2][mid_x - 5] = 1
    face[mid_y - 2][mid_x + 5] = 1

    for dx in range(-4, 5):
        face[mid_y + 3][mid_x + dx] = 1
    face[mid_y + 2][mid_x - 3] = 1
    face[mid_y + 2][mid_x + 3] = 1

    return face

def sad_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 3][mid_x + 5] = 1

    for dx in range(-4, 5):
        face[mid_y + 4][mid_x + dx] = 1
    face[mid_y + 5][mid_x - 3] = 1
    face[mid_y + 5][mid_x + 3] = 1

    return face

def surprised_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    for dy in (-3, -2):
        face[mid_y + dy][mid_x - 5] = 1
        face[mid_y + dy][mid_x + 5] = 1

    mouth_y = mid_y + 2
    face[mouth_y][mid_x] = 1
    face[mouth_y - 1][mid_x] = 1
    face[mouth_y][mid_x - 1] = 1
    face[mouth_y][mid_x + 1] = 1
    face[mouth_y + 1][mid_x] = 1

    return face

def empathetic_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 2][mid_x - 4] = 1
    face[mid_y - 3][mid_x + 5] = 1
    face[mid_y - 2][mid_x + 4] = 1

    for dx in range(-3, 4):
        face[mid_y + 3][mid_x + dx] = 1
    face[mid_y + 2][mid_x - 2] = 1
    face[mid_y + 2][mid_x + 2] = 1

    return face


def confused_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    face[mid_y - 4][mid_x - 6] = 1
    face[mid_y - 4][mid_x - 5] = 1
    face[mid_y - 4][mid_x - 4] = 1

    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 3][mid_x + 5] = 1

    for dx in range(-3, 4):
        face[mid_y + 3][mid_x + dx + (dx // 3)] = 1

    return face

def sleeping_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    def set_pixel(x, y):
        if 0 <= x < FACE_COLS and 0 <= y < FACE_ROWS:
            face[y][x] = 1
    left_cx = mid_x - 4
    left_ey = mid_y - 2

    for dx in range(-3, 4):      
        set_pixel(left_cx + dx, left_ey)
        set_pixel(left_cx + dx, left_ey + 1)

    right_cx = mid_x + 4
    right_ey = mid_y - 2

    for dx in range(-3, 4):
        set_pixel(right_cx + dx, right_ey)
        set_pixel(right_cx + dx, right_ey + 1)

    mouth_y = mid_y + 3
    for dx in range(-2, 3):
        set_pixel(mid_x + dx, mouth_y)

    z_x = FACE_COLS - 6  
    z_y = 2

    for dx in range(0, 3):
        set_pixel(z_x + dx, z_y)

    set_pixel(z_x + 2, z_y + 1)

    for dx in range(0, 3):
        set_pixel(z_x + dx, z_y + 2)

    return face

EMOTION_FACES = {
    "happy": happy_face,
    "sad": sad_face,
    "surprised": surprised_face,
    "empathetic": empathetic_face,
    "confused": confused_face,
    "sleeping": sleeping_face,  
}
