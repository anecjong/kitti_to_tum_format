from scipy.spatial.transform import Rotation as R
import numpy as np
import glob
import os


def start():
    split_dir = "/"  # ubuntu
    # split_dir = "\\" # window

    kitti_pose_name_list = glob.glob("./poses/*")
    kitti_time_list = glob.glob("./time/*")
    kitti_pose_name_list.sort()
    kitti_time_list.sort()
    for i in range(len(kitti_time_list)):
        if kitti_pose_name_list[i].split(split_dir)[-1].split(".")[0] != kitti_time_list[i].split(split_dir)[-1].split(".")[0]:
            print("check file names!")
            print(kitti_time_list[i])
            print(kitti_pose_name_list[i])
            return 1
        kitti_pose_name = kitti_pose_name_list[i]
        kitti_time_name = kitti_time_list[i]

        with open(kitti_pose_name, "r") as f:
            lines_se3 = f.readlines()
        with open(kitti_time_name, "r") as f:
            lines_times = f.readlines()

        file_contents = []

        for i, se3 in enumerate(lines_se3[:]):
            se3 = list(map(float, se3.split()))
            rotation_matrix = [se3[0:3], se3[4:7], se3[8:11]]
            r = R.from_matrix(rotation_matrix)
            temp = [float(lines_times[i])] + [se3[x]
                                              for x in [3, 7, 11]] + list(np.round(r.as_quat(), 6))
            file_contents.append(temp)
        print(len(file_contents))
        output_file_name = "./tum_file/" + \
            kitti_pose_name.split(split_dir)[-1].split(".")[0] + "_tum.txt"
        with open(output_file_name, "w")as f:
            for content in file_contents:
                content = map(str, content)
                temp = " ".join(content)
                f.write(temp)
                f.write("\n")


if __name__ == "__main__":
    start()
