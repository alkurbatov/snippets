// NOTE (alkurbatov): 12096e5 is a magic number,
// represents count of milliseconds in two weeks.
const past = new Date(Date.now() - 12096e5)

console.log(past.toString())
