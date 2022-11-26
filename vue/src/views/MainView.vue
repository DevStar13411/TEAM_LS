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
        <button class="navbar-toggler" style="display: block;" type="button" data-bs-toggle="offcanvas" data-bs-target="#cart" @click="makeCartList">
          <i class="bi bi-cart3" style="font-size: 2rem;"></i>
        </button>
      </div>   
    </nav>
  </header>
  <main>

    <SideBarVue class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="sidebar" @categoryClick="getGoodsList"/>
    <h3 class="py-5">{{currentCategory}}</h3>
    <div>
        <div class="container text-start">
            <div class="row row-cols-2 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5">
                <div class="col my-2" v-for="item in goodList" v-bind:key="item.goodId">
                  <CardVue v-bind:item="item"/>
                </div>
            </div>
        </div>
    </div>
    <CartVue class="container offcanvas offcanvas-end navbar-nav-scroll" tabindex="-1" id="cart" style="max-height: 100%;" @moveToMap="mapView"/>
  </main>
</template>

<script>
import SideBarVue from '@/components/SideBar.vue';
import CardVue from '@/components/Card.vue';
import CartVue from '@/components/AddedProductList.vue';

export default {
	name : 'MainView',
  components:{
    SideBarVue,
    CardVue,
    CartVue
  },
  data : function() {
    return {
      latitude: Number(this.$route.query.latitude),
      longitude: Number(this.$route.query.longitude),
      goodList : [],
      priceList : {},
      cartList : [],
      currentCategory : ""
    };
  },
  methods : {
    getGoodsList(category) {
      let get_url =  "https://zzangbaguni.shop/goods";
      if(category!==undefined){
        if(category.name!=="전체"){
          get_url+= "/"+category.code;
        }
        this.currentCategory = category.name;
      }
      this.axios.get(get_url,{
        params: {
          latitude: this.latitude,
          longitude: this.longitude
        }
      }).then((res)=>{
        this.goodList = res.data.goods;
      }).catch((err) => {
        console.log(err);
      });
    },

    getPriceList(goodId) {
      if (this.priceList[goodId] === undefined) {
        let get_url = "https://zzangbaguni.shop/price";
        get_url += "/" + goodId;
        this.axios.get(get_url, {
          params: {
            latitude: this.latitude,
            longitude: this.longitude
          }
        }).then((res) => {
          this.priceList[goodId] = res.data;
        }).catch((err) => {
          console.log(err);
        });
      }
    },
    makeCartList(){
      this.cartList = this.$store.state.cart;
      console.log(this.cartList);
    },

    // MapView로 넘어가는 method -> 이후 goods 변경 필요함
    mapView() {
      this.$router.push({name: 'MapView', query:
        {latitude: this.latitude, longitude: this.longitude, goods:this.$store.getters.getcartProducts}});
    }

  },
  mounted() {//goodlist 컴포넌트가 마운트되면 getGoodList함수 호출
    this.getGoodsList();
  }   
};
</script>

<style>
</style>