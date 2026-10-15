# Report

## Decompile APK

Use Jadx to decompile the APK and read the code. After some reading on the *MainActivity* and *MainActivityKt* there is a function named *aBcDeFgHiJkLmNoPqRsTuVwXyZ123456* that is called when the app opens.

I ported the routine to Python and ran it on the Base64 string. For each byte at index i, the steps are:

- Base64-decode the string into bytes.
- XOR the byte with 19.
- Rotate the result right by 2 bits within 8 bits, which is ((t >> 2) | (t << 6)) & 255.
- Subtract i * 3 and take the result mod 256.
- Multiply by 183 and take the result mod 256 to get the character.
