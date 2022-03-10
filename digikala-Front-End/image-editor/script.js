const preview = document.querySelector('#preview')
const previewScale = document.querySelector('#preview-scale')
const previewFlip = document.querySelector('#preview-flip')
const brightnessSlider = document.querySelector('#brightness')
const brightnessSliderValue = document.querySelector('#brightness-value')
const rotateSlider = document.querySelector('#rotate')
const rotateSliderValue = document.querySelector('#rotate-value')

let filterStack = {
  Brightnes: '',
  Filter: 'none',
}
let transformStack = {
  Fliphorizontal: 1,
  Flipvertical: 1,
  Rotate: '',
}
const filterAdd = () => {
  let transform =
    ' scale(' +
    transformStack.Fliphorizontal +
    ',' +
    transformStack.Flipvertical +
    ') ' +
    transformStack.Rotate //+
  // transformStack.Brightnes
  let filter = filterStack.Filter + filterStack.Brightnes
  preview.style.transform = transform
  preview.style.filter = filter
}
const handleRotate = () => {
  const rotate = rotateSlider.value
  rotateSliderValue.innerText = rotate
  const size = Math.abs(Math.sin(rotate)) + Math.abs(Math.cos(rotate))
  transformStack.Rotate =
    'scale(' + size.toFixed(5) + ') rotate(' + rotate + 'deg) '
  filterAdd()
}

const handleBrightness = () => {
  const brightness = brightnessSlider.value
  brightnessSliderValue.innerText = brightness
  filterStack.Brightnes = ' brightness(' + brightness + ') '
  filterAdd()
}
const filterFunction = (type) => {
  let dic = {
    grayscale: 1,
    sepia: 1,
    invert: 1,
    'hue-rotate': '90deg',
    contrast: 2,
    saturate: 2,
    blur: '2px',
  }
  return '(' + dic[type] + ')'
}
const handleFilter = (e) => {
  const { target } = e
  const { id: filter } = target

  if (filter == 'none') {
    filterStack.Filter = ''
  } else {
    filterStack.Filter = filter + filterFunction(filter)
  }
  filterAdd()
}

const handleFlip = (flip) => {
  if (flip == 'vertical') {
    transformStack.Flipvertical = transformStack.Flipvertical * -1
  } else {
    transformStack.Fliphorizontal = transformStack.Fliphorizontal * -1
  }
  filterAdd()
}

const handleMouseEnter = () => {
  console.log('mouse enter')
}

const handleMouseLeave = () => {
  // TODO: write your code here
}

const handleMouseMove = (e) => {
  const imageWidth = previewScale.offsetWidth
  const imageHeight = previewScale.offsetHeight
  const imageOffsetTop = previewScale.offsetTop
  const imageOffsetLeft = previewScale.offsetLeft
  const pageX = e.pageX
  const pageY = e.pageY

  // TODO: write your code here
}
