# coding=utf-8

import glob
import os
import xml.etree.ElementTree as ET


def xml_to_txt(indir, outdir):
    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations) + '*.xml')

    for i, file in enumerate(annotations):

        file_save = 'gt_' + file.split('.')[0] + '.txt'
        file_txt = os.path.join(outdir, file_save)
        f_w = open(file_txt, 'w')

        # actual parsing
        in_file = open(file)
        tree = ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
            current = list()
            name = obj.find('name').text

            xmlbox = obj.find('bndbox')
            xn = xmlbox.find('xmin').text
            xx = xmlbox.find('xmax').text
            yn = xmlbox.find('ymin').text
            yx = xmlbox.find('ymax').text
            # print xn
            f_w.write(xn + ',' + yn + ',' +
                      xx + ',' + yn + ',' +
                      xx + ',' + yx + ',' +
                      xn + ',' + yx + '\n')

        print("{} save to {}".format(file, file_save))


if __name__ == '__main__':
    indir = '/Volumes/KIM/projects/AI_Projects/text-detection-ctpn/data/VOCdevkit/VOC2007/Annotations'  # xml目录
    outdir = '/Volumes/KIM/projects/AI_Projects/text-detection-ctpn/data/VOCdevkit/VOC2007/Label'  # txt目录
    xml_to_txt(indir, outdir)
