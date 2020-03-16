import platform
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)



import matplotlib

#한글 라벨 설정 : '맑은 고딕'으로 설정 (windows 운영체제만)
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

#한글 라벨 설정 : '맑은 고딕'으로 설정 (Mac 운영체제만)
matplotlib.rcParams['font.family'] = 'AppleGothic'