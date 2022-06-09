function selectKey(key, classNameAdd, classNameRemove) {
  const elements = document.getElementsByClassName('key')
  for (let i = 0; i < elements.length; i++) {
    if (elements[i].innerHTML.toLocaleLowerCase() == key) {
      elements[i].classList.add(classNameAdd)
      elements[i].classList.remove(classNameRemove)
    }
  }
}
document.addEventListener('keydown', function (event) {
  selectKey(event.code, 'key--held', 'key--selected')
})
document.addEventListener('keyup', function (event) {
  selectKey(event.code, 'key--selected', 'key--held')
})
