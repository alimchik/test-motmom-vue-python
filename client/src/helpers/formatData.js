export default function (date, format = 'dd.mm.yyyy') {
  const date2 = new Date(date)

  let dd = date2.getDate()
  dd = dd < 10 ? '0' + dd : dd

  let mm = date2.getMonth() + 1
  mm = mm < 10 ? '0' + mm : mm

  let yy = date2.getFullYear()
  yy = yy < 10 ? '0' + yy : yy

  let result = ''

  switch (format) {
    case 'dd.mm.yyyy':
      result = dd + '.' + mm + '.' + yy
      break
    case 'yyyy-mm-dd' :
      result = yy + '-' + mm + '-' + dd
      break
    default:
      break
  }

  return result
}
