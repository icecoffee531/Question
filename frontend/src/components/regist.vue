<template>
  <div id="background">
    <div id="regist">
      <br>
      <span>注&ensp;册</span>
      <el-form ref="form"  :model="form" :rules="rules">
        <el-form-item label="用户名" prop="user">
          <label slot="label">用户名&ensp;&ensp;</label>
          <el-input placeholder="请输入用户名" v-model="form.user"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password1">
          <label slot="label">密&ensp;&ensp;码&ensp;&ensp;</label>
          <el-input placeholder="请输入密码" v-model="form.password1" show-password></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password2">
          <el-input placeholder="请输入密码" v-model="form.password2" show-password></el-input>
        </el-form-item>
        <br>
        <div id="LR">
          <el-button v-on:click="finish" type="primary" :disabled="isAble" plain>确认</el-button>
          <br><br>
          <el-button v-on:click="reset" type="primary" plain>重置</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
    export default {
        name: "regist",
        metaInfo:{
            title: '注册'
        },
        data(){
            var user = (rule, value , callback) => {
                if (value.length < 6){
                    callback(new Error('用户名长度不得小于6位'));
                    this.isAble = true
                }else{
                    this.isAble = false;
                }
            };
            var password1 = (rule, value, callback) => {
                if (value.length < 6){
                    callback(new Error('密码长度不能小于6位'));
                    this.isAble = true
                }else if(value.length > 18){
                    callback(new Error('密码长度不能大于18位'));
                    this.isAble = true
                }else{
                    this.isAble = false;
                }
            };
            return{
                form: {
                    user: '',
                    password1: '',
                    password2: '',
                    // isAble: true
                },
                rules: {
                    user:[{required: true, message: '这是必填项', trigger: 'blur'}, {validator: user, trigger: 'blur'}],
                    password1:[{required: true, message: '这是必填项', trigger: 'blur'}, {validator: password1, trigger: 'blur'}],
                    password2:[{required: true, message: '这是必填项', trigger: 'blur'}, {validator: password1, trigger: 'blur'}],
                },
                isAble: true
            }
        },
        methods: {
            finish: function () {
                let params = {
                    user: this.form.user,
                    password1: this.form.password1,
                    password2: this.form.password2
                };
                if (params.user === '' || params.password1 === '' || params.password2 === ''){
                    this.$message({
                        message: '用户名密码不能为空',
                        type: "error",
                        center: true
                    })
                } else {
                    this.$axios.post('/apis/regist/', params)
                        .then(response =>{
                            console.log(response.data);
                            if (response.data.code === 23) {
                                this.$message({
                                    message: '用户名已存在',
                                    type: "warning",
                                    center: true
                                });
                            } else if (response.data.code === 24){
                                this.$message({
                                    message: '两次输入的密码不一致',
                                    type: "error",
                                    center: true
                                })
                            } else if (response.data.code === 'finish'){
                                this.$message({
                                    message: '注册成功，正在跳转到登录界面',
                                    type: "success",
                                    center: true
                                });
                                window.setTimeout("window.location='/'",2000);
                            }
                        });
                    }
            },
            reset: function () {
                this.form.user = '';
                this.form.password1 = '';
                this.form.password2 = '';
                this.isAble = true
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
    /*padding-top: 100px;*/
    width: 80%;
    margin:40px auto 0;
  }
  .el-form-item__label{
    color: pink;
    text-align: left;
  }
  .el-input{
    width: 220px;
  }
  #regist{
    position: relative;
    width: 400px;
    height: 500px;
    background: rgba(255,255,255,0.8);
    margin: 125px auto;
    border-radius: 50px;
  }
  .el-button{
    font-size: 20px;
    width: 78%;
    text-align: center;
  }
  #regist span{
    font-size: 30px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    color: navy;
    opacity: 0.7;
  }
</style>
