/*
home.js
-------
*/

let start = 0
let timeVisible = false
const usageTime = document.getElementById("usage-time")
usageTime.style.cssText = "display:none;"

function counter() {
    start += 1
    document.title = `${start} seconds`
    usageTime.innerHTML = `Time since last reload (in seconds): <i style='color:orange;'>${start}</i>`
}
setInterval(counter, 1000)
// -----------------------------------------------------

const helpTable = `
<div id="section-commands">
    <h6>Commands</h6>

    <table>
        <tbody>
            <tr>
                <th>
                    <p>cd home</p>
                </th>

                <th class="column2">
                    <p>- navigate to the 'home' route</p>
                </th>
            </tr>

            <tr>
                <th>
                    <p>cd videos</p>
                </th>

                <th class="column2">
                    <p>- navigate to the 'videos' route</p>
                </th>
            </tr>

            <tr>
                <th>
                    <p>cd channels</p>
                </th>

                  <th class="column2">
                <p>- navigate to the 'channels' route</p>
                </th>
            </tr>

            <tr>
                <th>
                    <p>cd tasks</p>
                </th>

                  <th class="column2">
                    <p>- navigate to the 'tasks' route</p>
                </th>
            </tr>
            
            <tr>
                <th>
                    <p>cd webpages</p>
                </th>

                  <th class="column2">
                    <p>- navigate to the 'webpages' route</p>
                </th>
            </tr>

            <tr>
                <th>
                    <p>cd api/docs</p>
                </th>

                  <th class="column2">
                    <p>- navigate to the 'api/docs' route</p>
                </th>
            </tr>

              <tr>
                <th>
                    <p>about</p>
                </th>

                  <th class="column2">
                    <p>- show information about this software program</p>
                </th>
            </tr>

            <tr>
                <th>
                    <p>history</p>
                </th>

                  <th class="column2">
                    <p>- show session history</p>
                </th>
            </tr>

            <tr>
                <th>
                    <p>timer</p>
                </th>

                  <th class="column2">
                    <p>- show or hide the time since the last reload</p>
                </th>
            </tr>
            
            <tr>
                <th>
                    <p>browser</p>
                </th>

                  <th class="column2">
                    <p>- show browser and other details</p>
                </th>
            </tr>

        </tbody>
    </table>
</div> 
`



const browserTableContainer = document.getElementById("section-browser-details")
browserTableContainer.style.cssText = "display:none;"

const browserTable = document.getElementById("section-browser-details").querySelector("table")
    .querySelector("tbody")


let userHistory = []
let historyBlock = document.querySelector(".history")

let feedback = document.querySelector(".feedback")


// --- KEY EVENT --- // 
let uInput = document.getElementById("user-input")
uInput.addEventListener("keydown", (event) => {
    feedback.innerHTML = ""

    if (event.key === "Enter") {
        historyBlock.innerHTML = ""
        browserTableContainer.style.cssText = "display:none;"
        browserTable.innerHTML = ""

        data = uInput.value.trim()
        console.log(`\ninput: "${data}", length: ${data.length}`)
        userHistory.push(data)

        const website1 = "https://ammaar0x01-websites.netlify.app/"
        const website2 = "https://youtube-favs.netlify.app/"
        const page0 = "http://localhost:5000/home"
        const page1 = "http://localhost:5000/videos"
        const page2 = "http://localhost:5000/channels"
        const page3 = "http://localhost:5000/tasks"
        const page4 = `${window.location.origin}/webpages`

        // const page4 = "http://localhost:5000/api/docs"
        // const page4 = `${window.location.host}/api/docs`
        const page10 = `${window.location.origin}/api/docs`


        if (data == "hello world") {
            window.open(website1)
        }
        else if (data == "youtube-favs") {
            window.open(website2)
        }
        else if (data == "cd home" || data == "/home") {
            window.open(page0)
        }
        else if (data == "cd videos" || data == "/videos") {
            window.open(page1)
        }
        else if (data == "cd channels" || data == "/channels") {
            window.open(page2)
        }
        else if (data == "cd tasks" || data == "/tasks") {
            window.open(page3)
        }
        else if (data == "cd webpages" || data == "/webpages") {
            window.open(page4)
        }
        

        else if (data == "cd api/docs" || data == "/api/docs") {
            window.open(page10)
        }

        else if (data == "timer") {
            timerBlock()
        }
        else if (data == "browser" || data == "browser data") {
            showBrowserInfo()
        }
        else if (data == "help") {
            historyBlock.innerHTML += helpTable
        }
        else if (data == "history") {
            showHistory()
        }
        else if (data == "about") {
            showAboutAppInfo()
        }

        else {
            feedback.innerHTML = "Invalid input"
        }

        uInput.value = ""
    }
})

// -----------------------------------------------------


function showHistory() {
    historyBlock.innerHTML += `
<br /> 
<i style='color:orange;'>History</i>
`
    userHistory.forEach((item) => {
        historyBlock.innerHTML += `<br /> - ${item}`
    })
    console.log(userHistory)
}
// -----------------------------------------------------

 function counter1() {
    start += 1
    document.title = `> ${start} seconds`
}
function timerBlock() {
    // change title to time 
   
// setInterval(counter1, 1000)

    if (!timeVisible) {
        usageTime.style.cssText = "display:block;"
        timeVisible = true
    }
    else if (timeVisible) {
        usageTime.style.cssText = "display:none;"
        timeVisible = false
    }
}
// -----------------------------------------------------

const windowObjData = {
    "URL": window.document.URL,

    // location 
    "host": window.location.host,
    "hostname": window.location.hostname,
    "full path": window.location.href,
    "origin route": window.location.origin,
    "port": window.location.port,
    "protocol": window.location.protocol,
    "route (end-point)": window.location.pathname,
    // "": "\n",

    // navigator 
    "app name": window.navigator.appName,
    "app code name": window.navigator.appCodeName,
    "app version": window.navigator.appVersion,
    "device memory": window.navigator.deviceMemory,
    "language": window.navigator.languages[0],
    "outer-height": window.outerHeight,
    "inner-height": window.innerHeight,
    "outer-width": window.outerWidth,
    "inner-width": window.innerWidth,
}

function showBrowserInfo() {
    browserTableContainer.style.cssText = "display:block;"

    const objectKeys = Object.keys(windowObjData)
    for (let a = 0; a < objectKeys.length; a++) {
        browserTable.innerHTML += `
<tr>
    <th>
        <p>${objectKeys[a]}</p>
    </th>

    <th class="column2">
        <p>- ${windowObjData[objectKeys[a]]}</p>

    </th>
</tr>`
    }
}
// -----------------------------------------------------

function showAboutAppInfo() {
    historyBlock.innerHTML += `
<p style="color:orange;">About</p>

<pre style="white-space:pre-wrap; font-family:'Orbitron', sans-serif;">
This is a web-based, software program to store YouTube videos, 
and websites that you may find enjoyable or education
</pre>

<p id="comment">
    Created by 
    <br>
    <a href="https://ammaar0x01.netlify.app" target="_blank" style="color:orange;">ammaar0x01</a> | 
    <a href="https://github.com/ammaar0x01" target="_blank" style="color:orange;">GitHub profile</a>
</p>

`
}
// -----------------------------------------------------
