# pyvernam
Vernam's cipher implementation for Python 3, written to be (hopefuly) fast and easily scriptable.

If the key is longer than the plaintext, padding is applied. If it's shorter, an exception is raised. Plaintext is normalized to upper case. For each out-of-dictionary character, a random value is generated to ensure randomness instead of a fixed default value.

Supported alphabet:
```{0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: '0', 27: '1', 28: '2', 29: '3', 30: '4', 31: '5', 32: '6', 33: '7', 34: '8', 35: '9', 36: ' '}```

Usage:
```./vernam.py: gen|enc|dec (otp_lines_num otp_name)|(plaintext key)|(cryptotext key)```

# Examples
 - ```./vernam.py gen 10 otp.txt``` - generate one-time pad with 10 lines of 50 random alphanumeric characters each.
 - ```./vernam.py enc 'alice bob' 'BLAHBLAHBLAH'``` - encrypt ```'alice bob'``` with ```'BLAHBLAHBLAH'``` key.
 - ```./vernam.py dec ' AI6DZBHAZ 3' 'BLAHBLAHBLAH'``` - decrypt ```' AI6DZBHAZ 3'``` with ```'BLAHBLAHBLAH'``` key.
 - OTP example:
 ```
ZNIK483YDN4BDGYTFVJ58X6R1Z7J4IM5AQQFFYJ0KM2KG35U3K
227624RB2ZGQB80MXQVQBL3K41KLHBC1BKSEAE3F8L8LAD0NWN
QTPT3PDG24TGA4LG5ZFKIBFSLFQ2TTNMB9HJLQCWNJCRF80WKN
CRUGB5G06LFJTDCO6PC7C47OBTVE63WDR3FHE5NFHMYUYR0GW4
P33H1K2GERXOI19AVWMQWWNRDFJS3GCZ76ERZ5ZGGG38IVW6L8
R1ZSY7EMB631IEG6AOQLJGQZNJ30T3AIMY51QXYKIM5PJACO15
8L82DD2ZX9ZBLP01E8LDB59IUR2GD1FW8JRRKHBMBDCXBKQGNV
UQICLQZ5CYMDRE13GCZ2FY3CG1OEE7A5MJB3U8U6HASHCDJZAI
F1DTQGYVPSD4J02NPDKYDO9I1B3AVYBNMPXREIFIIPDCAYL5HS
J23OZQJ8RL4LDI0PUC6FC1BSKLMKYLJKWR4OSYZTLAOFKW5HD8
```
