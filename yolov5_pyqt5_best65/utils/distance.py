foc = 1000.0        # 镜头焦距
# real_hight_person = 64.96   # 行人高度
# real_hight_car = 57.08      # 轿车高度

real_hight_person = 8.01   # 路锥高度
real_hight_car = 39.37      # 瓶子高度，注意单位是英寸

# 自定义函数，单目测距
def detect_distance_person(h):
    dis_inch = (real_hight_person * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm/100
    return dis_m

def detect_distance_car(h):
    dis_inch = (real_hight_car * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm/100
    return dis_m
