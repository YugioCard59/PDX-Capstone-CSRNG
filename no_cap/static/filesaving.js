//         const fs = require('fs')
//     function hashToJson(hashHex) {
//         const hashedRandom = hashHex
//         const jsonHash = JSON.stringify(hashedRandom)
//         console.log("This is json" + jsonHash)
//         const blob = new Blob([jsonHash], {
//             type: "application/json",
//         })
//         const cleanedList = new File([jsonHash], './static/cleanedList.json', {
//             type: "application/json",
//         })
//         console.log(cleanedList)
//         return cleanedList
//         formData.append('token', jsonHash, './static/cleanedList.json')
//         console.log(formData)
//         fs.writeFile('/static/cleanedList.json', jsonHash, (err) => {
//             if (err) throw err;
//         })
    
//     }

//     <script>src="js/FileSaver.js"</script>
// <script>

//     const cleanList = document.querySelector("#clearList");
//     fetch('http://127.0.0.1:8000/static/cleanedList.json')
//         .then(function (response) {
//             return response.json()
//         })
//         .then(function (data) {
//             // console.log(data)
//             let typedArray32Array = Uint32Array.from(data, z => z * 3200); //number 3200 can be any whole number*
//             // document.write(typedArray32Array);
//             const newTypedArray = new Uint32Array(typedArray32Array);
//             self.crypto.getRandomValues(newTypedArray);
//             console.log(newTypedArray)
//             // for (const num of newTypedArray) {
//             //     numToString = num.toString()
//             //     newString = numToString.concat(numToString)
//             //     console.log(newString)
//             //     newNum = parseInt(newString)

//             newNum = newTypedArray.join("")
//             newNumnum = parseInt(newNum)

//             const text = newNum;

//             async function digestMessage(message) {
//                 const msgUint8 = new TextEncoder().encode(message);                           // encode as (utf-8) Uint8Array
//                 const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);           // hash the message
//                 const hashArray = Array.from(new Uint8Array(hashBuffer));                     // convert buffer to byte array
//                 const hashHex = hashArray.map((b) => b.toString(16).padStart(2, '0')).join(''); // convert bytes to hex string
//                 alert(hashHex)
//                 console.log("this is hash" + hashHex)
// //                 writeToFile('/static/cleanedList.json', hashHex);
// //                 // hashToJson(hashHex)
// //                 function writeToFile(fileName, str) {
// //   const file = new Blob([str], {type: 'text/plain'});
// //   const a = document.createElement('a');
// //   const url = URL.createObjectURL(file);
// //   a.href = url;
// //   a.target = fileName;
// //   document.body.appendChild(a);
// //   a.click();
// //   setTimeout(function() {
// //     document.body.removeChild(a);
// //     // window.URL.revokeObjectURL(url);
// //   }, 0);
// // }

// // writeToFile('hello.json', hashHex);
// // function writeToFile(fileName, str, static) {
// //   const file = new Blob([str], {type: 'text/plain', static});
// //   console.log(file)
// //   const a = document.createElement('a');
// //   console.log(a)
// //   const url = URL.createObjectURL(file);
// //   console.log(url)
// //   a.href = url;
// //   a.target = fileName;
// //   document.body.appendChild(a);
// // //   a.click();
// // //   setTimeout(function() {
// // //     document.body.removeChild(a);
// // //     window.URL.revokeObjectURL(url);
// // //   }, 0);
// // }

// // writeToFile('hello.txt', 'hello', 'static/');

// // function appendHex() {
// //     document.getElementById("appendMe").insertAdjacentHTML("feforeend", "<h4>{ hashHex }</h4>");
// // }
// // function saveFile(){
// //     let blob = new Blob([hashHex], {type: "application/json"});
    
// //     saveAs(blob, "/static/cleanedList.json");
// // }

// // $(document).ready(function() {
// //     $("#cleanList").click(function() {
// //         $.ajax({
// //             url: "{% url 'drawing' user %}",
// //             type: "POST",
// //             dataType: "json",
// //             data: {
// //                 url: JSON.stringify(dict), // coordinates are saved on dict
// //                 csrfmiddlewaretoken: '{{ csrf_token }}'
// //                 },
// //             success : function(json) {
// //                 alert("Drawing saved!");
// //             },
// //             error : function(xhr, errmsg, err) {
// //                 alert("Drawing could not be saved!");
// //             }
// //         });
// //     });
// // });


//                 return hashHex;

//             }
//             digestMessage(text)
//                 .then((digestHex) => console.log("this is digest" + digestHex));

//         });

//     //     const fs = require('fs')
//     // function hashToJson(hashHex) {
//     //     const hashedRandom = hashHex
//     //     const jsonHash = JSON.stringify(hashedRandom)
//     //     console.log("This is json" + jsonHash)
//     //     // const blob = new Blob([jsonHash], {
//     //     //     type: "application/json",
//     //     // })
//     //     // const cleanedList = new File([jsonHash], './static/cleanedList.json', {
//     //     //     type: "application/json",
//     //     // })
//     //     // console.log(cleanedList)
//     //     // return cleanedList
//     //     // formData.append('token', jsonHash, './static/cleanedList.json')
//     //     // console.log(formData)
//     //     fs.writeFile('/static/cleanedList.json', jsonHash, (err) => {
//     //         if (err) throw err;
//     //     })
    
//     // }

    
// </script>

                    // writeToFile('http://127.0.0.1:8000/static/cleanedList.json', hashHex);
                // hashToJson(hashHex)
//                 function writeToFile(fileName, str) {
//   const file = new Blob([str], {type: 'text/plain'});
//   const a = document.createElement('a');
//   const url = URL.createObjectURL(file);
//   a.href = url;
//   a.download = fileName;
//   document.body.appendChild(a);
//   a.click();
//   setTimeout(function() {
//     document.body.removeChild(a);
//     window.URL.revokeObjectURL(url);
//   }, 0);
// }

// writeToFile('hello.json', hashHex);
// function writeToFile(fileName, str, static) {
//   const file = new Blob([str], {type: 'text/plain', static});
//   console.log(file)
//   const a = document.createElement('a');
//   console.log(a)
//   const url = URL.createObjectURL(file);
//   console.log(url)
//   a.href = url;
//   a.target = fileName;
//   document.body.appendChild(a);
// //   a.click();
// //   setTimeout(function() {
// //     document.body.removeChild(a);
// //     window.URL.revokeObjectURL(url);
// //   }, 0);
// }

// writeToFile('hello.txt', 'hello', 'static/');

// function appendHex() {
//     document.getElementById("appendMe").insertAdjacentHTML("feforeend", "<h4>{ hashHex }</h4>");
// }
// function saveFile(){
//     let blob = new Blob([hashHex], {type: "application/json"});
    
//     saveAs(blob, "/static/cleanedList.json");
// }


