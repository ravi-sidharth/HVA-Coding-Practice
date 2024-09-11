function getMillisecondsBetween(date1, date2) {
    let milli1= date1.getTime()
    console.log(milli1)
    let milli2= date2.getTime()
    console.log(milli2)

    return Math.abs(milli1-milli2)
}

let date1=new Date("2005-03-02T10:01:15.000Z")
let date2 =new Date("2005-03-02T10:00:05.000Z")

console.log(getMillisecondsBetween(date1,date2))