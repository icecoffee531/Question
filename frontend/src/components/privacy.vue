<template>
  <el-container>
    <span v-loading="loading"
          element-loading-text="正在开发中..."
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
          style="width:100%;margin: 30px auto"></span>
  </el-container>
</template>

<script>
    export default {
        name: "privacy",
        data(){
            return{
                loading: true
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

<style scoped>

</style>
