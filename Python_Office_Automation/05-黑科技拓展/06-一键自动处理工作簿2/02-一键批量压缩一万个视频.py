import os

def video_execute():
    get_file = []
    path = "../source_material/06/02一键批量压缩一万个视频"
    os.chdir(path)
    file_name = os.getcwd() + "/视频处理"
    # print(file_name)
    for file in os.listdir(file_name):
        get_file.append(os.path.join(file_name, file))
    video = []
    for i in get_file:
        if ".mp4" in i or ".MP4" in i or ".mov" in i or ".MOV" in i:
            video.append(i)
        else:
            pass
    count = 0
    for my_vi in video:
        b_side = 0.0
        e_side = 0.0
        count = count + 1
        vi_size_begin = os.path.getsize(my_vi) / 1024
        b_side += float(vi_size_begin)
        my_vi = my_vi.replace(os.getcwd() + '/', "")[5:]
        sava_vi = os.getcwd() + "/video/" + my_vi
        # -b可以修改视频质量，越大越清晰，-r为视频的帧率，一般为25就可以了
        # print(sava_vi)
        my_vi = file_name + "/" + my_vi
        os.system('ffmpeg -i {} -y {} -pix_fmt yuv420p  -b 80 -r 30  -ar 44100 -ac 2 -ab 220'.format(my_vi, sava_vi))
        vi_size_end = os.path.getsize(sava_vi) / 1024
        print("视频{}\n压缩前{}kb || 压缩后{}kb".format(count, round(vi_size_begin, 2), round(vi_size_end, 2)))
        e_side += float(vi_size_end)
    print("共压缩", round(b_side - e_side, 2), "kb")

def main():
    video_execute()

if __name__ == "__main__":
    main()
