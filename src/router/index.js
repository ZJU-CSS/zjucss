import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/frontglass',
      component: () => import('../views/frontglass/FrontGlass')
    },
    {
      path
    }
  ]
})
