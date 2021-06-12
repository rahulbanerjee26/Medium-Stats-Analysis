var storyPath = window.location.href;

// Console API to clear console before logging new data
console.API;
if (typeof console._commandLineAPI !== 'undefined') {
    console.API = console._commandLineAPI; //chrome
} else if (typeof console._inspectorCommandLineAPI !== 'undefined') {
    console.API = console._inspectorCommandLineAPI; //Safari
} else if (typeof console.clear !== 'undefined') {
    console.API = console;
}

function getStats(){
    const data = document.querySelectorAll(".js-statsTableRow")
    const result = []
    data.forEach(
        (obj)=>{
            const title = obj.querySelector('.sortableTable-title>a').text
            const minRead = obj.querySelector('.readingTime').title.replaceAll(" min read","")
            const publication = obj.querySelector('.sortableTable-link').text
            const views = obj.querySelectorAll('.sortableTable-value')[1].textContent
            const reads = obj.querySelectorAll('.sortableTable-value')[2].textContent
            const readPercentage = obj.querySelectorAll('.sortableTable-value')[3].textContent
            const numFans = obj.querySelectorAll('.sortableTable-value')[4].textContent
            result.push(
                {title,minRead,publication,views,reads,readPercentage,numFans}
            )
    })
    
    console.save(result);
}

console.save = function (data, filename) {
    if (!data) {
        console.error('Console.save: No data')
        return;
    }

    if (!filename) filename = 'story.json'

    if (typeof data === "object") {
        data = JSON.stringify(data, undefined, 4)
    }

    var blob = new Blob([data], {
            type: 'text/json'
        }),
        e = document.createEvent('MouseEvents'),
        a = document.createElement('a')

    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
}


