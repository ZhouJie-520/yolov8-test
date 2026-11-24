# import os
# from collections import Counter
# from pathlib import Path
#
# root = Path(r"D:/aiStudyProjects/object_detection_model/dataset")
# for split in ["HelmetDataset-YOLO-Train", "HelmetDataset-YOLO-Val"]:
#     imgs = list((root / split / "images").glob("*.*"))
#     txts = list((root / split / "labels").glob("*.txt"))
#     cnt = Counter()
#     for t in txts:
#         for line in t.read_text(encoding="utf-8").splitlines():
#             if line.strip():
#                 cnt[line.split()[0]] += 1
#     print(split, "图片:", len(imgs), "标签:", len(txts), "类别分布:", dict(cnt))
#

