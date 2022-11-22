<template>
    <!-- <nav class="col-md-3 col-lg-2 d-md-block sidebar collapse">
        <div class="position-sticky pt-3">
            <ul class="nav flex-column list-group">
                <li class="nav-item list-group-item" style="border: 0px;">
                    <h4>카테고리</h4>
                </li>
            </ul>
            <ul class="nav flex-column list-group" v-for="category in categories" v-bind:key="category.name">
                <li class="nav-item list-group-item">
                    <a class="nav-link category" @click="clickEventHandler(category)"> {{category.name}}</a>
                </li>
            </ul>
      </div>
    </nav> -->
    <div class="flex-column flex-shrink-0 p-3 text-white bg-dark col-md-3 col-lg-2 d-md-block sidebar collapse" style="width: 280px;">
    <a class="align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
        <i class="bi bi-bucket" style="font-size: 1.5rem;"></i>
        <span class="fs-4"> 카테고리</span>
    </a>
    <hr>
    <ul class="nav nav-pills flex-column mb-auto" v-for="category in categories" v-bind:key="category.name">
      <li class="nav-item">
        <a class="nav-link text-white category" @click="clickEventHandler(category)">
            <i class="bi bi-caret-right-fill" style="font-size: 0.7rem;"></i> {{category.name}}
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
	name : 'SideBar',
    data : function() {
        return {
          categories : [
            {name:"전체",code:undefined},
            {name:"정육/난류",code:"30101"},
            {name:"수산가공품",code:"30202"},
            {name:"낙농/축산가공품",code:"30203"},
            {name:"생선류",code:"30103"},
            {name:"조미료/장류/식용유",code:"30204"},
            {name:"채소류",code:"30102"},
            {name:"과자/빙과류",code:"30205"},
            {name:"차/음료/주류",code:"30206"},
            {name:"이미용품",code:"30301"},
            {name:"세탁/주방/가사용품",code:"30302"}
            ]            
        };

    },
    methods : {
        clickEventHandler(category) {
            this.$emit('categoryClick',category);
        }
    }    
};
</script>

<style scoped>
.category {
  cursor:pointer;
  color: black;  
  text-align: start;
}
</style>