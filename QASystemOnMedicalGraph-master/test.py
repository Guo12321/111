import os
import codecs
import chardet


#对该文件夹下包括子文件夹的所有文件进行遍历
"path_in = r'D:\**'"
path_in = r'C:\Users\86181\Desktop\QASystemOnMedicalGraph-master\model'
#需要转换成GBK编码
codec_out = 'GBK'
for home, dirs, files in os.walk(path_in):
    for filename in files:
        #只转换matlab脚本文件
        if filename.endswith('.m'):
            #home为文件所在文件夹的路径，filename为文件名
            file = os.path.join(home, filename)

            #检测文件原来的编码格式
            with open(file, "rb") as f_in:
                data = f_in.read()
                codec_in = chardet.detect(data)['encoding']

            #将文件旧编码格式转换为UTF-8，并写入原文件完成替换
            try:
                with codecs.open(file, 'r', codec_in) as f_in:
                    new_data = f_in.read()
                    f_out = codecs.open(file, 'w', codec_out)
                    f_out.write(new_data)
                    f_out.close()
            except IOError as err:
                print("I/O error: {0}".format(err))