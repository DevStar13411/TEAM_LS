import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueGeolocation from 'vue-geolocation-api';

const app = createApp(App).use(router,VueGeolocation);
app.config.globalProperties.axios = axios;
app.mount('#app');
