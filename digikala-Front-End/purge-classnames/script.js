function convertToAll(arr, string) {
  let res = arr.map((x) => {
    const firstSt = x[0]
    if (firstSt.startsWith(string)) {
      if (
        firstSt == string + 't' ||
        firstSt == string + 'b' ||
        firstSt == string + 'l' ||
        firstSt == string + 'r'
      )
        return firstSt + '-' + x[1]
      else if (firstSt == string + 'y')
        return [string + 't-' + x[1], string + 'b-' + x[1]]
      else if (firstSt == string + 'x')
        return [string + 'l-' + x[1], string + 'r-' + x[1]]
      else
        return [
          string + 't-' + x[1],
          string + 'b-' + x[1],
          string + 'l-' + x[1],
          string + 'r-' + x[1],
        ]
    }
  })

  return [].concat(...res)
}
const convertSplitTBRL = (arr) => {
  if (!arr || arr.length == 0) return
  const arrNew = arr.map((x) => x.split('-'))
  let arrNewT = arrNew.filter((x) => x[0].endsWith('t')).slice(-1)
  if (arrNewT.length > 0) arrNewT = arrNewT[0][0] + '-' + arrNewT[0][1]

  let arrNewB = arrNew.filter((x) => x[0].endsWith('b')).slice(-1)
  if (arrNewB.length > 0) arrNewB = arrNewB[0][0] + '-' + arrNewB[0][1]
  let arrNewL = arrNew.filter((x) => x[0].endsWith('l')).slice(-1)
  if (arrNewL.length > 0) arrNewL = arrNewL[0][0] + '-' + arrNewL[0][1]
  let arrNewR = arrNew.filter((x) => x[0].endsWith('r')).slice(-1)
  if (arrNewR.length > 0) arrNewR = arrNewR[0][0] + '-' + arrNewR[0][1]

  return [arrNewT, arrNewB, arrNewL, arrNewR].filter((x) => x.length > 0)
}
const convert4 = (arr, string) => {
  if (!arr || arr.length == 0) return []
  const arrNew = arr.map((x) => x.split('-'))
  const T = arrNew.filter((x) => x[0].endsWith('t')).slice(-1)
  const B = arrNew.filter((x) => x[0].endsWith('b')).slice(-1)
  const L = arrNew.filter((x) => x[0].endsWith('l')).slice(-1)
  const R = arrNew.filter((x) => x[0].endsWith('r')).slice(-1)
  res = []
  if (T.length > 0 && B.length > 0 && T[0][1] == B[0][1])
    res.push(string + 'y-' + T[0][1])
  else {
    if (T.length > 0) res.push(string + 't-' + T[0][1])
    if (B.length > 0) res.push(string + 'b-' + B[0][1])
  }
  if (L.length > 0 && R.length > 0 && L[0][1] == R[0][1])
    res.push(string + 'x-' + L[0][1])
  else {
    if (L.length > 0) res.push(string + 'l-' + L[0][1])
    if (R.length > 0) res.push(string + 'r-' + R[0][1])
  }
  return [...res].filter((x) => x.length > 0) //.map((x) => x.join('-'))
}
const convert2 = (arr, string) => {
  if (!arr || arr.length == 0) return []
  const arrNew = arr.map((x) => x.split('-'))
  const XY = arrNew.filter((x) => x[0].endsWith('x') || x[0].endsWith('y'))
  res = arrNew.filter((x) => !(x[0].endsWith('x') || x[0].endsWith('y')))
  if (XY.length > 1 && XY[0][1] == XY[1][1]) {
    res.push(string + '-' + XY[0][1])
  }
  return res
}
function marginPaddingName(arr) {
  let M = convertSplitTBRL(convertToAll(arr, 'm'))
  let resM = convert2(convert4(M, 'm'), 'm').join(' ')

  // let P = convertSplitTBRL(convertToAll(arr, 'p'))
  // let resP = convert2(convert4(P, 'p'), 'p').join(' ')
  return resM //+ ' ' + resP
}
function displayName(arr) {
  let newArr = arr.filter((x) => x[0].startsWith('d'))
  if (newArr.length > 0)
    return newArr.slice(-1)[0][0] + '-' + newArr.slice(-1)[0][1]
  return ''
}
function purgeClassNames(...classNames) {
  let classNameSplit = classNames
    .map((x) => x.split('-'))
    .filter((x) => x.length == 2)

  res = marginPaddingName(classNameSplit) + ' ' + displayName(classNameSplit)

  return res
}

document.getElementById('input').onkeyup = function () {
  document.getElementById('output').innerHTML = purgeClassNames(
    ...this.value.trim().split(/\s+/)
  )
}
