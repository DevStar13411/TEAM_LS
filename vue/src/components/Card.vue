<template>
    <div class="card">
        <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
        <div class="card-body">
            <h5 class="card-title">{{item.goodName}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{category[parseInt(item.goodSmlclsCode/1000)]}}</h6>
            <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <button type="button" class="btn btn-sm btn-outline-secondary" @click="addOrder(item)">담기</button>
                </div>
                <PricePop :goodId="item.goodId"/>
            </div>
        </div>
    </div>
</template>

<script>
import PricePop from '@/components/PricePop.vue';
export default {
	name : 'ItemCard',
    components:{
        PricePop
    },
    props:{
        item: Object
    },
    data : function() {
        return {
        category : {
            30201 : "곡물가공품",
            30101 : "정육/난류",
            30202 : "수산가공품",
            30203 : "낙농/축산가공품",
            30204 : "조미료/장류/식용유",
            30102 : "채소류",
            30205 : "과자/빙과류",
            30206 : "차/음료/주류",
            30301 : "이미용품",
            30302 : "세탁/주방/가사용품",
            30103 : "생선류"}
        };
    },
    methods : {
        addOrder(item) {
            this.$store.dispatch("addOrder", item);
            console.log(item);
        }
    }   
};
</script>

<style>
.card-img-top {
  height: 15em;
  object-fit: scale-down;
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