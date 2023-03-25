myObject = {
  a: {
    aa: 1,
    aaa: '2'
  },
  b: {},
  c: {
    cc: {
      ccc: true
    }
  }
}

console.log(JSON.stringify(myObject, null, 4))
