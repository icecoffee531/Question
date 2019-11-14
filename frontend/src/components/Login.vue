<template>
  <div id="background">
    <div id="nav">
      <p>Q-A</p>
    </div>
    <div id="login">
      <br>
      <span>登&ensp;录</span>
    <el-form ref="form" :model="form" :rules="rules">
      <el-form-item label="用户名">
        <el-input placeholder="请输入用户名" v-model="form.user"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <label slot="label">密&ensp;&ensp;码</label>
        <el-input placeholder="请输入密码" v-model="form.password" show-password></el-input>
      </el-form-item>
      <br><br>
      <div id="LR">
        <el-button v-on:click="login" type="primary" plain>登录</el-button>
        <br><br>
        <el-button v-on:click="regist" type="primary" plain>注册</el-button>
      </div>
    </el-form>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Login",
        metaInfo:{
            title: '登录',
        },
        data (){
            return{
              form:{
                  user: '',
                  password: ''
              }
            }
        },
    methods: {
        login: function () {
            // 获取输入的用户名和密码
            let params = {
                user: this.form.user,
                password: this.form.password
            };
            // 判断用户名密码状态
            if ((params.user || params.password) === ''){
                this.$message({
                    message: '用户名密码不能为空',
                    type: "warning",
                    center: true
                });
            }else {
                // 将用户名密码post到后端
                this.$axios.post('/apis/login/',params)
                    .then(response => {
                        // 登录成功后转到对应的路由
                        if (response.data.status === 1){
                            this.$router.push({path: response.data.url})
                        } else{
                            this.$message({
                                message: '用户名或密码错误',
                                type: "error",
                                center: true
                            });
                        }
                    });
            }
        },
        // 转到注册
        regist:function(){
            this.$router.push('/regist/')
        },
    }
    }
</script>

<style>
  .el-input__icon.el-icon-view.el-input__clear{
    margin: 0;
  }
</style>

<style scoped>
  #background {
    width: 100%;
    height: 100%;
    position: absolute;
    background: url("../assets/background1.png");
    background-size: 100% 100%;
    background-attachment: fixed;
  }
  .el-form{
    height: 400px;
    padding-top: 75px;
    width: 70%;
    margin: 0 auto;
  }
  .el-form-item__label{
    color: pink;
   }
  .el-input{
    width: 220px;
  }
  #login{
    position: relative;
    width: 400px;
    height: 500px;
    background: rgba(255,255,255,0.8);
    margin: 0 auto;
    border-radius: 50px;
  }
  #login span{
    font-size: 30px;
    color: navy;
    opacity: 0.7;
  }
  .el-button{
    font-size: 20px;
    width: 88%;
    text-align: center;
  }
  #nav p{
    margin: 60px auto 0;
    font-size: 70px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    color: blueviolet;
    opacity: 0.7;
  }
  body{overflow:hidden;}
</style>
