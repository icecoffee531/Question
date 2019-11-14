<template>
  <el-row :gutter="10">
    <el-col :xs="0" :sm="1" :md="1" :lg="5" :xl="5" style="padding: 0;"><div class="grid-content bg-purple-light" style="border-bottom: 0; border-radius: 0;"></div></el-col>
    <el-col :xs="21" :sm="16" :md="16" :lg="13" :xl="10" style="padding: 0">
      <div class="grid-content bg-purple-light" >
        <el-row type="flex" class="row-bg" >
          <el-col :xs="13" :sm="14" :md="14" :lg=14 :xl="10">
            <div class="grid-content bg-purple-light"></div>
          </el-col>
          <el-col :xs="10" :sm="9" :md="10" :lg=10 :xl="10">
            <div class="grid-content bg-purple-light" style="border-bottom: 0px solid #e6e6e6; border-radius: 0;" ></div>
          </el-col>
          <el-col :xs="1" :sm="1" :md="1" :lg=4 :xl="4">
            <div class="grid-content bg-purple-light" style="border-bottom: 0px solid #e6e6e6; border-radius: 0;"></div>
          </el-col>
        </el-row>
      </div>
      <el-row type="flex" class="row-bg">
        <el-col :span="24">
          <div class="grid-content bg-purple-light" style="text-align: left;">
            <el-header style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
              <br>
              <el-page-header @back="goBack" content="设置" ></el-page-header>
            </el-header>
            <br>
            <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
              <el-aside width="200px">
                <el-menu  :default-active="$route.path" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" router>
                  <el-menu-item index="/account">
                    <template slot="title"><i class="el-icon-user"></i>账户与密码</template>
                  </el-menu-item>
                  <el-menu-item index="/notification">
                    <template slot="title"><i class="el-icon-bell"></i>消息与邮件</template>
                  </el-menu-item>
                  <el-menu-item index="/filter">
                    <template slot="title"><i class="el-icon-circle-close"></i>屏蔽</template>
                  </el-menu-item>
                  <el-menu-item index="/privacy">
                    <template slot="title"><i class="el-icon-lock"></i>隐私</template>
                  </el-menu-item>
                  <el-menu-item index="/preference">
                    <template slot="title"><i class="el-icon-setting"></i>偏好设置</template>
                  </el-menu-item>
                </el-menu>
              </el-aside>
              <el-main style="padding: 0"><router-view></router-view></el-main>
            </el-container>
          </div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="3" :sm="6" :md="6" :lg="4" :xl="5" style="padding: 0">
      <div class="grid-content bg-purple-light" style="border-bottom: 0; border-radius: 0;"></div >
    </el-col>
    <el-col :xs="0" :sm="1" :md="1" :lg="2" :xl="4" style="padding: 0"><div class="grid-content bg-purple-light" style="border-bottom: 0; border-radius: 0;"></div></el-col>
  </el-row>
</template>

<script>
    export default {
        name: "setting",
        methods:{
            goBack(){
                this.$router.push('/index')
            }
        }
    }
</script>

<style>
  .cell {
    text-align: left;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 50px;
  }
  .grid-content.bg-purple-dark{
    width: 100%;
    height: 50px;
    border-bottom: 1px solid #e6e6e6;
  }
  .grid-content.bg-purple-light .el-input.el-input--suffix .el-input__inner{
    height: 35px;
    width: 300px;
    border-radius: 2px;
    margin-top: 10px;
  }
  i{
    margin: 7px;
  }
  .item {
    margin-top: 10px;
    margin-right: 0px;
    height: 20px;
  }
  .el-dropdown-menu.el-popper{
    text-align: left;
  }
  .el-dropdown-menu.el-popper.el-dropdown-menu--mini li{
    width: 40px
  }
  .el-dropdown-menu.el-popper li{
    width: 70px;
  }
  .el-menu-item {
    height: 50px;
  }
  .el-table tbody tr:hover>td {
    background-color:#ffffff!important
  }
</style>
