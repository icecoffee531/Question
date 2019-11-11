<template>
  <el-row :gutter="10">
    <el-col :xs="0" :sm="1" :md="1" :lg="4" :xl="5" style="padding: 0;"><div class="grid-content bg-purple-light" style="border-bottom: 1px solid #e6e6e6; border-radius: 0;"></div></el-col>
    <el-col :xs="21" :sm="16" :md="16" :lg="13" :xl="10" style="padding: 0">
      <div class="grid-content bg-purple-light" >
        <el-row type="flex" class="row-bg" >
          <el-col :xs="13" :sm="14" :md="14" :lg=14 :xl="10">
            <div class="grid-content bg-purple-light">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" style="height: 50px">
                <el-menu-item index="1" class="active">首页</el-menu-item>
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
      <el-row type="flex" class="row-bg">
        <el-col :span="24">
          <div class="grid-content bg-purple-light" style="text-align: left">
<!--            <template slot="empty">-->

<!--            </template>-->
            <el-tabs type="border-card">
              <el-tab-pane label="推荐" name="first">
                <el-button type="primary" @click="hangshou">全部显示</el-button>
                <el-button type="success" @click="hanghide">全部隐藏</el-button>
                  <el-table  :data = "tableData.slice((currangePage-1)*pagesize, pagesize*currangePage)" style="width: 100%;"
                             :default-sort = "{prop: 'date', order: 'descending'}" :show-header="false">
                    <el-table-column style="text-align: left" :show-overflow="true">
                      <template slot-scope="scope">
                        <a href="" style="font-size: large;text-decoration: none">{{scope.row.Question}}</a><br>
                        <div>{{scope.row.Question_Detail}}</div>
                        <span type="text">{{scope.row.Qid}}</span>
                        <el-button type="text" @click="show" style="float: right;">{{scope.row.Count}}条评论</el-button>
                        <el-dialog :title="scope.row.Count" :visible.sync="dialogTableVisible">
                          <el-table :data="gridData" :show-header="false">
                            <el-table-column style="text-align: left" :show-overflow="true">
                            </el-table-column>
                          </el-table>
                        </el-dialog>
<!--                        <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">-->
<!--                          <li v-for="i in count" class="infinite-list-item">{{ i }}</li>-->
<!--                        </ul>-->
                      </template>
                    </el-table-column>
                  </el-table>
                <el-pagination style="text-align: center" layout="prev, pager, next" @current-change="current_change" :total="total" page-size="1" ></el-pagination>
              </el-tab-pane>
              <el-tab-pane label="关注" name="second" disabled>
                <el-tooltip content="敬请期待" placement="top">
                <span>配置管理</span>
                </el-tooltip>
              </el-tab-pane>
              <el-tab-pane label="热榜" name="third" disabled>角色管理</el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
      </el-row>
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
            <el-dropdown-item class="el-icon-s-custom">我的主页</el-dropdown-item>
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
        name: "Index",
        metaInfo: {
            title: '首页'
        },
        data (){
            return{
                count: 0,
                total: 20,
                pagesize: 10,
                currangePage: 1,
                username: '',
                tableData: [],
                // qid: '',
                // expends: [{'id':1}],
                activeIndex: this.$route.path,
                dialogFormVisible: false,
                dialogTableVisible: false,
                form: {
                    quest: '',
                    detail: '',
                    delivery: false,
                },
                formLabelWidth: '120px'
            }
        },
        methods: {
            Quest_confirm(){
                let params = {
                    'quest': this.form.quest,
                    'detail': this.form.detail
                };
                if (params.quest  === ''){
                    this.$message({
                        message: '问题不能为空',
                        type: "warning",
                        center: true
                    })
                }else {
                    this.$axios.post('/apis/index/',params)
                        .then(response => {
                            console.log(response.data);
                            if (response.data.success === 1){
                                this.$message({
                                    message: '发布成功',
                                    type: 'success',
                                    center: true
                                });
                                window.setTimeout("window.location='/index/'", 1000);
                            }
                        });
                    this.dialogFormVisible = false;
                    this.form.quest = '';
                    this.form.detail= '';
                }
            },
            current_change:function(currentPage) {
                this.currangePage = currentPage
            },
            set(){
                this.$router.push('/setting')
            },
            exit(){
                this.$router.push('/')
            },
            load () {
                // this.count += 2
            },
            show (){
                // alert(this.scope.row.Qid);
                // let params = {
                //     'qid': scope.row.Qid
                // };
                this.$axios.post('/apis/answer/')
                    .then(response=>{
                        console.log(response.data);
                        this.dialogTableVisible = true;
                    });
            },
            // 全部隐藏
            hanghide () {
                this.tableData = []
            },
            // 全部显示
            hangshou () {
                this.$axios.get('/apis/index/')
                    .then(response =>{
                        var len = Object.keys(response.data).length;
                        for (var i = 1; i <= len; i++){
                            this.tableData.push(response.data[i])
                        }
                        this.total=this.tableData.length/this.pagesize;
                    })
            },
        },
        created() {
            this.$axios.get('/apis/index/')
                .then(response =>{
                    var len = Object.keys(response.data).length;
                    for (var i = 1; i <= len; i++){
                        this.tableData.push(response.data[i])
                    }
                    this.total=this.tableData.length/this.pagesize;
                })
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
  .grid-content.bg-purple{
    margin: 50px auto 0;
    height: 1000px;
  }
</style>
