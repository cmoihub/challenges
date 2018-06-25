(
    function findMostFrequentInteger(array) {
        let mostFrequentInteger = 0;
        /*
        For every item in the array
        Keep track of how many times they've occurred
        */
        var pairs = {};
        for (var key of array) {
            if (pairs.hasOwnProperty(key)) {
                pairs[key] += 1;
            } else {
                pairs[key] = 0;
            }
        }
        console.log(pairs);
    }
)([1, 2, 1, 4, 4, 4, 4, 4, 5, 3, 2, 3, 6, 1, 1, 1, 7, 7]);

(
    function findPairsEqualto10(array, pairs) {
        /*
          Find pairs in an integer array whose sum is equal to 10
         */
        for (var i = 0; array.length>1;i++){
          for (var j = 1;j<array.length-1;j++){
            if ((array[i] + array[j])==10){
              console.log("pair found");
              // if items are found, add them as a sub-array to the array of pairs
              pairs.push([array[i], array[j]]);
              // remove the items so they don't need to be analyzed anymore
              array.splice(i,1);
              array.splice(j,1);
              findPairsEqualto10(array, pairs);
              // break out of inner for loop
              // break;
            } else {
              console.log("no pair");
              // remove item being analyzed so it doesn't need to be analyzed anymore
              array.splice(i,1);
              // break;
              findPairsEqualto10(array, pairs);
            }
          }
        }
        console.log(pairs);
    }
)([1, 9, 3, 8, 2, 4], []);

(
    function findPairsEqualto10Linear(array,pairs) {
      var i = 0
      for (var j = 1;j<array.length-1;j++){
            if ((array[i] + array[j])==10){
              console.log("pair found");
              // if items are found, add them as a sub-array to the array of pairs
              pairs.push([array[i], array[j]]);
              // remove the items so they don't need to be analyzed anymore
              array.splice(i,1);
              array.splice(j,1);
              findPairsEqualto10Linear(array, pairs);
            } else {
              console.log("no pair");
              // remove item being analyzed so it doesn't need to be analyzed anymore
              array.splice(i,1);
              findPairsEqualto10Linear(array, pairs);
            }
          }
          console.log(pairs);
    }
)([1, 9, 3, 4],[]);