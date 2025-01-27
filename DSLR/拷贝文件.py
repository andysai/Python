import os
import shutil
from datetime import date

def copy_and_rename_file(src_path, dest_folder, new_name):
    # 确保目标文件夹存在
    os.makedirs(dest_folder, exist_ok=True)

    # 复制文件到目标文件夹
    shutil.copy(src_path, os.path.join(dest_folder, new_name))

# 获取时间
current_time = date.today()

# 源文件路径
posweb_source_path = r"D:\project\posweb\posweb\out\artifacts\posWeb_war\posWeb.war"
sms_source_path = r"D:\project\sms\new_pos-LitePos\out\artifacts\sms_war\sms.war"

# 目标文件夹路径
# destination_folder = r"E:\Dslr\项目\K8S部署\POS\version"
posweb_folder = r"F:\dslr\项目\K8S部署\POS\version\posweb"
sms_folder = r"F:\dslr\项目\K8S部署\POS\version\sms"

# 新文件名
posweb_filename = "posWeb.war-" + str(current_time)
sms_filename = "sms.war-" + str(current_time)

# 拷贝文件
copy_and_rename_file(posweb_source_path, posweb_folder, posweb_filename)
#copy_and_rename_file(sms_source_path, sms_folder, sms_filename)
