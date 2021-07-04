import hashlib

result = hashlib.md5('Hello World'.encode())
print("Hash Value:",end="")
print(result)
print("Hexadecimal Equivalent : ",end="")
print(result.hexdigest())