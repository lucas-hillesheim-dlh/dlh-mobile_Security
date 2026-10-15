# Report

## Decompile APK

Use Jadx to decompile the APK and read the code. After some reading on the *MainActivity* and *MainActivityKt* there is a function named *getSecretMessage* that is loaded from *native-lib*.

Checking the resoources for the APK I found the *libnative-lib.so*.

## Disassemble library

Using the GHidra to disassemble the library there are two functions named *getSecretMessage* and *lit*.
After reading how the code worked, I created a python version for that same code:

```py
enc_flag = bytes.fromhex('48706d6468777c7c839d6e62756b796a677584916b6a6f69626e7b6c83915f656a68696a7a7283965f6275616471748a')

def getSecretMessage():
    flag = ""
    for i in range(48):
        offset = lit(i % 10)
        flag += chr(enc_flag[i] - offset)
    return flag

def lit(number):
    if (number < 2):
        return number
    
    var1 = 0
    var2 = 1
    temp = 0
    for i in range(2,number + 1):
      temp = var1 + var2
      var1 = var2
      var2 = temp
    return temp

if __name__ == "__main__":
    flag = getSecretMessage()
    print(flag)
```

The encrypted flag was in the library code at address 0x10410, as referenced in the *getSecretMessage* function.


