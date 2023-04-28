#!/usr/bin/env node
const fs = require("fs");
fs.writeFile(process.argv[2], process.argv[3], (error, data) => {
    if (error) console,log(error);
})