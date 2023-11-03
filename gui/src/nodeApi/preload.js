import { contextBridge } from "electron"

// 获取api脚本
import indexApi from "./index/index_api"
 
// 暴露api至主线程
contextBridge.exposeInMainWorld("indexApi", indexApi)

window.addEventListener('DOMContentLoaded', () => {

})