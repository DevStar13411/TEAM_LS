<template lang="pug">
.wrapper
  .screen.-end(ref="cartItems")
    .app-bar
     img.logo(src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1315882/pngwave.png")
    .title Your cart
    transition(name="noContent")
      .no-content(v-if="$store.getters.getcartProducts.length === 0")
        p.text Your cart is empty.
    .cart-items
      transition-group(name="cartList" tag="div")
        .cart-item(v-for="item in $store.getters.getcartProducts" :key="item.goodId")
          .left
            .cart-image
              .image-wrapper
                img.image(:src="'https://zzangbaguni.shop/static/img/' + item.goodId + '.jpg'" alt="https://picsum.photos/300/500")
          .right
            .name {{item.goodName}}
            .count
              .button(@click="subOrder(item)") &lt;
              .number {{item.goodQuantity}}
              .button(@click="addOrder(item)") &gt;
    
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
    },
    moveToMap() {
      this.$emit('moveToMap');
    }
  },
};
</script>

<style lang="scss">
$white: #fff;
$yellow: #f6c90e;
$black: #303841;

body {
  font-family: "Rubik", sans-serif;
  color: $black;
}

.wrapper {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  flex-wrap: wrap;
  padding: 40px 20px;
  max-width: 720px;
  margin: 0 auto;

  &::before {
    content: "";
    display: block;
    position: fixed;
    width: 300%;
    height: 100%;
    top: 50%;
    left: 50%;
    border-radius: 100%;
    transform: translateX(-50%) skewY(-8deg);
    background-color: $yellow;
    z-index: -1;
    animation: wave 8s ease-in-out infinite alternate;
  }

  @keyframes wave {
    0% {
      transform: translateX(-50%) skew(0deg, -8deg);
    }

    100% {
      transform: translateX(-30%) skew(8deg, -4deg);
    }
  }
}

.screen {
  background-color: $white;
  box-sizing: border-box;
  width: 340px;
  height: 600px;
  box-shadow: 0 3.2px 2.2px rgba(0, 0, 0, 0.02),
    0 7px 5.4px rgba(0, 0, 0, 0.028), 0 12.1px 10.1px rgba(0, 0, 0, 0.035),
    0 19.8px 18.1px rgba(0, 0, 0, 0.042), 0 34.7px 33.8px rgba(0, 0, 0, 0.05),
    0 81px 81px rgba(0, 0, 0, 0.07);
  border-radius: 30px;
  overflow-y: scroll;
  padding: 0 28px;
  position: relative;
  margin-bottom: 20px;

  &::before {
    content: "";
    display: block;
    position: absolute;
    width: 300px;
    height: 300px;
    border-radius: 100%;
    background-color: $yellow;
    top: -20%;
    left: -50%;
    z-index: 0;
  }

  &::-webkit-scrollbar {
    display: none;
  }

  > .title {
    font-size: 24px;
    font-weight: bold;
    margin: 20px 0;
    position: relative;
  }
}

.app-bar {
  padding: 12px 0;
  position: relative;

  > .logo {
    display: block;
    width: 50px;
  }
}

.shop-items {
  position: relative;
}

.item-block {
  padding: 40px 0 70px;

  &:first-child {
    padding-top: 0;
  }

  > .image-area {
    border-radius: 30px;
    height: 380px;
    display: flex;
    align-items: center;
    overflow: hidden;

    > .image {
      display: block;
      width: 100%;
      filter: drop-shadow(0 30px 20px rgba(0, 0, 0, 0.2));
      transform: rotate(-24deg);
      margin-left: -16px;
    }
  }

  > .name {
    font-size: 20px;
    font-weight: bold;
    margin: 26px 0 20px;
    line-height: 1.5;
  }

  > .description {
    font-size: 13px;
    color: #777;
    line-height: 1.8;
    margin-bottom: 20px;
  }

  > .bottom-area {
    display: flex;
    justify-content: space-between;
    align-items: center;

    > .price {
      font-size: 18px;
      font-weight: bold;
    }

    > .button {
      cursor: pointer;
      background-color: $yellow;
      font-weight: bold;
      font-size: 14px;
      box-sizing: border-box;
      height: 46px;
      padding: 16px 20px;
      border-radius: 100px;
      box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
      transition: box-shadow 0.4s, background-color 0.2s;
      user-select: none;
      white-space: nowrap;
      position: relative;
      display: flex;
      align-items: center;
      overflow: hidden;

      &:hover {
        background-color: lighten($yellow, 10%);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      }

      &.-active {
        pointer-events: none;
        cursor: default;
      }

      > .cover {
        width: 16px;
        height: 16px;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;

        > .check {
          width: 100%;
          height: 100%;
          transform: translate(-100%, -73%) rotate(-45deg);
          position: absolute;
          left: 50%;
          top: 50%;

          &::before,
          &::after {
            content: "";
            display: block;
            background-color: $black;
            position: absolute;
            left: 0;
            bottom: 0;
            border-radius: 10px;
          }

          &::before {
            width: 3px;
            height: 50%;
          }

          &::after {
            width: 100%;
            height: 3px;
          }
        }
      }
    }
  }
}

.cart-items {
  position: relative;
}

.no-content {
  position: relative;

  > .text {
    font-size: 14px;
  }
}

.cart-item {
  display: flex;
  padding: 20px 0;

  > .right {
    > .name {
      font-size: 14px;
      font-weight: bold;
      line-height: 1.5;
      margin-bottom: 10px;
    }

    > .price {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 16px;
    }

    > .count {
      display: flex;
      align-items: center;

      > .number {
        font-size: 14px;
        margin: 0 14px;
        width: 20px;
        text-align: center;
      }

      .button {
        cursor: pointer;
        width: 28px;
        height: 28px;
        border-radius: 100%;
        background-color: #eee;
        font-size: 16px;
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: 0.2s;
        user-select: none;

        &:hover {
          background-color: #ddd;
        }
      }
    }
  }
}

.cart-image {
  width: 90px;
  height: 90px;
  border-radius: 100%;
  background-color: #eee;
  margin-right: 34px;

  > .image-wrapper {
    > .image {
      display: block;
      width: 140%;
      transform: rotate(-28deg) translateY(-40px);
      filter: drop-shadow(0 30px 20px rgba(0, 0, 0, 0.2));
    }
  }
}

.buttonText-leave-active,
.buttonText-enter-active {
  transition: opacity 0.2s, top 0.35s;
}
.buttonText-leave-to,
.buttonText-enter {
  opacity: 0;
}

.cartList-enter-active {
  transition: all 2s;

  > .right {
    > .name,
    > .price {
      transition: 0.4s;
    }

    > .name {
      transition-delay: 0.7s;
    }

    > .price {
      transition-delay: 0.85s;
    }

    > .count {
      transition: opacity 0.4s;
      transition-delay: 1s;
    }
  }

  .cart-image {
    transition: 0.5s cubic-bezier(0.79, 0.01, 0.22, 1);

    > .image-wrapper {
      transition: 0.5s cubic-bezier(0.79, 0.01, 0.22, 1) 0.1s;
    }
  }
}

.cartList {
  &-enter {
    > .right {
      > .name,
      > .price {
        opacity: 0;
        transform: translateX(30px);
      }

      .count {
        opacity: 0;
      }
    }

    .cart-image {
      transform: scale(0);

      > .image-wrapper {
        transform: scale(0);
      }
    }
  }

  &-leave-active {
    transition: 0.7s cubic-bezier(0.79, 0.01, 0.22, 1);
    position: absolute;
  }

  &-leave-to {
    transform: scale(0);
    opacity: 0;
  }

  &-move {
    transition: 0.7s cubic-bezier(0.79, 0.01, 0.22, 1);
  }
}

.noContent {
  &-enter-active,
  &-leave-active {
    transition: opacity 0.5s;
    position: absolute;
  }

  &-enter,
  &-leave-to {
    opacity: 0;
  }
}
</style>
