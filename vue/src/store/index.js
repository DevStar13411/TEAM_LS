
import Vuex from 'vuex';



export const store = new Vuex.Store({
    // 스토어 객체 옵션 설정
    state: {
        cart: []
    },
   actions: {
        //'+'버튼 클릭 시
        addOrder({state, commit}, product) {
            // const productItem = state.products.find(item => item.id === product.id);
            const cartItem = state.cart.find(item => item.goodId === state.cart.goodId); // 기존의 카트에 존재하면 product가 cartItem이 되는것
            if (!cartItem) {
                commit('pushProductToCart', product); //추가할 제품이 장바구니의 제품과 일치하지 않을 경우, 장바구니에 새로 추가
            } else {
                commit('incrementItemQuantity', cartItem); //일치할 경우, 장바구니의 제품 수량을 증가}
            }
            
            },
        //'-'버튼 클릭 시
        subOrder({state, commit}, product) {
        	//장바구니에 담긴 아이템이 있을 경우
            const cartItem = state.cart.find(item => item.productId === product.id);
            if (cartItem.quantity > 0) {
                commit('decrementItemQuantity', cartItem); //장바구니의 제품 수량 -1
            }
        	//장바구니에 담긴 아이템이 없을 경우
            else {
                alert("장바구니에 담은 수량 없음");
            }
        }
    },
    mutations: {
        //장바구니에 제품을 추가
        pushProductToCart(state, product) { 
            state.cart.push({
                goodId: product.goodId,
                goodSmlclsCode: product.goodSmlclsCode,
                goodName: product.goodName,
                quantity: 0
            });
        },
        //쇼핑 카트의 아이템 수량 증가
        incrementItemQuantity(state, cartItem) { 
            state.cart[cartItem].quantity++;
        },
        //쇼핑 카트의 아이템 수량 감소
        decrementItemQuantity(state, cartItem) { 
            state.cart[cartItem].quantity--;
        }
    },
    getters: {
        getcartProducts(state) {
            return state.cart.map(cartItem => {
                return {
                    goodId: cartItem.goodId,
                    goodName: cartItem.goodName,
                    // price: product.price,
                    // inventory: product.inventory,
                    goodQuantity: cartItem.quantity,
                    goodSmlclsCode: cartItem.goodSmlclsCode,
                };
            });
        }
       
    },
});

