#coding:utf-8
### V1.0版
### 针对xml文件，要修改的地方是<folder><path><width><height><bndbox>
### 程序瑕疵，在计算bud box时使用float格式，openCV画框函数为int格式
### 因此会产生误差
 
import os
import shutil
import os.path
import xml.dom.minidom

for num in range(1,77):
	src = 'C:\\Users\\Fairy\\Desktop\\000002.xml'
	dst = 'C:\\Users\\Fairy\\Desktop\\circle\\'+'000' + format(str(num), '0>3s')+'.xml'
	shutil.copyfile(src,dst) #复制源文件src到目的文件dst，注意，src和dst都是带文件

	#path="../xml/"
	path='C:\\Users\\Fairy\\Desktop\\circle'
	#files=os.listdir(path) #得到文件夹下所有文件名称
	#for xmlFile in files: #遍历文件夹
	xmlFile = dst
	if not os.path.isdir(xmlFile): #判断是否是文件夹，不是文件夹才打开
		print(xmlFile)
			
		#xml读取操作		
		#将获取到的xml文件名送入到dom解析
		#错误代码：dom=xml.dom.minidom.parse(xmlFile)
		dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
		root=dom.documentElement
	
		###获取标签对xmin/ymin之间的值
		# ~ folder=root.getElementsByTagName('folder')
		paths=root.getElementsByTagName('path')
		filenames=root.getElementsByTagName('filename')
		# ~ xmin=root.getElementsByTagName('xmin')
		# ~ ymin=root.getElementsByTagName('ymin')
		# ~ #修改相应标签的值
		# ~ # 修改<folder>
		# ~ for i in range(len(folder)):
			# ~ print folder[i].firstChild.data
			# ~ folder[i].firstChild.data='xml'
			# ~ print folder[i].firstChild.data
		for i in range(len(filenames)):
			#print(paths[i].firstChild.data)
			filenames[i].firstChild.data='000' + format(str(num), '0>3s')+".jpg"
			#print(paths[i].firstChild.data)
			fn = filenames[i].firstChild.data
		
		###############################################################################################################		
		### 如何修改path？每个xml文件对应不同名字的图片？？？                                                                
		### 解决方式如下，测试成功×----------->开始的思路有问题，                                                            
		###paths[i].firstChild.data='/home/kanghao/SSD-Tensorflow/yibiao512/JPEGImages/'+fn语句中，fn使用的是xmlFiles    
		###那么修改后的path中后缀加的是xml文件，不是对应的jpg文件。 思路2————————>直接读取filename标签中的值，添加到地址后即可     
		###############################################################################################################   
		# 修改<path>
		for i in range(len(paths)):
			#print(paths[i].firstChild.data)
			paths[i].firstChild.data='C:\\Users\\Fairy\\Desktop\\xml\\'+fn
			#print(paths[i].firstChild.data)
		# ~ # 修改<xmin>	
		# ~ for k in range(len(xmin)):
			# ~ print xmin[k].firstChild.data
			# ~ xia = unicode.encode(xmin[k].firstChild.data)
			# ~ xmin[k].firstChild.data=float(xia)/1.25
			# ~ print xmin[k].firstChild.data
		# ~ # 修改<ymin>	
		# ~ for j in range(len(ymin)):
			# ~ print ymin[j].firstChild.data
			# ~ yia = unicode.encode(ymin[j].firstChild.data)
			# ~ ymin[j].firstChild.data=float(yia)/1.0666667
			# ~ print ymin[j].firstChild.data
 
		#保存修改到xml文件中
		with open(os.path.join(path,xmlFile),'w') as fh:
			dom.writexml(fh)
			# ~ with open(os.path.join(path2,jpgFile),'w') as fh:
			# ~ dom.writexml(fh)
			#print('恭喜，写入xmin/ymin成功！')