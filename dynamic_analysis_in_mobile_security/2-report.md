# Report

## Decompile APK

Use Jadx to decompile the APK and read the code. After some reading on the *MainActivity* and *MainActivityKt* there is a function named *performslowDecryption* that is called when the app opens.

That function try to decrypt the flag calling the *slowRecursive* functiont that tries to calculate the 150th fibonacci to use as key for the decryption.

Reading the *xorDecrypt* function, it just do a simple XOR with the encrypted flag an the key. Using CyberChef to decode the flag that was in base64 and using the key with XOR function, the decrypted flag is found:

[CyberChef Recipe](https%3A%2F%2Fcyberchef.io%2F%23recipe%3DFrom_Base64%28%27A-Za-z0-9%252B%2F%253D%27%2Ctrue%29XOR%28%257B%27option%27%3A%27UTF8%27%2C%27string%27%3A%279969216677189303386214405760200%27%257D%2C%27Standard%27%2Cfalse%29%26input%3DY1ZaYVcxZERRbGxaVEZkUlcxeGVVbEJiWDIxQ1dGdEhhbFJaWFVKRlJGaE5YMVpjYmxsR1ExNWNVVU5TUkZwY1Zrcz0)

