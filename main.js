/*const kmlgenBtn = document.getElementById("gen-btn"); */
let {PythonShell} = require('python-shell')
// console.log("running bubbles.py")
// PythonShell.run('', null, function (err, results) {
//   console.log("main js before error")
//   console.log()
//   if (err) throw err;
//   console.log('main js finished');
// });

ipcMain.on('fileupload', function (event, pathToFile) {
  console.log(pathToFile)
  PythonShell.run('bubbles.py', {
    args: [pathToFile] // Send our filepath to python
  }, function (err, results) {
    if (err) {
      console.error(err)
      return
    }

    const kmlFile = results[0]

    // Send kmlFile to actions.js (ipcmain -> ipcrenderer)
    window.webContents.send('kmlConversion', kmlFile)
    // Turn string into file object
    // Prompt user to download in browser
  })
})

/*let window;

  function createWindow () {
      window = new BrowserWindow(
        {
          width: 800, 
          height: 600,
          webPreferences: {
            nodeIntegration: true
          }
        })
      window.loadFile('index.html')
  } 



  app.on('ready', createWindow)
  app.on('window-all-closed', () => {
      if (process.platform !== 'darwin') {
        app.quit()
      }
  })
*/