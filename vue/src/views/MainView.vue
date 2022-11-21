<template>
  <div class="row">
    <SideBarVue @categoryClick="getGoodsList"/>
    <div class="col-md-9 py-5">
        <div class="container text-start">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4">
                <div class="col my-2" v-for="item in goodList" v-bind:key="item.goodId">
                  <CardVue v-bind:item="item"/>
                </div>
            </div>
        </div>
    </div>
  </div>
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