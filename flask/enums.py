from enum import Enum

class Flags(Enum):
    First_Login             = 1     #首次登录
    Video_Authentication    = 2     #视频认证通过
    First_Publish           = 3     #首次发布软文
    First_Like              = 4     #首次点赞
    First_Comment           = 5     #首次评论
    First_Forward           = 6     #首次转发
    First_Follow            = 7     #首次关注
    First_Join              = 8     #首次加入一个群
    First_Set_Avatar        = 9     #首次设置头像
    First_Set_Name          = 10    #首次设置昵称
    First_Create_Group      = 11    #首次创建群
    First_Followed          = 12    #首次被关注
    First_Liked             = 13    #首次被点赞
    First_Commented         = 14    #首次被评论
    First_Forwarded         = 15    #首次被转发
    Day_First_Publish       = 16    #每日首次发布

FlagsValueMap = {}
FlagsValueMap[Flags.First_Login]            = 10 #首次登录
FlagsValueMap[Flags.Video_Authentication]   = 10 #视频认证通过
FlagsValueMap[Flags.First_Publish]          = 10 #首次发布软文
FlagsValueMap[Flags.First_Like]             = 10 #首次点赞
FlagsValueMap[Flags.First_Comment]          = 10 #首次评论
FlagsValueMap[Flags.First_Forward]          = 10 #首次转发
FlagsValueMap[Flags.First_Follow]           = 10 #首次关注
FlagsValueMap[Flags.First_Join]             = 20 #首次加入一个群
FlagsValueMap[Flags.First_Set_Avatar]       = 5  #首次设置头像
FlagsValueMap[Flags.First_Set_Name]         = 5  #首次设置昵称
FlagsValueMap[Flags.First_Create_Group]     = 20 #首次创建群
FlagsValueMap[Flags.First_Followed]         = 10 #首次被关注
FlagsValueMap[Flags.First_Liked]            = 10 #首次被点赞
FlagsValueMap[Flags.First_Commented]        = 10 #首次被评论
FlagsValueMap[Flags.First_Forwarded]        = 10 #首次被转发
FlagsValueMap[Flags.Day_First_Publish]      = 4  #每日首次发布