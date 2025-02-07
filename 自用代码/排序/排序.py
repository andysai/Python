data = [
    {'name': '辉', 'free': '1.05'},
    {'name': '林先生', 'free': '0.42'},
    {'name': '阿乐', 'free': '1.40'},
    {'name': '李锦泉', 'free': '0.20'},
    {'name': '大彬', 'free': '1.43'},
    {'name': '始如初见', 'free': '0.52'},
    {'name': '无言', 'free': '0.16'},
    {'name': '小王子', 'free': '0.55'},
    {'name': '拂晓', 'free': '0.34'},
    {'name': '彭成勇', 'free': '0.58'},
    {'name': '刘勋', 'free': '1.10'},
    {'name': '游者', 'free': '0.26'},
    {'name': '柠檬', 'free': '1.18'},
    {'name': '文羡', 'free': '0.13'},
    {'name': '李钱钱', 'free': '0.49'},
    {'name': '袅歌', 'free': '0.19'}
]

sorted_data = sorted(data, key=lambda k: k['free'], reverse=True)

for item in sorted_data:
    print(item['name'], item['free'])


