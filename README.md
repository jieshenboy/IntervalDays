# IntervalDays
给定任意两个日期，计算两个之前之间相隔多少天。

采用的思路为：计算两个时间之间的间隔天数
实验环境：python3.6
解题思路：
目的：给定任意两个日期，计算两个之前之间相隔多少天。
方法：解决的思路为两个日期之间相差多少天。
1、	首先将这两个日期从小到大排序；
2、	当二者年份一样的时候，即同一年的时候，可以将二者在同一年份已经过去的天数相减得到间隔天数。即：间隔天数 = | 前者该年第几天 – 后者该年第几天 |
当年份不一样的时候，可以将这部分间隔天数分为三部分：
1、前者年份剩余的天数
2、两个年份间隔的天数
3、后者年份已经过去的天数

所以两者的间隔天数 = 前者年份剩余的天数+两个年份间隔的天数+后者年份已经过去的天数
3、	设计模块两个年份间隔的天数模块、年份已经过去的天数、年份剩余天数模块，其中年份剩余天数模块 = 年份天数-已经过去的天数。
4、	设计年份天数模块，闰年的定义为不能被100整除且能被4整除的年份都是闰年，所以我们进行整除判断，并如果为闰年的话，该年天数设为366天，二月天数设为29天，否则其它年份天数为365天，二月天数为28天。
5、	设定月份天数模块，使用年份天数模块判断2月份天数，剩下的月份天数将1、3、5、7、8、10、12月份设为31天，其它月份天数设为30天。
6、	设定两年间相差天数模块，使用for循环将这些间隔年份的天数都加起来。
7、	当年过去时间模块，将已经过去的月份的天数和最后一个月已经过去的天数加起来。

程序的具体设计放在了附件IntervalDays.py中。

# 注：模块设计完成
