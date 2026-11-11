from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    decode_access_token
)


def test_password_hashing():
    password = "TestPass123!"
    hashed = get_password_hash(password)

    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("WrongPassword", hashed)


def test_create_and_decode_token():
    token = create_access_token({"sub": "testuser"})
    decoded = decode_access_token(token)

    assert decoded["sub"] == "testuser"
    assert "exp" in decoded
