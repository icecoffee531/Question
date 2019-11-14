<template>
  <el-row type="flex" class="row-bg">
      <el-col :span="24">
        <div class="grid-content bg-purple-light" style="text-align: left">
          <el-tabs type="border-card">
            <el-tab-pane label="推荐" index="1">
              <el-table  :data = "tableData.slice((currangePage-1)*pagesize, pagesize*currangePage)" style="width: 100%;"
                         :default-sort = "{prop: 'date', order: 'descending'}" :show-header="false">
                <el-table-column style="text-align: left" :show-overflow="true">
                  <template slot-scope="scope">
                    <a href="" style="font-size: large;text-decoration: none">{{scope.row.Question}}</a><br>
                    <div>{{scope.row.Question_Detail}}</div>
                    <el-button type="text" @click="show(scope.row.Qid)" style="float: right;">{{scope.row.Count}}条评论</el-button>
                    <el-dialog title="所有评论" :visible.sync="dialogTableVisible">
                      <el-table :data="gridData" :show-header="false">
                        <el-table-column style="text-align: left" :show-overflow="true">
                          <template slot-scope="scope">
                            <a href="" style="text-decoration: none">{{scope.row.username}}</a>
                            <span style="float: right;color: #8590a6">{{scope.row.answer_date}}</span><br>
                            {{scope.row.answer_detail}}
                          </template>
                        </el-table-column>
                      </el-table>
                      <el-input style="width: 89%" v-model="detail"></el-input>
                      <el-button type="primary" @click="Release">
                        发布
                      </el-button>
                    </el-dialog>
                  </template>
                </el-table-column>
              </el-table>
              <el-pagination style="text-align: center" layout="prev, pager, next" @current-change="current_change" :total="total" page-size="1" ></el-pagination>
            </el-tab-pane>
            <el-tab-pane label="关注" index="2" disabled>
              <el-tooltip content="敬请期待" placement="top">
                <span>配置管理</span>
              </el-tooltip>
            </el-tab-pane>
            <el-tab-pane label="热榜" index="3" disabled>角色管理</el-tab-pane>
          </el-tabs>
        </div>
      </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "home",
        data (){
            return{
                total: 20,
                pagesize: 10,
                currangePage: 1,
                detail: '',
                tableData: [],
                gridData: [],
                isable: false,
                dialogTableVisible: false,
            }
        },
        methods: {
            current_change:function(currentPage) {
                this.currangePage = currentPage
            },
            Release(){
                let params = {
                    'detail': this.detail
                };
                if (params.detail === ''){
                    this.$message({
                        message: '发布的回答不能为空',
                        type: 'error',
                        center: true
                    })
                }else{
                    this.$axios.post('/apis/answer/', params)
                        .then(response =>{
                            console.log(response.data);
                            if (response.data.code === 'finish'){
                                this.$message({
                                    message: '发布成功',
                                    type: "success",
                                    center: true,
                                });
                                window.setTimeout("window.location='/index/'",2000);
                                this.dialogTableVisible = false
                            }else{
                                this.$message({
                                    message: '出现未知错误',
                                    type: "error",
                                    center: true
                                })
                            }
                        })
                }
            },
            show (qid){
                let params = {
                    'qid': qid
                };
                this.$axios.post('/apis/answer_detail/',params)
                    .then(response=>{
                        this.gridData = [];
                        console.log(response.data);
                        var len = Object.keys(response.data).length;
                        for (var i = 1; i<= len; i++){
                            this.gridData.push(response.data[i]);
                        }
                        this.dialogTableVisible = true;
                    });
            },
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
                        var len = Object.keys(response.data).length;
                        console.log(len);
                        for (var i = 1; i <= len; i++){
                            this.tableData.push(response.data[i])
                        }
                        this.total=this.tableData.length/this.pagesize;
                    }
                })
        }
    }
</script>

<style>
  .cell {
    text-align: left;
  }
  .el-table tbody tr:hover>td {
    background-color:#ffffff!important
  }
  /*.el-dropdown-menu.el-popper.el-dropdown-menu--mini li{*/
  /*  width: 40px*/
  /*}*/
</style>
