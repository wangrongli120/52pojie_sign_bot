# 52pojie_sign_bot

## 只支持一个帐号签到#
### 每天北京时间早上8:01签到

如要更改签到时间，在.github/workflows/52pojie_sign.yml中修改cron表达式。

如本签到系统的cron表达式为 '1 0 * * * *'，代表标准时间00：01， 第一位是分，第二位是时，后面三位为**，表示不做限制。北京时间属于东八区，时位+8，既是北京时间早上8:01

### 在setting-secrets里新建secret

1. secret键 COOKIE
2. secret值 52pojie cookie值
   
### 获取52pojie cookie

1. 手动登录52pojie网站
2. 按下F12或右键检查打开开发者工具，点击网络(network)选项卡
3. 刷新网页，拉动开发者工具界面滑动条到顶部，找到52pojie.cn并点击
4. 开发者工具右侧点击标头(headers)，下拉滑动条，找到请求标头（request headers），复制cookie中的 #### htVD_2132_saltkey=xxxxx;htVD_2132_auth=xxxxxx'两项
