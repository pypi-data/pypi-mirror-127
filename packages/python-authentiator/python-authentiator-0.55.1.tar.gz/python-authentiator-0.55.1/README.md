# python-authentiator

> TOTP based on python



Homepage: https://github.com/zzzzls/python_authentiator



```python
from python_authentiator import TOTP

g_auth = TOTP(
    origin_secret='123456',
    label='demo',
    account='example@gmail.com'
)

# 生成密钥
secret = g_auth.generate_secret()
# 生成一次性密码
print(g_auth.generate_code(secret))
# 生成二维码
print(g_auth.generate_qrcode(secret))
```

