

// TODO: make the datasetMap array be derived from an obj that represents any imported csv

// BELOW: makes a Uint32Array that is a type of typedArray which is param for Crypto.getRandomValues(typedArray)
// let cleanList = document.getElementById("cleanList").value;
// const cleanList = [0.0839, 0.00836, 0.4586, 0.1258, 0.1121, 0.2563]  //these are example numbers in the array
let typedArray32Array = Uint32Array.from(cleanList, z => z * 3200); //number 3200 can be any whole number*
document.write(typedArray32Array);

//BELOW: implements .getRandomValues() a method returns cryptographically strong random numbers; it uses a 
//pseudo-random number generator algorithm (PRNG) that varies across user agents**
const newTypedArray = new Uint32Array(typedArray32Array);
self.crypto.getRandomValues(newTypedArray);
for (const num of newTypedArray) {
    console.log(num)
}

