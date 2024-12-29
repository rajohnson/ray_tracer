from vec3 import Vec3


def test_add():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = v1 + v2
    assert v3.x == 5
    assert v3.y == 7
    assert v3.z == 9

    # iadd
    v3 += Vec3(1, 1, 1)
    assert v3.x == 6
    assert v3.y == 8
    assert v3.z == 10


def test_sub():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = v1 - v2
    assert v3.x == -3
    assert v3.y == -3
    assert v3.z == -3

    # isub
    v3 -= Vec3(1, 1, 1)
    assert v3.x == -4
    assert v3.y == -4
    assert v3.z == -4


def test_neg():
    v1 = Vec3(1, 2, 3)
    v2 = -v1
    assert v2.x == -1
    assert v2.y == -2
    assert v2.z == -3


def test_getitem():
    v1 = Vec3(1, 2, 3)
    assert v1[0] == 1
    assert v1[1] == 2
    assert v1[2] == 3


def test_setitem():
    v1 = Vec3(1, 2, 3)
    v1[0] = 4
    v1[1] = 5
    v1[2] = 6
    assert v1.x == 4
    assert v1.y == 5
    assert v1.z == 6


def test_iter():
    v1 = Vec3(1, 2, 3)
    for i, e in enumerate(v1):
        assert e == v1[i]


def test_properties():
    v1 = Vec3(1, 2, 3)
    assert v1.x == 1
    assert v1.y == 2
    assert v1.z == 3

    v1.x = 4
    v1.y = 5
    v1.z = 6
    assert v1.x == 4
    assert v1.y == 5
    assert v1.z == 6


def test_index_error():
    v1 = Vec3()
    try:
        v1[3]
    except IndexError as e:
        assert str(e) == "Index out of range"
    else:
        assert False

    try:
        v1[4] = 3
    except IndexError as e:
        assert str(e) == "Index out of range"
    else:
        assert False


def test_equality():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(1, 2, 3)
    assert v1 == v2

    v2.x = 4
    assert v1 != v2


def test_mul():
    v1 = Vec3(1, 2, 3)
    v2 = v1 * 2
    assert v2.x == 2
    assert v2.y == 4
    assert v2.z == 6

    v2 = 2 * v1
    assert v2.x == 2
    assert v2.y == 4
    assert v2.z == 6

    v3 = v1 * Vec3(1, 2, 3)
    assert v3.x == 1
    assert v3.y == 4
    assert v3.z == 9

    v1 *= 2
    assert v1.x == 2
    assert v1.y == 4
    assert v1.z == 6

    v1 *= Vec3(1, 2, 3)
    assert v1.x == 2
    assert v1.y == 8
    assert v1.z == 18


def test_div():
    v1 = Vec3(2, 4, 6)
    v2 = v1 / 2
    assert v2.x == 1
    assert v2.y == 2
    assert v2.z == 3

    v1 /= 2
    assert v1.x == 1
    assert v1.y == 2
    assert v1.z == 3


def test_length():
    v1 = Vec3(2, 4, 4)
    assert v1.length() == 6

    v1 = Vec3(2, 4, 4)
    assert v1.length_squared() == 36


def test_dot():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    assert v1.dot(v2) == 32


def test_cross():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = v1.cross(v2)
    assert v3.x == -3
    assert v3.y == 6
    assert v3.z == -3
