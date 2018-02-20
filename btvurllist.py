#coding=utf-8
"""
    本程序只为媳妇生成下载节目的所有链接
"""



print("开始生成。。。。。。")

"""
《财富大魔方》20180212我国海洋强国建设迎来历史机遇期
"""
# linkUrl="http://video.tvbt.sj.360.cn/vod-pgc-btime-q1-bj/95579114_2-1518418399-ca48f7a0-ed99-094c_"
# for i in range(1,451):
#     if len(str(i))==1:
#         lU=linkUrl+"0000"+str(i)+".ts"
#     elif len(str(i))==2:
#         lU=linkUrl+"000"+str(i)+".ts"
#     elif len(str(i))==3:
#         lU=linkUrl+"00"+str(i)+".ts"
#     print(lU)

"""
《财富大魔方》20180214如何辨别基金类型
"""
linkUrl="http://video.tvbt.sj.360.cn/vod-pgc-btime-q1-bj/96022902_2-1518599667-ec9abb1a-793a-175e_"
for i in range(1,451):
    if len(str(i))==1:
        lU=linkUrl+"0000"+str(i)+".ts"
    elif len(str(i))==2:
        lU=linkUrl+"000"+str(i)+".ts"
    elif len(str(i))==3:
        lU=linkUrl+"00"+str(i)+".ts"
    print(lU)
