# assetbundle.ksy
通过使用kaitai-struct配置描述unity assetbundle文件二进制结构，生成代码解析器提取assetbundle资源。

# 用法
1. 先安装kaitai-struct-compiler
2. 安装kaitai-struct py runtime
3. 编译assetbundle.ksy生成assetbundle.py

```
usage:
kaitai-struct-compiler assetbundle.ksy -t python
python extractbundle.py xxxx.assetbundle
```