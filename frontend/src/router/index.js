import Vue from 'vue'
import Router from 'vue-router'
import regist from "@/components/regist";
import Login from "@/components/Login";
import Index from "@/components/Index";
import setting from "../components/setting";
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
      component: Index
    },
    {
      path: '/regist',
      name: 'regist',
      component: regist
    },
    {
     path: '/setting',
     name: 'setting',
     component: setting
    }
  ]
})
