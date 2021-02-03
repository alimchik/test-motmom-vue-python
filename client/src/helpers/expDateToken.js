export default function (token) {
  const beginIndex = token.indexOf('.') + 1
  const endIndex = token.indexOf('.', beginIndex)
  const publicKey = token.substring(beginIndex, endIndex)
  const expDate = JSON.parse(atob(publicKey)).exp * 1000
  return expDate
}
