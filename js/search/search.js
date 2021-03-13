let array = [2,3,4,5,6,7];
let element = 5;


function linearSearch(array, element) {
    for (i = 0; i < array.length; i++) {
        if (element == array[i]){
            return i;
        }
    }
    return null;
}

index = linearSearch(array, element);
console.log("Array = " + array)
console.log("Element to Find = " + element)
console.log(element + " was found at index " + index);
