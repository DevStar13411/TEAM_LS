<template>
    <header>
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <div class="container-fluid">
        <button class="navbar-toggler" style="display: block;" type="button" data-bs-toggle="offcanvas" data-bs-target="#sidebar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <router-link to="/" class="navbar-brand">
          <img alt="Vue logo" src="@/assets/logo_small.png" style="height:40px;" />
          ZzangBaguni
        </router-link>
        <button class="navbar-toggler" style="display: block;" type="button" data-bs-toggle="offcanvas" data-bs-target="#cart">
          <i class="bi bi-cart3" style="font-size: 2rem;"></i>
        </button>
      </div>   
    </nav>
  </header>
  <main>
    <SideBarVue class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="sidebar" @categoryClick="getGoodsList"/>
    <div class="py-5">
        <div class="container text-start">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4">
                <div class="col my-2" v-for="item in goodList" v-bind:key="item.goodId">
                  <CardVue @put_in_cart = "getCartList" v-bind:item="item"/>
                </div>
            </div>
        </div>
    </div>
    <div class="offcanvas offcanvas-end" data-bs-scroll="true" tabindex="-1" id="cart">
      <CartVue v-bind:goodList="goodList"/>
    </div>
  </main>
</template>

<script>
import SideBarVue from '@/components/SideBar.vue';
import CardVue from '@/components/Card.vue';
import CartVue from '@/components/Cart.vue';

export default {
	name : 'MainView',
  components:{
    SideBarVue,
    CardVue,
    CartVue
  },
  data : function() {
    return {
      goodList : [],
      priceList : {},
      cartList : new Set([])
    };
  },
  methods : {
    getGoodsList(category) {
      let get_url =  "https://zzangbaguni.shop/goods";
      if(category!==undefined){
        get_url+= "/"+category;
      }
      this.axios.get(get_url,{
        params: {
          latitude: this.$route.query.latitude,
          longitude: this.$route.query.longitude
        }
      }).then((res)=>{
        this.goodList = res.data.goods;
      }).catch((err) => {
        console.log(err);
      });
    },
    itemClick(item) {
      this.$router.push({name : 'GoodView', query : {itemNo : item.goodId}});
    },
    getPriceList(goodId) {
      if (this.priceList[goodId] === undefined) {
        let get_url = "https://zzangbaguni.shop/price";
        get_url += "/" + goodId;
        this.axios.get(get_url, {
          params: {
            latitude: this.$route.query.latitude,
            longitude: this.$route.query.longitude
          }
        }).then((res) => {
          this.priceList[goodId] = res.data;
        }).catch((err) => {
          console.log(err);
        });
      }
    },
    getCartList(item){
      this.cartList.add(item);//추가할 제품이 장바구니의 제품과 일치하지 않을 경우, 장바구니에 새로 추가
      console.log(this.cartList);
    }
  },
  mounted() {//goodlist 컴포넌트가 마운트되면 getGoodList함수 호출
    this.getGoodsList();
  }   
};
</script>

<style>
</style>