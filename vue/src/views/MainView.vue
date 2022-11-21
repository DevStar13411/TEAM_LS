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
        <button class="navbar-toggler" style="display: block;" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="bi bi-cart3" style="font-size: 2rem;"></i>
        </button>
      </div>   
    </nav>
  </header>
  <main>
    <SideBarVue class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="sidebar" @categoryClick="getGoodsList"/>
    <div class="py-5">
        <div class="container text-start">
            <div class="row row-cols-2 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5">
                <div class="col my-2" v-for="item in goodList" v-bind:key="item.goodId">
                  <CardVue v-bind:item="item"/>
                </div>
            </div>
        </div>
    </div>
  </main>
</template>

<script>
import SideBarVue from '@/components/SideBar.vue';
import CardVue from '@/components/Card.vue';

export default {
	name : 'MainView',
  components:{
    SideBarVue,
    CardVue
  },
  data : function() {
    return {
      goodList : [],
      priceList : {}
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
    }
  },
  mounted() {//goodlist 컴포넌트가 마운트되면 getGoodList함수 호출
    this.getGoodsList();
  }   
};
</script>

<style>
</style>