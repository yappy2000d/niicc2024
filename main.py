from collections import Counter
import csv, os, time, shutil
import threading

from uart import receive
from yolov5.detect import run


folder_path = "ROOT/exp/labels/"
file_path = folder_path + "uploaded.txt"
id2classname = ['lettuce', 'potato', 'carrot', 'onion', 'garlic', 'leek', 'broccoli']

def 當冰箱門關上時():
    圖片 = 攝影機.拍照()
    圖片.存檔("uploaded.png")
    
    run(weights='yolov5/runs/train/yolo_veg_det/weights/best.pt',
        source='./uploaded.png',
        conf_thres=0.25, project='ROOT',
        save_txt=True
    )
    
    reserve = [0] * len(id2classname)

    while not os.path.exists(folder_path):
        time.sleep(1)

    if not os.path.exists(file_path):
        # 無辨識到
        pass
    else:
        with open(file_path, newline='') as file:
            rows = csv.reader(file, delimiter=' ')
            result = [row[0] for row in rows]

            for id in result:
                reserve[int(id)] += 1
            
            counter = Counter(result)
            reserve = [0] * len(id2classname)
            for id, count in counter.items():
                reserve[int(id)] = count

    # send(*reserve)
    
    print(dict(zip(id2classname, reserve)))
    shutil.rmtree("ROOT")
    
recv_thread = threading.Thread(target=receive, daemon=True)
recv_thread.start()