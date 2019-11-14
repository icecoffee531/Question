<template>
  <el-row :gutter="10" >
    <el-col :xs="0" :sm="1" :md="1" :lg="4" :xl="5" style="padding: 0;"><div class="grid-content bg-purple-light" style="border-bottom: 1px solid #e6e6e6; border-radius: 0;"></div></el-col>
    <el-col :xs="21" :sm="16" :md="16" :lg="13" :xl="10" style="padding: 0">
      <div class="grid-content bg-purple-light" >
        <el-row type="flex" class="row-bg" >
          <el-col :xs="13" :sm="14" :md="14" :lg=14 :xl="10">
            <div class="grid-content bg-purple-light">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" style="height: 50px" router>
                <el-menu-item index="/home" class="active">首页</el-menu-item>
                <el-menu-item index="2" disabled>
                  <el-tooltip content="敬请期待" placement="top">
                    <span>发现</span>
                  </el-tooltip>
                </el-menu-item>
                <el-menu-item index="3" disabled>
                  <el-tooltip content="敬请期待" placement="top">
                    <span>等你来答</span>
                  </el-tooltip>
                </el-menu-item>
              </el-menu>
            </div>
          </el-col>
          <el-col :xs="10" :sm="9" :md="10" :lg=10 :xl="10">
            <div class="grid-content bg-purple-light" style="border-bottom: 1px solid #e6e6e6; border-radius: 0;" >
              <el-input placeholder="请输入内容" suffix-icon="el-icon-search" v-model="input2" style="width: 300px;" >
              </el-input>
            </div>
          </el-col>
          <el-col :xs="1" :sm="1" :md="1" :lg=4 :xl="4">
            <div class="grid-content bg-purple-light" style="border-bottom: 1px solid #e6e6e6; border-radius: 0;"></div>
          </el-col>
        </el-row>
      </div>
      <br>
      <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
        <br>
        <div class="people" style="width: 100%;padding: 30px 20px;text-align: left">
          <el-button style="float: right;padding-top: 5px" type="text" @click="edit">编辑</el-button>
          用户名：<span>{{name}}</span>
        </div>
        <el-dialog title="编辑个人资料" :visible.sync="dialogTableVisible" style="text-align: left">
          <span>用户名：{{name}}</span>
          <el-button type="text" @click="change">修改</el-button>
          <span :hidden="hide" style="padding: 0px 20px">
                  <el-input type="text" style="height: 20px;width: 150px" placeholder="请输入您的用户名" v-model="newname"></el-input>
                  <el-button type="primary" size="small" @click="name_confirm(newname)" plain>确认</el-button>
                  <el-button type="primary" size="small" plain>取消</el-button>
                </span>
        </el-dialog>
      </el-container>
      <br>
      <el-menu :default-active="activeIndex" class="el-menu-vertical-demo" mode="horizontal" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)" router>
        <el-menu-item index='/activities'>
          <template slot="title"><span style="font-size: 14px;font-weight: bold">动态</span></template>
        </el-menu-item>
        <el-menu-item index="/answers">
          <template slot="title"><span style="font-size: 14px;font-weight: bold">回答</span> {{answer_count}}</template>
        </el-menu-item>
        <el-menu-item index="/asks"><span style="font-size: 14px;font-weight: bold">提问</span> {{quit_count}}</el-menu-item>
      </el-menu>
      <router-view></router-view>
    </el-col>
    <el-col :xs="3" :sm="6" :md="6" :lg="4" :xl="5" style="padding: 0">
      <div class="grid-content bg-purple-light" style="border-bottom: 1px solid #e6e6e6; border-radius: 0;">
        <el-dropdown>
            <span class="el-dropdown-link">
              <el-avatar icon="el-icon-bell"></el-avatar>
            </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item class="el-icon-bell">消息通知</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-dropdown>
            <span class="el-dropdown-link">
              <el-avatar icon="el-icon-edit-outline" ></el-avatar>
            </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item class="el-icon-edit-outline" @click.native="dialogFormVisible = true">写问题</el-dropdown-item>
          </el-dropdown-menu>
          <el-dialog title="Question" :visible.sync="dialogFormVisible">
            <el-form :model="form">
              <el-form-item label="问题名称：" :label-width="formLabelWidth">
                <el-input v-model="form.quest" autocomplete="off" maxlength="20" placeholder="请输入问题名称" show-word-limit></el-input>
              </el-form-item>
              <el-form-item label="问题描述：" :label-width="formLabelWidth">
                <el-input type="textarea" maxlength="100" v-model='form.detail' placeholder="问题描述" show-word-limit></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="primary" @click="Quest_confirm">确 定</el-button>
            </div>
          </el-dialog>
        </el-dropdown>
        <el-dropdown>
            <span class="el-dropdown-link" >
              <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
            </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item class="el-icon-s-custom" @click.native="myself">我的主页</el-dropdown-item>
            <br>
            <el-dropdown-item class="el-icon-s-tools" @click.native="set">设置</el-dropdown-item>
            <br>
            <el-dropdown-item class="el-icon-switch-button" @click.native="exit">退出</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div >
    </el-col>
    <el-col :xs="0" :sm="1" :md="1" :lg="3" :xl="4" style="padding: 0"><div class="grid-content bg-purple-light" style="border-bottom: 1px solid #e6e6e6; border-radius: 0;"></div></el-col>
  </el-row>
</template>

<script>
    export default {
        name: "people",
        data(){
            return{
                activeIndex: this.$route.path,
                dialogFormVisible: false,
                dialogTableVisible: false,
                hide: true,
                name: '',
                newname: '',
                answer_count: '',
                quit_count: '',
                form: {
                    quest: '',
                    detail: '',
                    delivery: false,
                },
                formLabelWidth: '120px'
            }
        },
        methods:{
            edit(){
                this.dialogTableVisible = true;
                this.hide = true
            },
            change(){
                this.hide = false
            },
            myself(){
                window.location='/people'
            },
            set(){
                window.location='/setting'
            },
            exit(){
                this.$axios.post('/apis/loginout/')
                    .then(response =>{
                        if (response.data.code === 'loginout'){
                            this.$router.push('/')
                        }
                    });
            },
            name_confirm(name){
                let params = {
                    name: name
                };
                this.$axios.post('/apis/people/',params)
                    .then(response =>{
                        if (response.data.status === 'exist'){
                            this.$message({
                                message: '用户名已存在',
                                type: "warning",
                                center: true
                            })
                        }else {
                            this.$message({
                                message: '用户名修改成功',
                                type: "success",
                                center: true
                            });
                            this.dialogTableVisible = false;
                            this.name = name
                        }
                    })
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
                    }else{
                        this.$axios.get('/apis/people/')
                            .then(response=>{
                                this.name = response.data.name;
                                this.answer_count = response.data.answer_count;
                                this.quit_count = response.data.quit_count;
                            })
                    }
                })
        }
    }
</script>

<style>
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
  .item {
    margin-top: 10px;
    margin-right: 0px;
    height: 20px;
  }
  .el-dropdown-menu.el-popper{
    text-align: left;
  }
  .el-dropdown-menu.el-popper li{
    width: 70px;
  }
  .el-menu-item {
    height: 50px;
  }
  .el-input__icon.el-icon-search{
    margin: 7px;
  }
</style>

<style scoped>
  .el-dropdown {
    width: 60px;
    height: 50px;
    line-height: 50px;
  }
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
    width: 40px;
    height: 50px;
  }
  .el-menu-item {
    height: 50px;
  }
</style>
