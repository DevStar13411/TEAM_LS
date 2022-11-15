<template>
    <h1>This is Main View</h1>
    <div class="py-5">
        <div class="container text-start">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4">
                <div class="col my-2" v-for="item in goodList" v-bind:key="item.goodId">
                    <div class="card">
                        <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
                        <div class="card-body">
                            <h5 class="card-title">{{item.goodName}}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{item.goodSmlclsCode}}</h6>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <button type="button" class="btn btn-sm btn-outline-secondary" @click="itemClick(item)">담기</button>
                                </div>
                                <small class="text-muted">가격</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
	name : 'MainView',
    data : function() {
        return {
            goodList : []
        };
    },
    methods : {
        getGoodsList() {
            //this.axios.get("http://localhost:5000/goods",{
            this.axios.get("https://zzangbaguni.shop/goods",{
                params: {
                    address: this.$route.query.address,
                    latitude: this.$route.query.latitude,
                    longtitude: this.$route.query.longtitude
                }
            }).then((res)=>{
                console.log(res);
                this.goodList = res.data.goods;
            }).catch((err) => {
                console.log(err);
            });
        },
        itemClick(item) {
            this.$router.push({name : 'GoodView', query : {itemNo : item.goodId}});
        }
    },
    mounted() {//goodlist 컴포넌트가 마운트되면 getGoodList함수 호출
        this.getGoodsList();
    }
    
};
</script>

<style scoped>
.card-img-top {
  height: 15em;
  object-fit: cover;
}
.card-title {
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.4em;
  height: 2.8em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>