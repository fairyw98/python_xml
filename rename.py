# -*- coding:utf8 -*-

import os

class BatchRename():
    '''
    批量重命名当前文件夹中的图片文件

    '''
    def __init__(self):
        self.path = os.getcwd()
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        n = 6
        for item in filelist:
            if item.endswith('.jpg') or  item.endswith('.jpeg') :
        	n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0)*n + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print( 'converting %s to %s ...' % (src, dst))
                    i = i + 1

                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
