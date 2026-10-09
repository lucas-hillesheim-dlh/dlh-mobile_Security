from base64 import b64decode

enc_flag = b64decode('cVZaW1dDQllZTFdRW1xeUlBbX21CWFtHalRZXUJFRFhNX1ZcbllGQ15cUUNSRFpcVks=')
key = '9969216677189303386214405760200' # 150th Fibonacci value

for i in range(len(enc_flag)):
    print(chr(ord(key[i % len(key)]) ^ enc_flag[i]), end="")
