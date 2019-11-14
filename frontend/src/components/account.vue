<template>
  <el-container>
    <el-table :data="accountDate" :show-header="false">
      <el-table-column style="text-align: left" :show-overflow="true">
        <template slot-scope="scope">
          <span style="font-weight: 500;height:39px;line-height:39px;font-size: 17px;float: left;">{{scope.row.data}}</span>
          <el-button type="text" @click="Change(scope.row.data)" style="float: right;">{{scope.row.change}}</el-button>
          <br><br>
          <el-form :hidden="pass_able" v-if="scope.row.data === '修改密码'" class="change_data" :model="ChangeForm" ref="ChangeForm" :rules="rules">
            <el-form-item prop="password">
              <el-input placeholder="请输入密码" v-model="ChangeForm.password" show-password></el-input>
            </el-form-item>
            <el-form-item prop="repassword">
              <el-input placeholder="请重新输入新密码" v-model="ChangeForm.repassword" show-password></el-input>
            </el-form-item>
            <el-button type="primary" style="width: 300px" @click="Confirm" :disabled="isAble" plain>提交</el-button>
          </el-form>
        </template>
      </el-table-column>
    </el-table>
  </el-container>
</template>

<script>
    export default {
        name: "account",
        metaInfo:{
            title: '账户与密码'
        },
        data(){
            var password = (rule, value , callback) => {
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
                accountDate: [
                    {data: '修改密码',change: '修改'},
                    {data: '绑定手机',change: '修改'},
                    {data: '绑定邮箱',change: '修改'}
                ],
                ChangeForm:{
                    password: '',
                    repassword: ''
                },
                pass_able: true,
                isAble: true,
                rules: {
                    password: [{required: true, message: '密码不能为空', trigger: 'blur'}, {validator: password, trigger: 'blur'}],
                    repassword: [{required: true, message: '密码不能为空', trigger: 'blur'}, {validator: password, trigger: 'blur'}]
                }
            }
        },
        methods:{
            Change(data){
                console.log(data);
                var len = this.accountDate.length;
                console.log(len);
                for (var i = 0;i<len;i++){
                    console.log(this.accountDate[i]);
                    if (this.accountDate[i].data === data){
                        if (this.accountDate[i].change === '修改'){
                            this.accountDate[i].change = '收起'
                        } else {
                            this.accountDate[i].change = '修改'
                        }
                        if (data === '修改密码' && this.accountDate[i].change === '收起'){
                            this.pass_able = false;
                        }else{
                            this.pass_able = true
                        }
                        if (data === '绑定手机' && this.accountDate[i].change === '收起'){
                           this.$message({
                               message: '待开发中...敬请期待',
                               type: "warning",
                               center: true
                           })
                        }
                        if (data === '绑定邮箱' && this.accountDate[i].change === '收起'){
                            this.$message({
                                message: '待开发中...敬请期待',
                                type: "warning",
                                center: true
                            })
                        }
                    }
                }
            },
            Confirm(){
                if (this.ChangeForm.password === '' && this.ChangeForm.repassword === ''){
                    this.$message({
                        message: '新密码不能为空',
                        type: "warning",
                        center: true
                    });
                }else if (this.ChangeForm.password === this.ChangeForm.repassword){
                    let params = {
                        password: this.ChangeForm.password
                    };
                    console.log(params.password);
                    this.$axios.post('/apis/change_password/',params)
                        .then(response => {
                            if (response.data.code === 200){
                                this.$message({
                                    message: '修改密码成功',
                                    type: "success",
                                    center: true
                                });
                                this.ChangeForm.password = '';
                                this.ChangeForm.repassword = '';
                            }else {
                                this.$message({
                                    message: '出现未知错误',
                                    type: "error",
                                    center: true
                                });
                            }
                        });
                }else{
                    this.$message({
                        message: '两次输入的密码不一致',
                        type: "error",
                        center: true
                    })
                }
            }
        },
        created() {
            this.$axios.get('/apis/index/')
                .then(response =>{
                    if (response.data.status === 0){
                        this.$router.push(response.data.url);
                        this.$message({
                            message: response.data.msg,
                            type: "warning",
                            center: true
                        })
                    }
                })
        }
    }
</script>

<style>
  .change_data .el-form-item.is-required .el-form-item__content .el-input.el-input--suffix .el-input__inner{
    border-radius: 0;
    width: 300px;
    margin: 0;
}
  .change_data .el-input--suffix{
    width: 300px;
  }
  .change_data .el-input--suffix .el-input__suffix span i {
    margin: 0;
  }
</style>
