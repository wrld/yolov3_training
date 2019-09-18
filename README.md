# 制作yolo的voc样本
## 使用labelimg
- labelimg[官方代码下载](https://github.com/tzutalin/labelImg),或直接下载本文件夹代码
- 参考readme安装及运行即可
## 样本预制作
- 首先将样本视频转换为照片,使用video_to_image.cpp(记改路径),运行代码要求有opencv
- 将照片分为训练集和验证集两个文件夹
- 运行rename.sh(记得改路径),将照片序列好
## 使用labelimg标记样本
- 选择打开目录,即为照片目录,存放目录也是该目录
- 选择yolo模式
- 截取样本,选框越小越好
- 保存

