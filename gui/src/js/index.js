
// 控制面板开合
var chPanelLock = false;
function changePanel(targetId) {
    var home = document.getElementById("home");
    var plan = document.getElementById("plan");
    var script = document.getElementById("script");
    var download = document.getElementById("download");
    var settings = document.getElementById("settings");
    const panelList = [home, plan, script, download, settings]

    if (chPanelLock)
        return;
    else
        chPanelLock = true;

    panelList.forEach(item => {
        // debugger
        if (item.id == targetId) {
            if (item.style.display == "none" || item.style.display == "")
            // 更换面板
            {
                // 关闭所有面板
                panelList.forEach(item => {
                    item.style.display = "none";
                })
                item.style.display = "block";
                item.style.top = "0px";
                item.style.opacity = "100%";
            }
        }
    });

    chPanelLock = false
}

window.onload = () => {
    changePanel("home");
}
