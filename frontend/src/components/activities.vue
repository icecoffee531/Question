<template>
<el-container >
  <el-table :data="activitiesData" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
    <el-table-column style="text-align: left" :render-header="renderHeader"  :show-overflow="true">
      <template slot-scope="scope">
        {{scope.row.activity}}
      </template>
    </el-table-column>
  </el-table>
</el-container>
</template>

<script>
    export default {
        name: "activities",
        data(){
            return{
                activitiesData: []
            }
        },
        methods:{
            renderHeader (h) {
                return [h('p', {style: 'font-size: 14px;color: black;margin:0'}, ['我的动态'])]
            }
        },
        created() {
            this.activitiesData.push({activity: '暂无动态'})
        }
    }
</script>

<style scoped>
  .el-table tbody tr:hover>td {
    background-color:#ffffff!important
  }
</style>
