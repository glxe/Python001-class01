# 需要先安装图片依赖库 libpng，jpeg，libtiff，leptonica
# mac系统使用brew install libpng jpeg libtiff leptonica
# 安装图片文字处理工具 Tesseract
# // 安装tesseract的同时安装训练工具

# brew install --with-training-tools tesseract

# // 安装tesseract的同时安装所有语言，语言包比较大，如果安装的话时间较长，建议不安装，按需选择

# brew install --all-languages tesseract

# // 安装tesseract，并安装训练工具和语言

# brew install --all-languages --with-training-tools tesseract

# // 只安装tesseract，不安装训练工具

# brew install tesseract

# 然后还需要安装支持python的库，pip3 install Pillow pytesseract

import requests
import os
import pytesseract
from PIL import Image

codeUrl = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2282030598,1303150352&fm=26&gp=0.jpg'
header = {
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
r = requests.get(codeUrl, headers = header)

with open('code.jpeg', 'wb') as f:
    f.write(r.content)


# 打开文件
im = Image.open('code.jpeg')
# im.show()

# 灰度处理
gray = im.convert('L')
gray.save('code_gray.jpeg')
im.close()

# 二值化
th = 120
table = []
for i in range(256):
    if i < th:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('code_th.jpeg')

th = Image.open('code_th.jpeg')

codeStr = pytesseract.image_to_string(th, lang = 'eng')
th.close()
print(codeStr)