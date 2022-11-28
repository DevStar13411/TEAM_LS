<template>
    <div class="card">
        <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
        <div class="card-body">
            <h5 class="card-title">{{item.goodName}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{category[parseInt(item.goodSmlclsCode/1000)]}}</h6>
            <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <!-- <button v-if = "notInCart(item)" type="button" class="btn btn-sm btn-outline-secondary" @click="addOrder(item)">담기</button> -->
                    <!-- 장바구니에 있으면 비활성화 -->
                    <!-- <button  type="button" v-if = "canAddToCart(item)" class="btn btn-sm btn-outline-secondary" @click="addOrder(item)">담기</button> -->
                    <!-- <button  type="button" disabled ="true" class="btn btn-sm btn-outline-secondary" v-else>담기</button> -->
                    <button type="button" class="btn btn-sm btn-outline-secondary" @click="[addOrder(item), openModal()]">담기</button>
                </div>
                <PricePop :goodId="item.goodId"/>
            </div>
        </div>
    </div>


    <MyModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p>알림</p>
      <div>{{item.goodName}}을(를) 장바구니에 담았습니다</div>
      <!-- /default -->
      <!-- footer 슬롯 콘텐츠 -->
      <!-- /footer -->
    </MyModal>
</template>

<script>
import PricePop from '@/components/PricePop.vue';
import MyModal from './MyModal.vue';

export default {
	name : 'ItemCard',
    components:{
        PricePop,
        MyModal
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
            30103 : "생선류",
            30304 : "기타",
            30305 : "기타"},
        modal : false,
        message : ''
        };
    },

    methods : {
        addOrder(item) {
            this.$store.dispatch("addOrder", item);
            // alert(item.goodName + " 이(가) 장바구니에 추가되었습니다.");
            console.log("item = ", item);
            console.log("방금 담은 item: " + this.$store.getters.getcartProducts.find(element => element.goodId === item.goodId).elem);
            // console.log("item Quantity = " + item.goodQuantity);
        },
        canAddToCart(item){
            // 카트에 없다 == 담을 수 있다.
            const flag = this.$store.getters.getcartProducts.find(element => element.goodId === item.goodId);
            if(!flag){
                return true;
            }else{
                return false;
            }
        },
        openModal() {
            this.modal = true;
        },
        closeModal() {
        this.modal = false;
        },
        doSend() {
        if (this.message.length > 0) {
            alert(this.message);
            this.message = '';
            this.closeModal();
        } else {
            alert('메시지를 입력해주세요.');
        }
        }
    }   
};
</script>

<style>

.card{
box-shadow: 0 3.2px 2.2px rgba(0, 0, 0, 0.02),
    0 7px 5.4px rgba(0, 0, 0, 0.028), 0 12.1px 10.1px rgba(0, 0, 0, 0.035),
    0 19.8px 18.1px rgba(0, 0, 0, 0.042), 0 34.7px 33.8px rgba(0, 0, 0, 0.05),
    0 81px 81px rgba(0, 0, 0, 0.07);
}

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