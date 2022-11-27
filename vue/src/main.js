import { createApp } from 'vue';

import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueGeolocation from 'vue-geolocation-api';
import { store } from './store';

import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap-icons/font/bootstrap-icons.css';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { fab } from '@fortawesome/free-brands-svg-icons';

library.add(fab);

const app = createApp(App).use(router,VueGeolocation).use(store);
app.component('font-awesome-icon', FontAwesomeIcon);
app.config.globalProperties.axios = axios;
app.mount('#app');

