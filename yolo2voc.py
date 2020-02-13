# -*- coding: utf-8 -*
from xml.dom.minidom import Document
import os
import os.path
from PIL import Image

ann_path = '/home/gjx/picture/dancer/2020.1.24/labelnw/' #yolov3标注.txt文件夹
img_path = '/home/gjx/picture/dancer/2020.1.24/jpeg/' #图片文件夹
xml_path = '/home/gjx/picture/dancer/2020.1.24/annotation/' #  .xml文件存放地址

if not os.path.exists(xml_path):
    os.mkdir(xml_path)


def writeXml(tmp, imgname, w, h, objbud, wxml):
    doc = Document()
    # owner
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    # owner
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    folder_txt = doc.createTextNode("HUMANOID")
    folder.appendChild(folder_txt)

    filename = doc.createElement('filename')
    annotation.appendChild(filename)
    filename_txt = doc.createTextNode(imgname)
    filename.appendChild(filename_txt)
    # ones#
    source = doc.createElement('source')
    annotation.appendChild(source)

    database = doc.createElement('database')
    source.appendChild(database)
    database_txt = doc.createTextNode("The VOC2005 Database")
    database.appendChild(database_txt)

    annotation_new = doc.createElement('annotation')
    source.appendChild(annotation_new)
    annotation_new_txt = doc.createTextNode("PASCAL VOC2005")
    annotation_new.appendChild(annotation_new_txt)

    image = doc.createElement('image')
    source.appendChild(image)
    image_txt = doc.createTextNode("flickr")
    image.appendChild(image_txt)
    # onee#
    # twos#
    size = doc.createElement('size')
    annotation.appendChild(size)

    width = doc.createElement('width')
    size.appendChild(width)
    width_txt = doc.createTextNode(str(w))
    width.appendChild(width_txt)

    height = doc.createElement('height')
    size.appendChild(height)
    height_txt = doc.createTextNode(str(h))
    height.appendChild(height_txt)

    depth = doc.createElement('depth')
    size.appendChild(depth)
    depth_txt = doc.createTextNode("3")
    depth.appendChild(depth_txt)
    # twoe#
    segmented = doc.createElement('segmented')
    annotation.appendChild(segmented)
    segmented_txt = doc.createTextNode("0")
    segmented.appendChild(segmented_txt)

    for i in range(0, int(len(objbud))):
        objbuds=objbud[i].split(' ')
        #print(objbuds)
        # threes#
        object_new = doc.createElement("object")
        annotation.appendChild(object_new)

        name = doc.createElement('name')
        object_new.appendChild(name)
        name_txt = doc.createTextNode(objbuds[0])
        if name_txt.data == '0':
            name_txt.data = 'ball'
        elif name_txt.data == '1':
            name_txt.data = 'goal'   
        elif name_txt.data == '2':
            name_txt.data = 'robot'
        elif name_txt.data == '3':
            name_txt.data = 'T corner'
        elif name_txt.data == '4':
            name_txt.data = 'L corner'
        elif name_txt.data == '5':
            name_txt.data = 'X corner'
        elif name_txt.data == '6':
            name_txt.data = 'penalty marks'       
        name.appendChild(name_txt)

        pose = doc.createElement('pose')
        object_new.appendChild(pose)
        pose_txt = doc.createTextNode("Unspecified")
        pose.appendChild(pose_txt)

        truncated = doc.createElement('truncated')
        object_new.appendChild(truncated)
        truncated_txt = doc.createTextNode("0")
        truncated.appendChild(truncated_txt)

        difficult = doc.createElement('difficult')
        object_new.appendChild(difficult)
        difficult_txt = doc.createTextNode("0")
        difficult.appendChild(difficult_txt)
        # threes-1#
        bndbox = doc.createElement('bndbox')
        object_new.appendChild(bndbox)

        xmin = doc.createElement('xmin')
        bndbox.appendChild(xmin)
        xmin_txt = doc.createTextNode(str(int((float(objbuds[1])*w - float(objbuds[3])*w/2.0))))
        xmin.appendChild(xmin_txt)

        ymin = doc.createElement('ymin')
        bndbox.appendChild(ymin)
        ymin_txt = doc.createTextNode(str(int(float(objbuds[2])*h - float(objbuds[4])*h/2.0)))
        ymin.appendChild(ymin_txt)

        xmax = doc.createElement('xmax')
        bndbox.appendChild(xmax)
        xmax_txt = doc.createTextNode(str(int(float(objbuds[1])*w + float(objbuds[3])*w/2.0)))
        xmax.appendChild(xmax_txt)

        ymax = doc.createElement('ymax')
        bndbox.appendChild(ymax)
        ymax_txt = doc.createTextNode(str(int(float(objbuds[2])*h + float(objbuds[4])*h/2)))
        ymax.appendChild(ymax_txt)
        # threee-1#
        # threee#

    tempfile = tmp + "test.xml"
    with open(tempfile, "w") as f:
        f.write(doc.toprettyxml(indent='\t'))

    rewrite = open(tempfile, "r")
    lines = rewrite.read().split('\n')
    newlines = lines[1:len(lines) - 1]

    fw = open(wxml, "w")
    for i in range(0, len(newlines)):
        fw.write(newlines[i] + '\n')

    fw.close()
    rewrite.close()
    os.remove(tempfile)
    return

def search(path,name):
    
    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in dirs or name in files:
            flag = 1      #判断是否找到文件
            root = str(root)
            dirs = str(dirs)
            return os.path.join(root, dirs)
    return -1

for files in os.walk(ann_path):
    img_path = '/home/gjx/picture/dancer/2020.1.24/jpeg/' #图片文件夹
    temp = '/home/gjx/picture/dancer/2020.1.24/annotation2'
    if not os.path.exists(temp):
        os.mkdir(temp)
    for file in files[2]:
        img_path = '/home/gjx/picture/dancer/2020.1.24/jpeg/' #图片文件夹
        print (file + "-->start!")
        (filename, extension) = os.path.splitext(file)
        img_name = os.path.splitext(file)[0] + '.jpg'
        fileimgpath = img_path + img_name
        answer = search(img_path,img_name)
        print(fileimgpath)
        if search(img_path,img_name)==-1:
            img_name = os.path.splitext(file)[0] + '.png'
            img_path="/home/gjx/picture/dancer/2020.1.24/png/"
            fileimgpath = img_path + img_name
            if search(img_path,img_name)==-1:
                img_name = os.path.splitext(file)[0] + '.jpeg'
                img_path="/home/gjx/picture/dancer/2020.1.24/jpg/"
                fileimgpath = img_path + img_name
        im = Image.open(fileimgpath)
        width = int(im.size[0])
        height = int(im.size[1])

        filelabel = open(ann_path + file, "r")
        lines = filelabel.read().split('\n')
        obj = lines[:len(lines)-1]
        #print(obj)

        filename = xml_path + os.path.splitext(file)[0] + '.xml'
        writeXml(temp, img_name, width, height, obj, filename)
    os.rmdir(temp)