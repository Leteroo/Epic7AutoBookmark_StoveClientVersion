# epic7autoBookmark_WindowsClient

基於此開源: https://github.com/steven010116/epic7autoBookmark/tree/main  
改成支援電腦版第七史詩的工具，目前小工具跟第七史詩的語系都只支援繁體中文。
  
![image](https://github.com/steven010116/epic7autoBookmark/assets/24381832/526e78b9-df97-4500-9758-55f514eed883)

## 一、環境
1. windows10 / windows11  
i. 顯示：800x600，程式會自動調整
2. 第七史詩  
i. 裝置詳細設定和遊戲詳細設定最好都不勾，如果覺得畫面太醜，高畫質套件測試過也是能正常運行  
ii. 推薦：只勾高級設定  
3. Python  
i. 開發環境 3.10，不確定向下相容多少
4. 文件架構  
i. released : 執行檔，一般使用者只須要保留這個文件。  
ii. source : 原始碼，開發與編譯都在這個文件下執行。
 
## 二、使用方式
  
1. 綠色按鈕 code > download zip 整包下載後解壓縮放在同一個資料夾下，路徑最好為英數避免有其他問題。
2. 開啟遊戲，進到秘密商店後，畫面會長得像下面這樣。  
  
![預覽](https://i.imgur.com/xLI1RJV.png)  

3. 用【系統管理員權限】開啟打開小工具(main.exe)，選擇條件並輸入目標次數，按下開始應該就會自己動惹。  
4. 因為電腦版只能用桌面擷取再進行圖像辨識，所以會綁滑鼠，遊戲畫面也需要保持置頂。  
5. .exe 是用 pyinstaller main.spec 打包的，有疑慮可以自行編輯 main.spec 重新打包。

## 三、停止方式

1. 因為使用中會綁定滑鼠，為了方便中途停止，在每個行為都設置了 1 秒的停頓。  
2. 想要中途停止，請在停頓時，將滑鼠手動移動到小工具的小視窗上點擊一次後，按下快捷鍵【SPACE】(空白鍵)。

## 四、特別感謝
steven010116 - 開源原始碼  
Raven9527 - 自動點擊派遣功能
