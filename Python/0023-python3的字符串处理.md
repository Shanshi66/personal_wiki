# py3的字符串处理

1. python3中的str字符串保存的是Unicode码位，python2中是字节字符串

2. python3中用bytes类型处理字节字符串

3. 字节字符串只能保存ascii码

4. bytearray可以存变长字符串，支持append，pop，insert方法

5. str.encode(encoding, errors)将字符串转为字节序列, encoding默认是utf-8, errors指定对错误的处理方法。或者使用bytes构造函数bytes(source, encoding, errors)

6. bytes.decode(encoding, errors)对字节序列进行解码, 或者, str(source, encoding, error)