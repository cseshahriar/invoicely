import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount'
import Clients from '../views/dashboard/Clients.vue'
import Client from '../views/dashboard/Client.vue'
import AddClient from '../views/dashboard/AddClient.vue'
import EditClient from '../views/dashboard/EditClient.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'

import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/clients',
    name: 'Clients',
    component: Clients,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/client/:id',
    name: 'Client',
    component: Client,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/client/:id/edit',
    name: 'EditClient',
    component: EditClient,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/dashboard/client/add',
    name: 'AddClient',
    component: AddClient,
    meta: {
      requiredLogin: true
    }
  },  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiredLogin) && !store.state.isAuthenticated) {
    next({name: 'LogIn', query: {to: to.path }})
  } else {
    next()
  }
})

export default router
