import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/frontglass',
      component: () => import('../views/frontglass/FrontGlass'),
    },
    {
      path: '/test',
      component: () => import('../views/test.vue'),
    },
    {
      path: '/magicmirror',
      component: () => import('../views/magicmirror/Main'),
      children: [
        {
          path: 'page1',
          component: () => import('../components/magicmirror/Page1'),
        },
      ],
    },
    {
      path: '/upload',
      component: () => import('../views/upload.vue'),
    },
  ],
})
