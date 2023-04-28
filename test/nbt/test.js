function test(array) {
	// body...
	let a;
	for (var i = array.length - 1; i >= 0; i--) {
		a = array[i]
		...
	}
}
//
function test(array) {
	// body...
	for (var i = array.length - 1; i >= 0; i--) {
		let a = array[i]
		...
	}
}
