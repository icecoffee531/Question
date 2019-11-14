<template>
  <el-container >
    <el-table :data="asksData" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)" :show-header="false">
      <el-table-column style="text-align: left" :render-header="renderHeader"  :show-overflow="true">
        <template slot-scope="scope">
          <el-button style="float: right;padding: 50px 0 " type="text" @click="Delete(scope.row.Qid)">删除</el-button>
          <span style="float: right"></span>
          <p class="quest">提问时间：{{scope.row.Question_Date}}</p>
          <p class="quest">问题：{{scope.row.Question}}</p>
          <p class="quest">回答次数：{{scope.row.Count}}</p>
        </template>
      </el-table-column>
    </el-table>
  </el-container>
</template>

<script>
    export default {
        name: "asks",
        data(){
            return{
                asksData: [],
            }
        },
        methods:{
            Delete(qid){
                this.$confirm('此操作将永久删除该问题, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning',
                    center: true
                }).then(() => {
                    let params = {
                        qid :qid
                    };
                    this.$axios.post('/apis/delete/', params)
                        .then(response=>{
                            console.log(response.data)
                        });
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            }
        },
        created() {
            this.$axios.get('/apis/people/')
                .then(response=>{
                    //
                    var len = Object.keys(response.data.asks).length;
                    for (var i=0; i<len; i++){
                        this.asksData.push(response.data.asks[i])
                    }
                })
        }
    }
</script>

<style>
.quest{
  width: 200px;
}
</style>
