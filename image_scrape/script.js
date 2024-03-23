// Imports
const cheerio = require('cheerio');
const request = require('request');
const fs = require('fs');

// Create a Write Stream
var WriteStream = fs.createWriteStream("C:/dark-patterns-recognition-master/image_scrape/ImagesLink.txt", "UTF-8");

request('https://www.flipkart.com/', (err, resp, html) => {

    if (!err && resp.statusCode == 200) {
        console.log("Request was successful ");

        // Define Cheerio or $ Object
        const $ = cheerio.load(html);

        $("img").each((index, image) => {
            // Check if 'src' attribute exists before accessing it
            var imgSrc = $(image).attr('src');
            if (imgSrc) {
                var baseUrl = 'https://www.flipkart.com/';

                // Check if the image URL is already absolute
                var absoluteUrl = imgSrc.startsWith('http') ? imgSrc : baseUrl + imgSrc;

                WriteStream.write(absoluteUrl);
                WriteStream.write("\n");
            }
        });

    } else {
        console.log("Request Failed ");
    }

});
