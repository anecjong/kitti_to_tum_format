<div align="center">
  <h1>KITTI to TUM format(pose)</h1>
</div>

## Depencdency
python scipy library is used for rotation matrix and quaternion.  
python glob library is used for making file lists.  
numpy

## Pose format
- **KITTI Pose(SE3)**
    
    ```
    r11 r12 r13 tx
    r21 r22 r23 ty
    r31 r32 r33 tz
    0   0   0   1
    ```
    
    `r11 r12 r13 tx r21 r22 r23 ty r31 r32 r33 tz`
    
- **TUM Pose**
    
    ```
    time tx ty tz q1 q2 q3 q4
    ```

To change kitti pose to TUM pose, you need timestamp file.


## How to Use
```
.
├── kitti_2_tum.py
├── poses
│   └── 04.txt
├── time
│   └── 04.txt
└── tum_file
```
Prepare pose files and time files.  
Each pose file and time file should have same name.

```
$ python3 kitti_2_tum.py
```
In terminal, type above.

```
.
├── kitti_2_tum.py
├── poses
│   └── 04.txt
├── time
│   └── 04.txt
└── tum_file
    └── 04_tum.txt
```
Your tum files are saved in tum_file directory.