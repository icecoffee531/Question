<template>
  <el-container>
    <el-table :data="notificationData">
      <el-table-column style="text-align: left"  :render-header="renderHeader" :show-overflow="true">
        <template slot-scope="scope">
          <div>
            <el-button type="text" style="float: right;" @click="Change(scope.row.id)">{{scope.row.change}}</el-button>
            <div style="font-weight: bold;font-size: 15px;color: black;width: 570px">{{scope.row.title}}</div>
            <p>{{scope.row.data}}</p>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </el-container>
</template>

<script>
    export default {
        name: "notification",
        metaInfo:{
            title: '消息与邮件'
        },
        data(){
            return{
                notificationData:[
                    {id: 1, title: '私信设置', data: '允许谁给我发私信', change: '编辑'},
                    {id: 2, title: '邀请/评论消息设置', data: '有人对我发出邀请时，我会收到消息通知', change: '编辑'},
                    {id: 3, title: '赞同/赞赏消息设置', data: '有人对我赞同或赞赏时，我会收到消息通知', change: '编辑'},
                    {id: 4, title: '关注消息设置', data: '我的关注有新动态时，我会收到消息通知', change: '编辑'},
                    {id: 5, title: '邮件设置', data: '重要事件发生时，我将会收到邮件提醒', change: '编辑'}
                ]
            }
        },
        methods:{
            renderHeader (h) {
                return [h('h1', {}, ['消息与邮件']),h('p', {}, ['私信设置/邀请设置/赞同与赞赏/关注/邮件设置'])]
            },
            Change(id){
                this.$message({
                    message: '尚未完成...敬请期待',
                    type: "warning",
                    center: true
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
                    }
                })
        }
    }
</script>

<style>
  .cell {
    padding: 20px 18px;
  }
  .cell h1{
    font-size: 19px;
    font-weight: bold;
    color: black;
    margin: 0;
  }
  .cell p{
    width: 570px;
    font-size: 14px;
    font-weight: 100;
    color: #8590A6;
    margin: 5px 0 0 0;
  }
</style>
