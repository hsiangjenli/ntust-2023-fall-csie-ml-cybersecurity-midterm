# How to use ?
在這個目錄下新增 `.env` 檔案，並且填入 VirusShare 的帳號密碼
```javascript
USERNAME=myusername
PASSWORD=mypassword
```
接著執行

```bash
make all
```
> 解釋  
> 
> - `make download` 會執行 `vs.py` 這隻程式
> - 並且帶入環境變數 `USERNAME` 與 `PASSWORD`，這兩個環境變數會被 `vs.py` 讀取，並且登入 VirusShare
> - 接著會下載 `--family` 所指定的家族樣本（在 `motif_reports.csv` 裡面，該 family 的病毒如果有在 VirusShare 就會被下載下來變成 zip 檔。）


# MOTIF
```javascript
Reported family
icedid                 143
maze                    74
azorult                 74
turnedup                60
phorpiex                59
trickbot                52
shamoon                 49
darknexus               45
egregor                 44
vermin                  44
gandcrab                44
sobaken                 42
locky                   42
astaroth                42
seduploader             42
prometei                40
redaman                 40
artradownloader         40
olympicdestroyer        38
interplanetarystorm     38
```