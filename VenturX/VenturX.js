//import the Express framework:
const express = require('express');

// Creates the Express app:
const app = express();

//Setting the port:
const port = 3000;

app.use(express.static('VenturX'));
app.get('/index.htm', function (req, res) {
    res.sendFile( __dirname + "/" + "index.htm" );
 })
// Now, we can create a simple GET endpoint. We'd like to set it to be on the home page, so the URL for the endpoint is /:
app.get('/process_get', (req, res) => {
    // Prepare output in JSON format
   response = {
    name:req.query.name
 };
 console.log(response);
 res.end(JSON.stringify(response));
})

app.listen(port, () => console.log(`Hello, VentureX app listening on port ${port}!`))


   