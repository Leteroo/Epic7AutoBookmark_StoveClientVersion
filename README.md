# Latest update: 2025/04/12  
Revise /img files because of some altered icons from Epic7


# Epic7AutoBookmark_StoveClientVersion  
基於此開源: https://github.com/steven010116/epic7autoBookmark/tree/main  
改成支援電腦版第七史詩的工具，目前小工具跟第七史詩的語系都只支援繁體中文。
  
![image](https://github.com/steven010116/epic7autoBookmark/assets/24381832/526e78b9-df97-4500-9758-55f514eed883)

## 一、環境
1. windows10 / windows11  
i. 顯示：1920 x 1080  
2. 第七史詩設定  
i. 語言選擇繁體中文  
3. Python  
i. 開發環境 3.10，不確定向下相容多少  
4. 文件架構  
i. released : 執行檔，一般使用者只須要保留這個文件。  
ii. source : 原始碼，開發與編譯都在這個文件下執行。
 
## 二、使用方式
  
> 請注意，此工具會去調整遊戲視窗，調整後請勿再移動遊戲視窗，否則會抓不到。  
> 想要變更視窗位置的話，請先移動到定點後，再重開小工具。  
  
1. 綠色按鈕 code > download zip 整包下載後解壓縮放在同一個資料夾下，路徑最好為英數避免有其他問題。
2. 開啟遊戲，進到秘密商店後，畫面會長得像下面這樣。  
  
![預覽](https://i.imgur.com/xLI1RJV.png)  

3. 用【系統管理員權限】開啟打開小工具(main.exe)，選擇條件並輸入目標次數，按下開始就會自己動了，且小工具視窗會自動縮小。  
4. 因為電腦版只能用桌面擷取再進行圖像辨識，所以會綁滑鼠，遊戲畫面也需要保持置頂。  
5. .exe 是用 pyinstaller main.spec 打包的，有疑慮可以自行編輯 main.spec 重新打包。

## 三、停止方式: 按下 F12，小工具視窗會自動恢復。  

## 四、特別感謝
steven010116 - 開源原始碼  
Raven9527 - 自動點擊派遣功能
