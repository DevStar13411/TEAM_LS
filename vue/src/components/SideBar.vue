<template>
  <div class="flex-column flex-shrink-0 p-3 text-white bg-dark col-md-3 col-lg-2 d-md-block sidebar collapse" style="width: 280px;">
    <a class="align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
        <i class="bi bi-bucket" style="font-size: 1.5rem;"></i>
        <span class="fs-4"> 카테고리</span>
    </a>
    <hr>
    <ul class="nav nav-pills flex-column mb-auto" v-for="category in categories" v-bind:key="category.name">
      <li class="nav-item">
        <a class="nav-link text-white category" :class="{active: category.isActive}" @click="clickEventHandler(category)">
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
            {name:"전체", code:"", isActive: true},
            {name:"정육/난류", code:"30101", isActive: false},
            {name:"수산가공품", code:"30202", isActive: false},
            {name:"낙농/축산가공품", code:"30203", isActive: false},
            {name:"생선류", code:"30103", isActive: false},
            {name:"조미료/장류/식용유", code:"30204", isActive: false},
            {name:"채소류", code:"30102", isActive: false},
            {name:"과자/빙과류", code:"30205", isActive: false},
            {name:"차/음료/주류", code:"30206", isActive: false},
            {name:"이미용품", code:"30301", isActive: false},
            {name:"세탁/주방/가사용품", code:"30302", isActive: false}
            ]            
        };

    },
    methods : {
        clickEventHandler(category) {
            this.categories.forEach(cat => {cat.isActive=false;});
            category.isActive = true;
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