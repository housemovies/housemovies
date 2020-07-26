<template>
  <div class="position-relative bg-grey-" :style="style">
    <div class="WAL" style="height: 50%">
      <q-carousel
        animated
        v-model="slide"
        infinite
        :autoplay="autoplay"
        arrows
        transition-prev="slide-right"
        transition-next="slide-left"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
        style="height: 550px;opacity: 0.9;"
      >
        <q-carousel-slide position="top" :name="key"  v-for="(item, key) in imagenes" :key="key"  :img-src="item.imagen" >
          <br><br><br>
          <div class="col-12  text-h3 q-pl-xl q-pa-md  text-white ">
            prueba de texto para mostrar
          </div>
          <div class="col-12  text-subtitle1 q-pl-xl  q-pb-md text-white ">
            <q-icon class="text-h6 q-pb-sm" color="white" name="theaters" /> 2020 <q-icon class="text-h6 q-pb-sm" color="white" name="alarm" /> 90 Minutos
          </div>
          <div class="col-12  text-subtitle1 q-pl-xl q-pb-md text-white ">
            Texto mas largo de prueba para la sipnosis
          </div>
          <div class="col-2 text-subtitle2 q-pl-xl text-white">
            <q-btn clickable  outline rounded  color="white" size="md" label="Ver Pelicula" style="margin-left: 5px;"  type="a" target="_blank"  href="https://www.youtube.com/watch?v=UVPkb6WEBV0" />
            <q-btn clickable  outline rounded  color="white" size="md" label="Ver Triller" style="margin-left: 5px;"  type="a" target="_blank"  href="https://www.youtube.com/watch?v=UVPkb6WEBV0" />
          </div>
        </q-carousel-slide>
        <!-- <q-carousel-slide :name="1" img-src="https://cdn.quasar.dev/img/parallax1.jpg" /> -->
        <!-- <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg" />
        <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg" /> -->
      </q-carousel>
    </div>
    <q-layout view="lHh Lpr lFf" class="WAL__layout shadow-9 q-mb-sm" style="height: 70%;margin-bottom: 2%;" container>
      <q-header elevated>
        <q-toolbar class="bg-grey-3 text-black row ">
          <div class="col-1">
            <q-btn v-if="leftDrawerOpen == true" round flat icon="close" class="WAL__drawer-close" @click="leftDrawerOpen = !leftDrawerOpen"  />
            <q-btn v-if="leftDrawerOpen == false" round flat icon="menu" class="q-mr-sm" @click="leftDrawerOpen = !leftDrawerOpen" />
          </div>
          <div class="col-7 text-h5 q-pl-sm">
            {{texto}}
          </div>
          <div class="col-4">
            <q-input rounded outlined dense class="WAL__field full-width" bg-color="white" v-model="search" placeholder="Buscar Pelicula">
              <template slot="prepend">
                <q-icon name="search" />
              </template>
            </q-input>
          </div>
        </q-toolbar>
      </q-header>

      <q-drawer
        v-model="leftDrawerOpen"
        bordered
        :breakpoint="690"
        content-class="bg-grey-2"
      >
        <q-toolbar class="bg-grey-3">
          <q-avatar class="cursor-pointer">
            <img src="https://cdn.quasar.dev/app-icons/icon-128x128.png" />
          </q-avatar>
          <q-space />
        </q-toolbar>
<!-- 
        <q-toolbar class="bg-grey-2">
          <q-input rounded outlined dense class="WAL__field full-width" bg-color="white" v-model="search" placeholder="Buscar Pelicula">
            <template slot="prepend">
              <q-icon name="search" />
            </template>
          </q-input>
        </q-toolbar> -->

        <q-scroll-area style="height: calc(100% - 100px)">
          <menu-modulos @close="leftDrawerOpen = false"/>
          
        </q-scroll-area>
      </q-drawer>

      <q-page-container class="bg-grey-2">
        <router-view :key="$route.fullPath" />
      </q-page-container>

    </q-layout>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MainLayout',
  middleware: 'guest',
  data () {
    return {
      leftDrawerOpen: false,
      links: [],
      left: false,
      right: false,
      search: '',
      message: '',
      slide: 1,
      autoplay: true,
      imagenes: []
    }
  },
  computed: {
    ...mapGetters('menu', ['sub_menu_active']),
    ...mapGetters('head', ['texto']),
    style () {
      return {
        height: this.$q.screen.height + 'px'
      }
    }
  },
  mounted () {
    this.getMenus()
    this.getImagenesMuestra()
  },
  methods: {
    async getMenus () {
      try {
        const data = await this.Get('principal/menus')
        this.$store.commit('menu/modulos', data)
      } catch ({ message }) {
        console.error(message)
      }
    },
    async getImagenesMuestra () {
      try {
        this.imagenes = await this.Get('principal/imagen_muestra')
      } catch ({ message }) {
        console.error(message)
      }
    }
  }
}
</script>

<style lang="sass">

::-webkit-scrollbar 
  display: none
.my-card
  width: 100%
  max-width: 165px
  height: 230px
  
.WAL
  width: 100%
  padding-bottom: 20px
  &__layout
    margin: 0 auto
    z-index: 4000
    
    width: 90%
    max-width: 1124px
    border-radius: 5px
  &__field.q-field--outlined .q-field__control:before
    border: none
  .q-drawer--standard
    .WAL__drawer-close
      display: none
@media (max-width: 850px)
  .WAL
    padding: 0
    &__layout
      width: 100%
      border-radius: 0
@media (min-width: 691px)
  .WAL
    &__drawer-open
      display: none
.conversation__summary
  margin-top: 4px
.conversation__more
  margin-top: 0!important
  font-size: 1.4rem
</style>
