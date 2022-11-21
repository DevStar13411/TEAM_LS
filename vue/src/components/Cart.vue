<template>
    <div class="card">
        <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
        <div class="card-body">
            <h5 class="card-title">{{item.goodName}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{category[parseInt(item.goodSmlclsCode/1000)]}}</h6>
            <div class="d-flex justify-content-between align-items-center">
                <button type="button" class="btn btn-sm btn-outline-secondary" @click="delOrder(item)">"삭제"</button>
                <button type="button" class="btn btn-sm btn-outline-secondary" @click="addOrder(item)">"+"</button>
                <button type="button" class="btn btn-sm btn-outline-secondary" @click="subOrder(item)">"-"</button>
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
        return{
            orderCount : 0
        }
        
        
    },
    methods : {
        addOrder(item){
            orderCount++;
            this.$emit('addOrder', orderCount);
            console.log(orderCount);
        },
        subOrder(item){
            if(orderCount > 0){
                orderCount--;
                this.$emit('subOrder', orderCount);
                console.log(orderCount);
            }
            
        },
        delOrder(item){

        }
    
    }   
};
</script>

<style>
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