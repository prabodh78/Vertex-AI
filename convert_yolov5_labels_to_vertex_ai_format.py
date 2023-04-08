import csv
import os
import glob
import cv2
import pandas as pd
from classes_in_coco import CLASSES


def write_to_csv(filename, data):  # writes the given data to the csv filename provided
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
    csvfile.close()


def yolo_to_xml_bbox(bbox, w, h):
    # x_center, y_center width heigth
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)
    return [xmin/w, ymin/h, xmax/w, ymax/h]


def convert_yolov5_annotation_to_vertex_ai_formate(annotation_dir_path, cloud_path, output_file_name):
    for label_txt in glob.glob('{}/*'.format(annotation_dir_path)):
        image_path = label_txt.replace('labels', 'images').replace('txt', 'jpg')
        if os.path.exists(image_path):
            h, w = cv2.imread(image_path).shape[:2]
            data = pd.read_csv(label_txt, sep=" ", header=None)
            for c in range(len(data[0])):
                tmp = []
                for i in range(5):
                    tmp.append(data[i][c])
                class_id, x_center, y_center, width, height = tmp
                # x_center, y_center, width, height = data[1][i], data[2][i], data[3][i]
                X_MIN, Y_MIN, X_MAX, Y_MAX = yolo_to_xml_bbox([x_center, y_center, width, height], w, h)
                class_name = CLASSES[class_id]
                data_write = ['TRAIN', cloud_path + os.path.basename(image_path), class_name, X_MIN, Y_MIN, X_MAX, Y_MIN, X_MAX, Y_MAX, X_MIN, Y_MAX]
                write_to_csv(output_file_name, data_write)


if __name__ == '__main__':
    annotation_dir_path = '/home/prabodh/Personal_Space/Tutorials/datasets/coco128/labels/train2017'
    cloud_path = 'gs://bucketname/folder_path_of_stored_images/'
    output_file_name = 'coco_128_gcp_labels_8_April_23.csv'
    convert_yolov5_annotation_to_vertex_ai_formate(annotation_dir_path, cloud_path, output_file_name)