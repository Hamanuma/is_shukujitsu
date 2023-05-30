# 日本の祝日判定処処理
## 使い方
`git clone https://github.com/Hamanuma/is_shukujitsu.git`

import  
`from shukujitsu import SyukujitsuApi`  
本日が祝日か判定  
`is_syukujitsu = SyukujitsuApi().is_syukujitsu_today()`  
特定日付が祝日か判定  
`is_syukujitsu = SyukujitsuApi().is_syukujitsu(datetime.datetime.now())`  
