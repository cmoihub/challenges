/**
 * https://community.topcoder.com/stat?c=problem_statement&pm=14848
 */

var LineOff = new function() {
    this.points = "";
    this.result = 0;
    this.movesToDo = function() {
        this.result = 0;
        this.points = this.points.toLowerCase().slice(0, 49);

        if (this.onlyHasLetters(this.points)) {
            this.eval(this.result)
        }
        return this.result;
    };
    this.onlyHasLetters = function(word) {
        return /^[a-zA-Z]+$/.test(word)
    };
    this.eval = function(result) {
      
          for (i = 0; i < this.points.length - 1; i++) {
              if (this.points[i] == this.points[i + 1]) {
                  this.points = this.points.slice(0, i) + this.points.slice(i + 2);
                  result++;
                  this.result = result;
                  this.eval(result);
              }
          }
    }
}