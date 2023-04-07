// fetch the data from API
fetch("https://seal.nighthawkcodingsociety.com/api/users/time", read_options)
    // response is a RESTful "promise" on any successful fetch
    .then(response => {
    // check for response errors
    if (response.status !== 200) {
        const errorMsg = 'Database read error: ' + response.status;
        console.log(errorMsg);
        return;
    }
    // valid response will have json data
    response.json().then(data => {
        for (let i = 0; i<data.length; i++) {
            var totaltime = 0;
            if (i == id) {
                for (let j=0; j<data[i]["tasks"].length; j++) {
                    totaltime = totaltime + parseInt(data[i]["times"][j]);
                    
            }
            }
        }
    })
})
// catch fetch errors (ie ACCESS to server blocked)
.catch(err => {
    console.error(err);
});

