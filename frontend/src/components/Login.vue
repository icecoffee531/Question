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
            let params = {
                'user':this.form.user,
                'password':this.form.password
            };
            if ((params.user || params.password) === ''){
                this.$message({
                    message: '用户名密码不能为空',
                    type: "warning",
                    center: true
                });
            }else {
                this.$axios.post('/apis/login/',params)
                    .then(response => {
                        console.log(response.data);
                        if (response.data.code === 200){
                            this.$router.push({path: '/index/'})
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
        regist:function(){
            this.$router.push('/regist/')
        },
        created() {
            this.$axios.get('/apis/login/')
                .then(response => {
                    console.log(response.data)
                })
        }
    }
    }
</script>

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
