# How to use ?
## 新增 `.env` 檔案
在這個目錄下新增 `.env` 檔案，並且填入 VirusShare 的帳號密碼
```javascript
USERNAME=myusername
PASSWORD=mypassword
```

## 安裝將 PE32 轉 Binary 的工具
```bash
sudo apt-get install xxd
```

## 安裝解析網頁的工具
```bash
pip install bs4
```
### 可以開始使用了～～～

接著執行

```bash
make download
make uzip
make unzip2bytescode
```
> 解釋  
> 
> - `make download` 會執行 `vs.py` 這隻程式
> - 並且帶入環境變數 `USERNAME` 與 `PASSWORD`，這兩個環境變數會被 `vs.py` 讀取，並且登入 VirusShare
> - 接著會下載 `--family` 所指定的家族樣本（在 `motif_reports.csv` 裡面，該 family 的病毒如果有在 VirusShare 就會被下載下來變成 zip 檔。）

### 我選的 family（我隨便選的）
- icedid（實際有的約 70 個檔案）
- maze（約 20 個檔案）
- azorult（不到 10 個）

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