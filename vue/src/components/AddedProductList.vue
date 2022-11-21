<template>
  <div id="addedproductlist">
    <div>
      <div>
        <div
          v-if="$store.getters.getcartProducts.length === 0"
          class="shopped-item"
        >
          장바구니에 담은 상품이 없습니다.
        </div>
        <div
          v-else
          class="shopped-item"
          :key="index"
          v-for="(cartproduct, index) in $store.getters.getcartProducts"
        >
          <div class="shopped-imgtitle">
            <img class="card-img-top" :src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500">
            <div class="shopped-title">{{ cartproduct.title }}</div>
          </div>
          <div id="editquantity">
            <button @click="subOrder(cartproduct)">-</button>
            <div>
              {{ cartproduct.quantity }}
            </div>
            <button @click="addOrder(cartproduct)">+</button>
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