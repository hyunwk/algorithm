const readline = require("readline");
 const std = readline.createInterface({
     input: process.stdin,
     output: process.stdout
 });

std.on('line',(line)=>{
    input = line.split(' ').map(el => Number(el));
    console.log(input[0] + input[1]);
    std.close();
}).on('close',()=>process.exit())

