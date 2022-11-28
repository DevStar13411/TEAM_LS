<template>
    <div class="card">
        <div  style="position: relative;">
            <img style="position: relative;" class="card-img-top p-3" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
            <div>
                <div style="position: absolute; bottom: 5%; right: 5%;">
                    <img src="@/assets/cart.png" style="height: 50px; width: 50px; cursor: pointer;" @click="[addOrder(item), openModal()]">
                </div>
            </div>
        </div>
        <div class="card-body">
            <h6 class="card-title">{{item.goodName}}</h6>
            <h6 class="card-subtitle mb-2">
                {{category[parseInt(item.goodSmlclsCode/1000)]}}
            </h6>
            <PricePop :goodId="item.goodId" />
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
.card {
    /* border-color: transparent; */
    /* border-radius: 0; */
}

.card:hover {
box-shadow: 0 3.2px 2.2px rgba(0, 0, 0, 0.02),
    0 7px 5.4px rgba(0, 0, 0, 0.028), 0 12.1px 10.1px rgba(0, 0, 0, 0.035),
    0 19.8px 18.1px rgba(0, 0, 0, 0.042), 0 34.7px 33.8px rgba(0, 0, 0, 0.05),
    0 81px 81px rgba(0, 0, 0, 0.07)
}

.card-img-top {
  height: 15em;
  object-fit: scale-down;
}
.card-title {
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.4em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  color: #333333;
}
.card-subtitle {
    font-weight: 800;
  color: #333333;
}
</style>