import os
import glob

print('[Info] YOLOv5 training started..!')
print('[Info] Does path able to access: ', os.path.exists('/gcs/bucket_name/datasets'))

os.system('python train.py --img 640 --batch 8 --epochs 10 --data new_coco128.yaml  --weights yolov5s.pt')

os.system('cp -R runs /gcs/bucket_name/')

print('[Info] Model training completed..!')
