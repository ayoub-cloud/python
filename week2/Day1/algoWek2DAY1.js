
 var arr=  ["q","b","c","d","e","f","g","h","i","j"]
function makeFrequencyTable(arr) {
    var frequencyTable = {};
 
    for (var i = 0; i < arr.length; i++) {
     var obj = arr[i];
  
      if (frequencyTable[obj]) {
        frequencyTable[obj]++;
      } else {
        frequencyTable[obj] = 1;
      }
    }
  
    return frequencyTable;
  }
  


console.log(makeFrequencyTable(arr));
