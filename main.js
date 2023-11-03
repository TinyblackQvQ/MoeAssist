const { app, BrowserWindow } = require('electron');
const path = require('node:path');
const childProcess = require("child_process");

// 唤起fastapi
const pythonApi = childProcess.spawn("python-embed-64x/Scripts/uvicorn.exe", ["api:app", "--reload", "--port", "8800"]);
// pythonApi.stdin.write(`python-embed-64x/Scripts/uvicorn.exe api:app --reload --port 8800`)
pythonApi.stdout.on('data', function (data) {
    console.log(data.toString());
})
pythonApi.stderr.on('data', function (data) {
    console.log(data.toString());
})
pythonApi.on('close', function (code) {
    console.log(`closed with code: $[code]`);
})


const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'gui/src/nodeApi/preload.js')
        },
        // titleBarStyle: "hidden",
        titleBarOverlay: true
    })
    win.setMenu(null)
    win.loadFile('gui/src/html/index.html')
    win.webContents.openDevTools()
}

app.whenReady().then(() => {
    createWindow()
    
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

app.on('window-all-closed', () => {
    // todo 更加精细地kill进程
    // pythonApi.kill失效的原因应该是uvicorn唤醒了多个进程，且唤醒功能的那个进程直接kill掉对整体无影响
    console.log(pythonApi.kill())
    childProcess.spawn("taskkill", ["/f", "/im", "python.exe"]);
    
    if (process.platform !== 'darwin') 
    {
        app.quit()
    }
})