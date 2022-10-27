import axios from 'axios'
function http(config) {
  const instance = axios.create({
    timeout: 30000,
  })
  return instance(config)
}
export default http
