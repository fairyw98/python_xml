import os
import shutil
import os.path
import xml.dom.minidom

for num in range(1,77):
	src = 'C:\\Users\\Fairy\\Desktop\\000002.xml'
	dst = 'C:\\Users\\Fairy\\Desktop\\circle\\'+'000' + format(str(num), '0>3s')+'.xml'
	shutil.copyfile(src,dst)
	path='C:\\Users\\Fairy\\Desktop\\circle'
	xmlFile = dst
	
	if not os.path.isdir(xmlFile):
		print(xmlFile)
			
		dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
		root=dom.documentElement
		paths=root.getElementsByTagName('path')
		filenames=root.getElementsByTagName('filename')
	
		for i in range(len(filenames)):
			filenames[i].firstChild.data='000' + format(str(num), '0>3s')+".jpg"
			fn = filenames[i].firstChild.data
		
		for i in range(len(paths)):
			paths[i].firstChild.data='C:\\Users\\Fairy\\Desktop\\xml\\'+fn
		with open(os.path.join(path,xmlFile),'w') as fh:
			dom.writexml(fh)