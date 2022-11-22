<template>
  <div id="addedproductlist">
    <div>
      <div>
        <div
          v-if="$store.getters.getcartProducts.length === 0"
          class="shopped-item py-5"
        >
          장바구니에 담은 상품이 없습니다.
        </div>
        <div v-else>
          <div
            class="shopped-item"
            :key="index"
            v-for="(cartproduct, index) in $store.getters.getcartProducts"
          >
            <div class="shopped-imgtitle">
              <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + cartproduct.goodId + '.jpg'" alt="https://picsum.photos/300/500">
              <div class="shopped-title">{{ cartproduct.goodName }}</div>
            </div>
            <div class="row" id="editquantity">
              <div class="col">
                <button @click="addOrder(cartproduct)">+</button>
              </div>
              <div class="col">
                {{ cartproduct.goodQuantity }}
              </div>
              <div class="col">
                <button @click="subOrder(cartproduct)">-</button>
              </div>
            </div>
            <hr/>
          </div>
          <div class="py-5">
            <button>지도에서 보기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddedProductList",
  methods: {
    addOrder(cartproduct) {
      this.$store.dispatch("addOrder", cartproduct);
    },
    subOrder(cartproduct) {
      this.$store.dispatch("subOrder", cartproduct);
    }
  },
};
</script>