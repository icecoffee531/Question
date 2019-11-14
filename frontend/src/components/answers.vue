<template>
  <el-container >
    <el-table :data="answersData" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)" :show-header="false">
      <el-table-column style="text-align: left" :render-header="renderHeader"  :show-overflow="true">
        <template slot-scope="scope">
          <el-button style="float: right;padding: 3px 0 " type="text" @click="Delete(scope.row.aid)">删除</el-button>
          <span style="float: right">问题: {{scope.row.question}}</span>
          {{scope.row.answer_detail}}
        </template>
      </el-table-column>
    </el-table>
  </el-container>
</template>

<script>
    export default {
        name: "answers",
        data(){
            return{
                answersData: [],
            }
        },
        methods:{
          Delete(aid){
              this.$confirm('此操作将永久删除该问题, 是否继续?', '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning',
                  center: true
              }).then(() => {
                  let params = {
                      aid :aid
                  };
                  this.$axios.post('/apis/delete/', params)
                      .then(response=>{
                          console.log(response.data);
                          if (response.data.status === 'success'){
                              this.$message({
                                  type: 'success',
                                  message: '删除成功!',
                                  center: true
                              });
                          }else {
                              this.$message({
                                  type: 'error',
                                  message: '删除失败，出现未知错误!',
                                  center: true
                              });
                          }
                      });
              }).catch(() => {
                  this.$message({
                      type: 'info',
                      message: '已取消删除',
                      center: true
                  });
              });
          }
        },
        created() {
            this.$axios.get('/apis/people/')
                .then(response=>{
                    //
                    var len = Object.keys(response.data.answer_detail).length;
                    for (var i=0; i<len; i++){
                        this.answersData.push(response.data.answer_detail[i])
                    }
                })
        }
    }
</script>

<style scoped>

</style>
