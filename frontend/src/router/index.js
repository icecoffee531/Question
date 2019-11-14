import Vue from 'vue'
import Router from 'vue-router'
import regist from "@/components/regist";
import Login from "@/components/Login";
import Index from "@/components/Index";
import home from "../components/home";
import setting from "../components/setting";
import people from "../components/people";
import activities from "../components/activities";
import answers from "../components/answers";
import asks from "../components/asks";
import account from "../components/account";
import notification from "../components/notification";
import filter from "../components/filter";
import privacy from "../components/privacy";
import preference from "../components/preference";
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/index',
      name: 'Index',
      component: Index,
      redirect: '/home',
      children:[
        {
          path: '/home',
          name: 'home',
          component: home,
        }
      ]
    },
    {
      path: '/regist',
      name: 'regist',
      component: regist
    },
    {
      path: '/setting',
      name: 'setting',
      component: setting,
      redirect: '/account',
      children:[
        {
          path: '/account',
          name: 'account',
          component: account
        },
        {
          path: '/notification',
          name: 'notification',
          component: notification
        },
        {
          path: '/filter',
          name: 'filter',
          component: filter
        },
        {
          path: '/privacy',
          name: 'privacy',
          component: privacy
        },
        {
          path: '/preference',
          name: 'preference',
          component: preference
        }
      ]
    },
    {
      path: '/people',
      name: 'people',
      component: people,
      redirect: "/activities",
      children:[
        {
          path: '/activities',
          name: 'activities',
          component: activities
        },
        {
          path: '/answers',
          name: 'answers',
          component: answers
        },
        {
          path: '/asks',
          name: 'asks',
          component: asks
        }

      ]
    }
  ]
})
