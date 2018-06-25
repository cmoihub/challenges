(
    function findMostFrequentInteger(array) {
    let mostFrequentInteger = 0;
    /*
    For every item in the array
    Keep track of how many times they've occurred
    */
   var pairs = {};
   for (var key of array){
       if(pairs.hasOwnProperty(key)){
           pairs[key]+=1;
       } else {
           pairs[key]=0;
       }
   }
   console.log(pairs);
}
)([1,2,1,4,4,4,4,4,5,3,2,3,6,1,1,1,7,7]);

(
  function findPairsEqualto10(array){
    

  }
  )([1,9,3,4]);