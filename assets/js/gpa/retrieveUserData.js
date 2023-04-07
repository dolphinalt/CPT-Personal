function retreiveGPA() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "http://13.58.102.35/api/users/gpa", false); // false for synchronous request
    xmlHttp.send(null);
    json = JSON.parse(xmlHttp.responseText);
    return json;
}

getResult = httpGet();

console.log(getResult[0]["classes"]);